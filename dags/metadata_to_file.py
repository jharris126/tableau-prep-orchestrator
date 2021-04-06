from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
import logging
import pendulum
import json
import yaml
import tableauserverclient as TSC


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 9, 1, tzinfo=pendulum.timezone('America/Los_Angeles')),
    'email': [],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
    }

dag = DAG('metadata_to_file', default_args=default_args, catchup=False, schedule_interval='*/5 * * * *')

def get_metadata():
    flows_query = '''{
    flows {
        id
        luid
        name
        downstreamFlows {
        name
        }
    }
    }'''

    with open('tableau-config.yml', 'r') as stream:
        tableau_info = yaml.safe_load(stream)

    tableau_auth = TSC.TableauAuth(tableau_info['tableau-username'], tableau_info['tableau-password'], site_id=tableau_info['tableau-site'])
    server = TSC.Server(tableau_info['tableau-base-url'], use_server_version=True)

    with server.auth.sign_in(tableau_auth):
        data = server.metadata.query(flows_query)['data']

        out_file = open("flows.json", "w")
        json.dump(data, out_file, indent=4)

    path = os.path.dirname(os.path.realpath(__file__)) + '/'
    name = 'orchestrate_prep_flows'
    for files in os.walk(path):
        for subfiles in files:
            for f in subfiles:
                if f == name + '.txt':
                    os.rename(path + name + '.txt', path + name + '.py')
                    logging.info(name + '.txt renamed to ' + name + '.py')

t = PythonOperator(task_id="metadata_to_json", python_callable=get_metadata, dag=dag)