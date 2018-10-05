#!/bin/bash

echo "Downloading Elastic Search and Kibana..."

wget 'https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-oss-6.4.2.tar.gz'
wget 'https://artifacts.elastic.co/downloads/kibana/kibana-oss-6.4.2-linux-x86_64.tar.gz'

# Unzip
tar -xvzf elasticsearch-oss-6.4.2.tar.gz
tar -xvzf kibana-oss-6.4.2-linux-x86_64.tar.gz

# Set simlinks
ln -s elasticsearch-6.4.2 elasticsearch-current
ln -s kibana-6.4.2-linux-x86_64 kibana-current

