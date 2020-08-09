import boto3
import json
import pprint

ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        pprint.pprint(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        print(instance["InstanceId"])


