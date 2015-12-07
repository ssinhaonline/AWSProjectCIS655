'''
@authors: Souradeep Sinha(ssinhaonline) and Simon Lee(s19920513)
This code creates a bucket as specified by the user. The bucket name could have been taken as a command line arguement, but it is advisable that the user reads the bucket naming considerations before he inputs the name.
'''
def main():
	import sys
	import boto3
	from botocore import exceptions
	s3 = boto3.resource('s3')
	blah = raw_input("This code creates a bucket from the command line.\nWhile naming a bucket, please make sure it is unique as the bucket namespace is universal and is shared all throughout Amazon S3 customers.\nShould you choose a name that is not available, this code will safely give you an error message and will prompt you to try another time.\nPress enter to continue..")
	try:
		bucket_name = raw_input("\nEnter bucket name: ")
		response = s3.create_bucket(Bucket = bucket_name)
		print "\nBucket has been created."
		print response
	except:
		print "Client Error. Please select another name for your bucket and try again!"
	
if __name__ == "__main__":
	main()


