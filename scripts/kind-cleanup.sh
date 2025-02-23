#!/bin/bash
NAMESPACE=helpdesk

kubectl delete all -n $NAMESPACE --all
helm uninstall helpdesk
