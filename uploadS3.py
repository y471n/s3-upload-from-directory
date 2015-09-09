# require 'aws-sdk-core'
# require 'aws-sdk-resources'

access_key = 'XXXXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
region_s3 = 'ap-southeast-1'
bucket_name = 'bucket'
permission = 'public-read'

# s3 = Aws::S3::Resource.new(
# 		credentials: Aws::Credentials.new(access_key, secret_key),
# 		region: region_s3
# 	)
import os
import fileinput
import boto3
from boto3.session import Session




session = Session(aws_access_key_id=access_key,
				  aws_secret_access_key=secret_key,
				  region_name=region_s3)

s3 = session.resource('s3')
thisdir = os.path.dirname(os.path.realpath(__file__)) + '/';


f = open('dirList.txt', 'r+')
for line in iter(f.readline, ''):
	print line
	if line.rstrip().endswith('jpg'):
		# Upload the file
		print 'Uploading file'
		fpath = os.path.dirname(os.path.realpath(__file__)) + '/' + line.rstrip()
		sendFile = open(fpath, 'rb')
		# print fpath
		s3.Bucket(bucket_name).put_object(ACL='public-read', ContentType='image',
Key='test/'+line.rstrip(), Body=sendFile)
		# Change file name
		line = line.rstrip().replace("jpg","don")
	else:
		print 'Not uploading'
		line = line.rstrip()
	try:
		old_pos
	except:
		print 'not defined'
	else:
		f.seek(old_pos)
		f.write(line+'\n')
	old_pos = f.tell()
