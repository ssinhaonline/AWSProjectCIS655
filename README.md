# AWSProjectCIS655
CIS655 Course Project on AWS. Fall 2015.

###Authors
Souradeep Sinha and Simon Lee

###Prerequisites
Before starting this project, we must make sure of the following for the project to run smoothly:
1.	awscli must be installed on all EC2 machines as well as the local machine. This is the tool that provides an interface with the AWS Servers and all of its resources.

2.	awscli must be configured with proper credentials (access key and access secret) with the aws config command. In our case, all the EC2 and local instances were preconfigured to suit our needs.
To install, use: 
    
    $ sudo apt-get install awscli

3.	git must be installed on all the AMIs.
To install, use: 
    
    $ sudo apt-get install git

4.	A KeyPair that corresponds to the users account is needed to provide authentication when SSHing into the EC2 instances. This is very important and provides security to the AWS consumer.

5.	Python must be installed on all the machines. In our case, all AMIs including the local machine were operating on Ubuntu which provides Python 2.7 with it’s distributions.

6.	It must be made sure that the following packages are installed on all the AMIs. To install click on the respective links:
  [python-pip] - (Python Package Management)
  
  [boto3] - (Python AWS API)
	
	[nltk] - (Natural Language Translation Kit)
	
	[sklearn] - (Scikit Learn – for clustering data)
	
	[numpy] - (Python Numerical Analysis package)
	
	[scipy] - (Python Scientific Analysis package)

###Program Flow
1.	Change directory to project folder.

2.	Create a bucket in S3 using:

    $ python createBucket.py

After showing a brief memorandum, the program will ask for user input for the Bucket name:

    $ Enter bucket name : <bucket_name>
 

3.	Upload the following files from the project folder into S3 bucket just created using:

    $ python upload2bucket.py smallfoods.txt timeanalysis.txt preprocessor.py dynamoDBdriver.py process_and_load deletedynamoDBtable.py
	
	  The program should ask for the destination bucket name. Enter the same bucket used in Step 2.
    $ Provide the name of an existing bucket : <bucket_name>
 

4.	For all EC2 instances, do the following:

    a.	Run the AMI starter script with the AMI name as follows:
      
        $ ./startScript <instance_name>
 

    b.	Wait for the AMI to start and initialize, which may take a while depending on AWS server loads or internet speeds. Type yes when asked for fingerprint authentication.

    c.	Now, the user is logged into the AMI.

    d.	Ensure git has been initialized on the home folder, otherwise use:
      
        $ git init

    e.	Clone the CIS655ConnectorRepository using the following link:

        $ git clone https://github.com/ssinhaonline/CIS655ConnectorRepository.git
		    
		  Use your Github account details for cloning.
 
    f.	Change directory to CIS655ConnectorRepository using:

        $ cd ./CIS655ConnectorRepository
 
    g.	Download all files from the bucket <bucket_name> using:
        
        $ download_from_bucket.py <bucket_name> -all
 
    h.	Use the process_and_load shell script to process smallfoods.txt and upload it to DynamoDB table called Reviews using:
        
        $ ./process_and_load <instance_name>
 
    i.	Perform queries on the table from the AWS Dashboard. For example, find out all the rows that belong to Cluster 7.

    j.	This is the cleanup stage. Delete the DynamoDB table to avoid being charged money for utilizing resources using:

        $ python deletedynamoDBtable.py

    k.	Update the text file timeanalysis.txt in the S3 bucket using:

        $ python updateS3file.py <bucket_name> <filename>
 
    l.	Change to home directory and perform cleanup using:
        
        $ rm -rf *
		
		  This step is optional. It is a good idea to leave the EC2 instance empty before logging off.
		
    m.	Log out of the AMI using: 
        
        $ logout
 
5.	After all the instances have completed going through Step 4, download the file timeanalysis.txt to obtain all the values of the different EC2 instances.

