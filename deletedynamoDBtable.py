def main():
	import boto3
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('Reviews')
	table.delete()

if __name__ == '__main__':
	main()
