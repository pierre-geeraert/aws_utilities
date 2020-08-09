import boto3
import json
import pprint

Number_of_instances=0

ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        Number_of_instances=Number_of_instances+1
        print("=======================================================")
        print("Instance number "+str(Number_of_instances))
        print("=======================================================")
        # This sample print will output entire Dictionary object
        #pprint.pprint(instance)
        # This will print will output the value of the Dictionary key 'InstanceId'
        print("Instance ID: "+str(instance["InstanceId"]))
        print("Instance Name: "+str(instance["Tags"]))

