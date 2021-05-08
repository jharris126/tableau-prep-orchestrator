# tableau-prep-orchestrator

## Summary

Tableau Prep Orchestrator is an opinionated docker deployment of [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/) that has been preconfigured to work with Tableau Server/Online and acts as an open-source alternative to Tableau Prep Conductor. It combines Airflow with Tableau's [Metadata](https://help.tableau.com/current/api/metadata_api/en-us/index.html) and [REST](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm) APIs to create a standalone server for scheduling, running, and managing dependencies around [Tableau Prep](https://www.tableau.com/products/prep) Flows published to [Tableau Server](https://www.tableau.com/products/server). After filling out a short .yml file with your Tableau Server login info and spinning up this [Docker](https://www.docker.com/) container (setup instructions below), your Prep Flows are automatically profiled and an Airflow DAG is generated with all dependencies and order of operations handled for you. Any changes made are automatically added at a configurable interval (every 5 min by default) and will integrate into your existing DAG with no manual intervention required.

## Setup

### Setup Docker

Before you can use Tableau Prep Orchestrator, you will need to install Docker.

- Install Docker
  - <https://docs.docker.com/get-docker/>

### Clone the GitHub Project

- Clone this repo onto your local machine
- Fill out tableau-config.yml file with your Tableau Server/Online connection info. If you only want to orchestrate Tableau Prep Flows in certain projects, fill out the *projects-to-refresh-from* section with a list of projects. Otherwise, leave empty and all Flows on the site will be pulled in for orchestration.

```yaml
--- # Tableau Server API Info
  tableau-base-url: "https://10ax.online.tableau.com"
  tableau-site: "my-tableau-site"
  tableau-username: "email@example.com"
  tableau-password: "super-secret-password"
  # leave blank to gather flows from all projects
  projects-to-refresh-from:
    - "default"
```

### Build & Deploy with Docker

Open terminal or cmd and navigate to the directory where you cloned the GitHub Repo then run the commands below that correspond to the setup you would like.

- Build your docker image
  - `docker build -t airflow . --no-cache`

- Run with docker run (Sequential Executor)
  - `docker run -d -p 8080:8080 airflow tableau-prep-orchestrator`

- run with docker-compose (Local Executor)
  - `docker compose -f docker-compose-LocalExecutor.yml up -d`

### Check It Out

Open a browser window and navigate to <localhost:8080> to start using Tableau Prep Orchestrator

Turn first dag on

![Home Screen](./screenshots/home.png)

Second DAG should show up, turn that on

Watch it run

![Prep Flows as Airflow DAG](./screenshots/orchestrate_prep_flows.png)

## Customizations

- edit each DAG to change timezone, scheduled execution times, and failure handling
- edit airflow config and dockerfiles to customize the implementations of airflow (needed for enterprise grade)
- add new DAG files (.py files in the DAG folder) or alter current ones to add any other workflows to run in tandem to Prep Flows

## Productionize
- By default, Tableau Prep Orchestrator does not use authenticaion. To run in production, you would want to modify the airflow.cfg file to enable your desired authentication method.
- docker compose on a single machine is great for Development and Test environments where containers can be quickly spun up and linked. However, to make better use of the horizontal scalability and fault tolerance of Airflow and Docker, deploy with Docker Swarm or Kubernetes.

## Acknowledgments

The Apache Airflow portion of this project is based on:
<https://github.com/puckel/docker-airflow>
