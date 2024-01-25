#!/bin/bash
# Script Created by Kenneth Sibayan
# Cloud Infra Delivery - Makati
#
# NOTE:
# MUST login to az cli on the corresponding account/service account first.
#
# $1 = CSV

clientid="d26bf6c6-0dd3-4291-8d82-86ff18044322"
secret="U0E8Q~EhDDUEBQBvLpZc_YCcX6KLgGHY~H24Qb2Q"
tenantid="abf9f4cd-56cd-4d8a-9a02-7c288b91d9a5"

az login --service-principal -u $clientid -p $secret -t $tenantid --output none
echo "Logged in using $clientid"

PIFS=$IFS
IFS=','
echo "Reading list of users in $1 file "
while read -r user
do
        echo "deleting $user...."
        az ad user show --id $user@deltekcloud.net
        echo "...Done"
done < $1
IFS=$PIFS