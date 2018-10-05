# ElasticSearch+Kibana on HPC Infrastructure

Repository of scripts for spinning up a personal instance of ElasticSearch and Kibana on HPC infrastructure (i.e., on Slurm)

## Setup Workflow

1. Download ElasticSearch and Kibana and decompress
1. Create simlinks to support upgrades
1. Update `run-es.sbatch` to correct path
1. Run `run-es.sbatch` to start ElasticSearch and Kibana. 
	- See slurm.log for port forwarding
1. Create your index with mappings for tweet metadata
1. Push tweet data to ElasticSearch
1. Access Kibana and set up your index pattern
1. Happy searching
