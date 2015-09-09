f = open('dirList.txt', 'w')
Dir.foreach('.') do |item|
	next if item == '.' or item == '..' or item == 'dirList.txt' or item == 'directoryListing.rb'
	f.write(item)
	f.write("\n")
end
