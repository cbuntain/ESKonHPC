# ElasticSearch+Kibana on HPC Infrastructure

Repository of scripts for spinning up a personal instance of ElasticSearch and Kibana on HPC infrastructure (i.e., on Slurm)

## Setup Workflow

1. Download ElasticSearch and Kibana and decompress and create simlinks to support upgrades
	- Run `bash download.sh`
1. Update `run-es.sbatch` to correct path
1. Run `run-es.sbatch` to start ElasticSearch and Kibana. 
	- See slurm.log for port forwarding
1. Create your index with mappings for tweet metadata
	- `python createIndex.py http://localhost:<ESPORT> <index_name>`
1. Push tweet data to ElasticSearch
	- `python postTwitter.py http://localhost:<ESPORT> <index_name> <tweet_path.json`
1. Access Kibana and set up your index pattern
	- Create SSH tunnel to HPC, and visit http://localhost:<KPORT> and go to _Manage_
1. Happy searching
