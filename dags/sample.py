from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime
from pendulum import timezone

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1, tzinfo=timezone('Asia/Seoul')),
}

with DAG(
    default_args=default_args,
    dag_id='DAG_FOR_TEST',
    schedule=None,
) as dag:
    start = EmptyOperator(
        task_id='start'
    )
    end = EmptyOperator(
        task_id='end'
    )

    start >> end