def main():
	import boto3
	from sys import argv
	from pdb import set_trace
	mybucket = raw_input("Provide the name of an existing bucket: ")
	print "Uploading may take time depending on the file size.\n"
	s3 = boto3.resource('s3')
	#set_trace()
	for filename in argv[1:]:
		try:
			s3.Object(mybucket, filename).put(Body = open(filename, 'rb'))
			print filename + " uploaded successfully."
		except:
			print "Error in uploading " + filename + " Moving on to the next file."

if __name__ == "__main__":
	main()
