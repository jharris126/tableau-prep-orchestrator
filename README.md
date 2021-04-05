# tableau-prep-orchestrator

## Summary

Tableau Prep Orchestrator is an open-source alternative to Tableau Prep Conductor that combines [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/) and Tableau's [Metadata](https://help.tableau.com/current/api/metadata_api/en-us/index.html) and [REST](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm) APIs to create a standalone server for scheduling, running, and managing dependencies around [Tableau Prep](https://www.tableau.com/products/prep) Flows published to [Tableau Server](https://www.tableau.com/products/server). After filling out a short .yml file with your Tableau Server login info and spinning up this [Docker](https://www.docker.com/) container (setup instructions below), your Prep Flows are automatically profiled and an Airflow DAG is generated with all dependencies and order of operations handled for you. Any changes made are automatically added at a configurable interval (every 5 min by default) and will integrate into your existing DAG with no manual intervention required.

## Setup

### Setup Docker

- install docker and docker compose

### Clone the GitHub Project

- clone the repo
- build with build command

### Build & Deploy with Docker

- compose with compose command

- <code>docker build -t airflow .</code>
- <code>docker-compose -f docker-compose-LocalExecutor.yml up -d</code>

### Check It Out

- localhost:8080
- screenshots

## Cusomizations

- edit each DAG to change timezone, scheduled execution times, and failure handling
- edit airflow config and dockerfiles to customize the implementations of airflow (needed for enterprise grade)
- add new DAG files (.py files in the DAG folder) or alter current ones to add any other workflows to run in tandem to Prep Flows

## Productionize
- security
- docker-compose to docker swarm

## Acknowledgments

The Apache Airflow portion of this project is based on:
https://github.com/puckel/docker-airflow
