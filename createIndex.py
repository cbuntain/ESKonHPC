#!/usr/bin/python

import json
import sys
import requests

from requests.auth import HTTPBasicAuth

index_info = {
    "settings": {
        "index.mapping.ignore_malformed": True,
        "number_of_shards": 12,
        "number_of_replicas": 1,
        "analysis": {
            "analyzer": {
                "english_exact": {
                    "tokenizer": "standard",
                    "filter": [
                        "lowercase"
                    ]
                }
            }
        }
    },
    "mappings": {
            "properties": {
                "coordinates": {
                    "properties": {
                        "coordinates": {
                            "type": "geo_point"
                        },
                        "type": {
                            "type": "text",
                            "fields": {
                                "keyword": {
                                    "type": "keyword",
                                    "ignore_above": 256
                                }
                            }
                        }
                    }
                },
                "place": {
                    "properties": {
                        "bounding_box": {
                            "properties": {
                                "coordinates": {
                                    "type": "geo_point"
                                },
                                "type": {
                                    "type": "text",
                                    "fields": {
                                        "keyword": {
                                            "type": "keyword",
                                            "ignore_above": 256
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "user": {
                    "properties": {
                        "created_at": {
                            "type": "date",
                            "format": "EEE MMM dd HH:mm:ss Z YYYY||strict_date_optional_time"
                        },
                        "screen_name": {
                            "type": "text"
                        }
                    }
                },
                "text": {
                    "type": "text",
                    "analyzer": "english",
                    "fields": {
                        "exact": {
                            "type": "text",
                            "analyzer": "english_exact"
                        },
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "smapp_text": {
                    "type": "alias",
                    "path": "text"
                },
                "created_at": {
                    "type": "date",
                    "format": "EEE MMM dd HH:mm:ss Z YYYY||strict_date_optional_time"
                },
                "smapp_datetime": {
                    "type": "alias",
                    "path": "created_at"
                },
                "smapp_embedding": {
                    "type": "dense_vector",
                    "dims": 100
                },
                "smapp_username": {
                    "type": "alias",
                    "path": "user.screen_name"
                }
            }
        }
}

es_url = sys.argv[1]
index_name = sys.argv[2]

res = requests.put(es_url + "/" + index_name, data=json.dumps(index_info), headers={"Content-Type": "application/json"}, auth=HTTPBasicAuth("elastic", "ElasticSearchFTW!"))
print("Result:", res.status_code, json.dumps(res.text, indent=2))
