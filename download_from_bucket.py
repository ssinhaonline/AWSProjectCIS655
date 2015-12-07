def main():
	import boto3
	import botocore
	from pdb import set_trace
	from sys import argv, exit

	s3 = boto3.resource('s3')
	try:
		mybucket = s3.Bucket(argv[1])
		count = 1
		file_dict = {}
		print "\nContents of bucket: \n"
		for key in mybucket.objects.all():
			print str(count) + ' ' + key.key
			file_dict[count] = key.key
			count += 1
		print "Select the file numbers (separated by commas) you want to download. Enter 0 for all files."
		set_trace()
		ch = raw_input().split(",")
		choices = []
		for i in ch:
			try:
				choices.append(int(i))	
			except:
				print "Invalid input: " + i
				pass
		if (len(choices) == 1) and (choices[0] == 0):
			#Download all files
			for key in mybucket.objects.all():
				s3.meta.client.download_file(mybucket.name, key.key, './' + key.key + '.s3download')
				print key.key + ' downloaded successfully.'
			print 'All files downloaded.'
		else:
			for choice in choices:
				filename = file_dict[choice]
				s3.meta.client.download_file(mybucket.name, filename, './' + filename + '.s3download')
				print filename + ' downloaded successfully.'

	except:
		print "Error while fetching bucket."
		exit()


if __name__ == "__main__":
	main()
