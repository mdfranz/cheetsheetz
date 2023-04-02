#!/bin/sh

if ! type aws > /dev/null; then 
	echo "AWS CLI is not installed"; exit
fi

if ! type jq > /dev/null; then
	echo "jq not installed"; exit
fi

REGION=$1

CLUSTERARN=`aws --region $REGION kafka list-clusters  | jq -r .ClusterInfoList[0].ClusterArn`
ZKSTRING=`aws --region $REGION kafka list-clusters  | jq -r .ClusterInfoList[0].ZookeeperConnectString`

echo ARN: $CLUSTERARN
echo ZKSTRING: $ZKSTRING
