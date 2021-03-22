#!/bin/bash
# deactivate virtual env 
echo "deactivating virtual env..."
deactivate
echo "deactivated virtual env."
# stop / remove container/images/networks
echo "stopping containers..."
echo "removing containers..."
echo "removing images..."
docker-compose down --rmi all
docker rmi tensorflow/serving
echo "stopped containers."
echo "removed containers."
echo "removed images."
