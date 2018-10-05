#!/bin/bash

#SBATCH --job-name=elasticSearch
#SBATCH --nodes=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=8GB
#SBATCH --time=48:00:00

module purge

port=$(shuf -i 6000-9999 -n 1)
kbport=$(expr $port + 1)

/usr/bin/ssh -N -f -R $port:localhost:$port log-0
/usr/bin/ssh -N -f -R $port:localhost:$port log-1
/usr/bin/ssh -N -f -R $kbport:localhost:$kbport log-0
/usr/bin/ssh -N -f -R $kbport:localhost:$kbport log-1

unset XDG_RUNTIME_DIR
if [ "$SLURM_JOBTMP" != "" ]; then
    export XDG_RUNTIME_DIR=$SLURM_JOBTMP
fi

# TODO: Update this path to point to your directory
TOP_ES_PATH=/home/clb617/scratch/thirdparty/elasticsearch

# You can leave these alone
ES_PATH=$TOP_ES_PATH/elasticsearch-current/
KB_PATH=$TOP_ES_PATH/kibana-current/

# Print port info to your slurm log
echo "ES Running on:" $(hostname)
echo "ElasticSearch at:" $port
echo "Kibanna at:" $kbport

# Start ElasticSearch in daemon mode
$ES_PATH/bin/elasticsearch -d -Ecluster.name=json_search_cluster -Enode.name=node_1 -Enetwork.host=_local_ -Ehttp.port=$port

# Spin up kibana, pointing to your ES installation
$KB_PATH/bin/kibana --elasticsearch http://localhost:$port --port $kbport


