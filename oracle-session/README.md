# Oracle DB Session Monitoring

## Setup Environment

```shell
export ORACLE_DB_USER=
export ORACLE_DB_PASSWORD=
export ORACLE_DB_DSN=

export ELASTIC_CLOUD_ID=
export ELASTIC_USERNAME=
export ELASTIC_PASSWORD=
```

## Run

```shell
make
```

```shell
nohup make oracle-session > /dev/null 2>&1 &
```
