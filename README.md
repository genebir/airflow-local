
<h1>Airflow</h1>

<h3>환경구성</h3>

> ubuntu:22.04
> airflow:2.7.0
> postgresql:14
> python:3.10


***

<h3>1. WSL에 Airflow 설치</h3>

```bash
export AIRFLOW_HOME=~/airflow

AIRFLOW_VERSION=2.7.0

PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

airflow version
```

***

<h3>2. Meta DB 연결</h3>

```bash
vi airflow.cfg

[database]
..
sql_alchemy_conn = postgresql+psycopg2://<username>:<password>@localhost:5432/airflow_db
..
```

```bash
airflow db init
```

***

<h3>3. Executor 설정</h3>

```bash
vi airflow.cfg

[core]
..
executor = LocalExecutor
..
```


