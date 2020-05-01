import boto3
import json
import time
from inspect import getmembers
from optparse import OptionParser
import sys

def delete_secret():
    region=input("Enter the region of your secrets: ")
    client = boto3.client('secretsmanager',region_name=region)
    my_list=list()
    paginator = client.get_paginator('list_secrets')
    for secrets in paginator.paginate(MaxResults=100):
        for secret_arn in secrets['SecretList']:
            a=my_list.append(secret_arn['ARN'])
    print("Listing all your Secrets from",region,"region")
    time.sleep(2)
    index=1
    if my_list==[]:
        print("No Secret Found")
        sys.exit()
    else:
        for i in my_list:
            print(index,i)
            index +=1
        start_delete(my_list)

def start_delete(my_list):
    x=input("Please note the script will delete all your secret permanenetly and this is an irreverisble operation,type confirm to proceed. ")
    if x == "confirm" or x == "Confirm":
        for i in my_list:
            print("Deleting.....")
            response = client.delete_secret(SecretId=i,ForceDeleteWithoutRecovery=True)
        print("All Secrets are successfully Deleted")
    else:
        print("Invalid Input.Exiting..")
        sys.exit()

delete_secret()
