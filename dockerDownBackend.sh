#!/bin/bash
docker rm -f swarmpostgres
docker rmi swarmpostgres:latest
rm -rf data/*


# Removes container(s) created by buildContainers script
docker ps --filter name=django_web -aq | xargs docker stop | xargs docker rm

#remove network
docker network rm swarm-net
