#!/bin/bash

# create virtual env
python -m venv env

# activate virtual env
source env/bin/activate

# upgrade pip and install libraries/modules specified in requirements.txt
pip install --upgrade pip

pip install -r requirements.txt

# build image and run container for text classifier
docker-compose up --build