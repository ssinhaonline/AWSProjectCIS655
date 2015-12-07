from pdb import set_trace

def create_table(jsonobj):
	import boto3
	dynamodb = boto3.resource('dynamodb')
	tablename = 'Reviews'
	row = jsonobj[0]
	keyschema = [None] * 2
	attributeschema = [None] * 2
	from sys import getsizeof
	for key in row:
		#print 'AttributeName: ' + str(key)
		if str(type(row[key])) == "<type 'int'>":
			attrtype = 'N'
		elif str(type(row[key])) == "<type 'str'>":
			attrtype = 'S'
		else:
			attrtype = 'N'
		#print 'AttributeType: ' + str(attrtype)

		if key == 'cluster':
			keytype = 'HASH'
			keyschema[0] = {'AttributeName' : key, 'KeyType' : keytype}
			attributeschema[0] = {'AttributeName' : key, 'AttributeType' : attrtype}
		elif key == 'rating':
			keytype = 'RANGE'
			keyschema[1] = {'AttributeName' : key, 'KeyType' : keytype}
			attributeschema[1] = {'AttributeName' : key, 'AttributeType' : attrtype}
		else:
			keytype = 'NONE'
		#print keytype
	
	#print len(jsonobj)
	#print getsizeof(row)
	#print attributeschema
	#print keyschema
	#set_trace()
	table = dynamodb.create_table(TableName = tablename, KeySchema = keyschema, AttributeDefinitions = attributeschema, ProvisionedThroughput = {'ReadCapacityUnits' : 80, 'WriteCapacityUnits' : 80})
	table.meta.client.get_waiter('table_exists').wait(TableName = tablename)
	#set_trace()
	for row in jsonobj:
		table.put_item(Item = row)

def main():
	import json
	filehandle = open('./out.json')
	data = json.load(filehandle)
	#print json.dumps(data)
	create_table(data)


if __name__ == "__main__":
	main()
