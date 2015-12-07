def main():
	import boto3
	from sys import argv
	bucketname = argv[1]
	filename = argv[2]
	s3 = boto3.resource('s3')
	try:
		bucket = s3.Bucket(bucketname)
		flag = 0
		for key in bucket.objects.all():
			if key.key == filename:
				key.delete()
				flag = 1
		if flag == 0:
			print "File not found in bucket."
		else:
			s3.Object(bucketname, filename).put(Body = open('./' + filename, 'rb'))
			print filename + ' has been updated in ' + bucketname

	except:
		print 'Some error occured.'

if __name__ == '__main__':
	main()
