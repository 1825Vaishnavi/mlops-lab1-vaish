from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator  # ← ADD THIS
from airflow.utils.dates import days_ago
from datetime import timedelta
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

default_args = {
    'owner': 'Vaishnavi',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
    'email': ['YOUR_EMAIL@gmail.com'],  # ← ADD YOUR EMAIL
    'email_on_failure': True,            # ← ADD THIS
    'email_on_retry': False,             # ← ADD THIS
}

dag = DAG(
    'Airflow_Lab2_Modified',
    default_args=default_args,
    description='Modified ML Pipeline using Iris Dataset',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False
)

def load_data():
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    df.to_csv('/tmp/iris.csv', index=False)

def build_model():
    df = pd.read_csv('/tmp/iris.csv')
    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print("Model Accuracy:", accuracy)

    joblib.dump(model, '/tmp/model.pkl')

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag
)

build_task = PythonOperator(
    task_id='build_model',
    python_callable=build_model,
    dag=dag
)

# ← ADD THIS EMAIL TASK
send_success_email = EmailOperator(
    task_id='send_success_email',
    to='vaishnavigajrala@gmail.com',
    subject='✅ Airflow Lab2 - SUCCESS',
    html_content='<h3>Pipeline Successful! 🎉</h3>',
    dag=dag
)

# ← UPDATE THIS LINE
load_task >> build_task >> send_success_email