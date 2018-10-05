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
	print(tweet["id"], tweet["text"])

	# Build the URL
	tweetId = tweet["id"]
	targetUrl = "{0}/{1}/{2}/{3}".\
		format(elasticUrl, indexName, dataType, tweetId)

	print("Posting to ES URL:", targetUrl)
	r = requests.put(targetUrl, data=line, headers={"Content-Type": "application/json"})
	print("Result:", r.status_code, r.text)


inFilePtr.close()




