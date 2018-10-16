#!/bin/bash

esport=9200
kbport=5601

# TODO: Update this path to point to your directory
TOP_ES_PATH=$(dirname "$0")

# You can leave these alone
ES_PATH=$TOP_ES_PATH/elasticsearch-current/
KB_PATH=$TOP_ES_PATH/kibana-current/

# Print port info to your slurm log
echo "ES Running on:" $(hostname)
echo "ElasticSearch at:" $esport
echo "Kibanna at:" $kbport

# Start ElasticSearch in daemon mode
$ES_PATH/bin/elasticsearch -d -Ecluster.name=json_search_cluster -Enode.name=node_1 -Enetwork.host=_local_ -Ehttp.port=$esport

# Spin up kibana, pointing to your ES installation
$KB_PATH/bin/kibana --elasticsearch http://localhost:$port --port $kbport


