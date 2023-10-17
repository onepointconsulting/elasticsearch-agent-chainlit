# Simple UI for the ElasticSearch Agent

Provides a simple UI for the ElasticSearch LangChain Agent which you can find in this project:
https://github.com/onepointconsulting/elasticsearch-agent

## Setup

We suggest to use [Conda](https://docs.conda.io/en/latest/) to manage the virtual environment and then install poetry.

```
conda activate base
conda remove -n elastic_search_chainlit --all
conda create -n elastic_search_chainlit python=3.11
conda activate elastic_search_chainlit
pip install poetry
```

## Installation

```
poetry install
poetry add --editable ..\elasticsearch_playground\dist\elasticsearch_agent-0.1.8-py3-none-any.whl
```

Please note that this project relies on this project:

https://github.com/onepointconsulting/elasticsearch-agent

In order to build the `elasticsearch_agent-0.1.5-py3-none-any.whl` you will need to build it first using the instructions in 
https://github.com/onepointconsulting/elasticsearch-agent.

## Execution

```
chainlit.exe run .\elasticsearch_chainlit\ui\agent_chainlit.py
```

## Configuration

```
OPENAI_API_KEY=...
OPENAI_MODEL=gpt-4-0613
# OPENAI_MODEL=gpt-3.5-turbo-16k-0613
REQUEST_TIMEOUT=300
LANGCHAIN_CACHE=false
CHATGPT_STREAMING=false
LLM_VERBOSE=true

# Elastic Search related
ELASTIC_SERVER=https://127.0.0.1:9200
ELASTIC_USER=elastic
ELASTIC_PASSWORD=...
ELASTIC_VERIFY_CERTIFICATES=false

ELASTIC_INDEX_DATA_FROM=0
ELASTIC_INDEX_DATA_SIZE=5
ELASTIC_INDEX_DATA_MAX_SIZE=50

LANGCHAIN_VERBOSE=true
AGGS_LIMIT=200
TOKEN_LIMIT=6000
MAX_SEARCH_RETRIES = 100
QUESTIONS_TO_KEEP=5
```