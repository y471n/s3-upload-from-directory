require 'aws-sdk-core'
require 'aws-sdk-resources'

access_key = 'XXXXXXXXXXX'
secret_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
region_s3 = 'ap-southeast-1'
bucket_name = 'bucket'
permission = 'public-read'

s3 = Aws::S3::Resource.new(
		credentials: Aws::Credentials.new(access_key, secret_key),
		region: region_s3
	)


File.open('dirList.txt', 'r+') do |f|
	old_pos = 0
	upload_counter = 0
	f.each do |line|
		upload_counter = upload_counter + 1
		break if upload_counter > 10
		if line.chomp.end_with? "jpg"
				# Upload file to s3
				obj = s3.bucket(bucket_name).object('test/'+line.chomp)
				obj.upload_file('./'+line.chomp, acl:permission)
				puts obj.public_url

				# Rename extension
				f.pos = old_pos
				f.print line.gsub('jpg', 'don')
				old_pos = f.pos
		else
				f.pos = old_pos
				f.print line
				old_pos = f.pos
			end
	end
end
