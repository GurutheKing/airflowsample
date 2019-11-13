from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
# default arguments contains the owner info, email details etc...
default_args = {
    'owner':'guru',
    'depends_on_past': False,
    'start_date': datetime(2018, 10, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
    'provide_context': True,
}
#define a DAG
# give a name and id
dag = DAG(
    'firsttest_1', default_args=default_args, schedule_interval=timedelta(days=1))
#create first task
stage1 = BashOperator(
    task_id='Hellocdags',
    bash_command='echo hello',
    dag=dag)
#Create second task, task id  is stage2
stage2 = BashOperator(
    task_id='Worldcdags',
    bash_command='echo world',
    dag=dag)
#marking the dependency
stage1 >> stage2
#opposite stage2 << stage1
#stage2.set_downstream(stage1)