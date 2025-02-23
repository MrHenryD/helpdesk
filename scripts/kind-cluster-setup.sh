#!/bin/bash

VERSION=1.21.1
NAMESPACE=helpdesk

# Create a cluster with the specified version
kind create cluster --image kindest/node:v$VERSION
kubectl cluster-info --context kind-kind
kubectl config use-context kind-kind

# Create namespace
kubectl apply -f kubernetes/namespace.yml
kubectl config set-context --current --namespace=$NAMESPACE

# Build and load the docker assets
docker build -f docker/Dockerfile -t helpdesk:1.0.0 .
kind load docker-image helpdesk:1.0.0

# Setup non-helm resources
kubectl apply -f kubernetes/volumes.yml
kubectl apply -f kubernetes/secrets.yml
kubectl apply -f kubernetes/database.yml
kubectl apply -f kubernetes/migrate.yml

# Install helm chart
helm install helpdesk ./helm
