#!/usr/bin/python

import sys
import requests

es_url = sys.argv[1]
index_name = sys.argv[2]

res = requests.delete(es_url + "/" + index_name)
print("Result:", res.status_code, res.text)
