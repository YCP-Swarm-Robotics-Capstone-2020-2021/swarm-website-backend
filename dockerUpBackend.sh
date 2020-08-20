#!/bin/bash

#make network if not already made
docker network create --driver=bridge --subnet=192.168.10.0/25 --gateway 192.168.10.1 swarm-net

#create the network bridge
sh createNetwork.sh

#build postgres container
cd swarmpostgres
sh dockerUpDb.sh

#build django container
cd ../swarmdjango
docker-compose run  --rm web django-admin startproject swarm_backend .
docker-compose up -d
