#!/usr/bin/python

import sys
import requests

index_info = {
  "mappings": {
    "_default_": {
      "properties": {
        "coordinates":{
          "properties": {
            "coordinates": {
              "type": "geo_point"
            },
            "type":{
              "type": "text",
              "fields": {
                "keyword":{
                  "type":"keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        },
        "created_at": {
          "type": "date",
          "format": "EEE MMM dd HH:mm:ss Z YYYY"
        }
      }
    }
  }
}

es_url = sys.argv[1]
index_name = sys.argv[2]

resp = requests.put(es_url + "/" + index_name, data=index_info)
print("Result:", res.status_code, res.text)
