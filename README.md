***
<h1>Airflow</h1>

***
>MWAA 환경에서의 개발과 별개로 로컬에서 Airflow를 사용하기 위한 인프라 구성
> 
> 개발에 대한 깊은 이해도를 위해 인프라부터 구성해보기로 한다.


<h3>환경구성</h3>
> ubuntu:22.04
> 
> airflow:2.7.0
> 
> postgresql:14


***

<h3>1. WSL에 Airflow 설치</h3>
```bash
export AIRFLOW_HOME=~/airflow # airflow home 설정

AIRFLOW_VERSION=2.7.0
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# airflow 버전 확인
airflow version
```

