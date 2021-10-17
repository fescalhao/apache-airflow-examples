from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from airflow.utils.task_group import TaskGroup

from subdags.subdag_parallel_dag import subdag_parallel_dag

default_args = {
    'start_date': datetime(2021, 10, 13)
}

with DAG(dag_id='parallel_dag', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:

    task_1 = BashOperator(
        task_id = 'task_1',
        bash_command = 'sleep 3'
    )

    with TaskGroup('processing_tasks') as processing_tasks:
        task_2 = BashOperator(
            task_id = 'task_2',
            bash_command = 'sleep 3'
        )

        task_3 = BashOperator(
            task_id = 'task_3',
            bash_command = 'sleep 3'
        )

    # Not recommended!!!!
    # processing = SubDagOperator(
    #     task_id = 'processing_task',
    #     subdag = subdag_parallel_dag('parallel_dag', 'processing_task', default_args)
    # )    

    task_4 = BashOperator(
        task_id = 'task_4',
        bash_command = 'sleep 3'
    )

task_1 >> processing_tasks >> task_4