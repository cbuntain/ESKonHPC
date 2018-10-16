import requests
import codecs
import json
import sys
import gzip
import bz2

try:
	elasticUrl = sys.argv[1]
	indexName = sys.argv[2]
	inFilePath = sys.argv[3]
except:
	print("Usage: postTwitter.py <http://localhost:PORT> <index_name> <tweet_path.json[.gz|.bz2]>")
	sys.exit(-1)

# What type of object is this?
dataType = "status"

inFilePtr = None
if inFilePath.endswith(".gz"):
	inFilePtr = gzip.open(inFilePath, 'rb')
elif inFilePath.endswith(".bz2"):
	inFilePtr = bz2.open(inFilePath, 'rb')
else:
	inFilePtr = open(inFilePath, 'r')

batch_size = 1000
bulk_post_data = []

# For each line in our file, read in and parse tweet
for line in inFilePtr:
	unicodeLine = line
	if ( type(line) == bytes ):
		unicodeLine = line.decode("utf8")

	if ( len(unicodeLine) == 0 ):
		continue

	tweet = json.loads(unicodeLine)

	# Skip end line
	if ( "info" in tweet ):
		continue

	# Debug
	# print(tweet["id"], tweet["text"])

	# Build the URL
	tweetId = tweet["id"]
	targetUrl = "{0}/{1}/{2}/{3}".\
		format(elasticUrl, indexName, dataType, tweetId)

	op_json = json.dumps({ "index" : { "_index" : indexName, "_type" : dataType, "_id" : tweetId } })
	bulk_post_data.append((op_json, unicodeLine))

	if ( len(bulk_post_data) == batch_size ):
		print("Posting %d tweets..." % batch_size )
		
		# Create the bulk request
		local_json_data = "\n".join(["\n".join(pair) for pair in bulk_post_data])

		# make bulk request 
		targetUrl = "{0}/_bulk".format(elasticUrl)
		res = requests.post(targetUrl, data=local_json_data, headers={"Content-Type": "application/json"})
		print("Result:", res.status_code, res.text)

		# Reset bulk data
		bulk_post_data = []


inFilePtr.close()

if ( len(bulk_post_data) > 0 ):
	# Create the bulk request
	local_json_data = "\n".join(["\n".join(pair) for pair in bulk_post_data])

	# make bulk request 
	targetUrl = "{0}/_bulk".format(elasticUrl)
	res = requests.post(targetUrl, data=local_json_data, headers={"Content-Type": "application/json"})
	print("Result:", res.status_code, res.text)


