import boto3
import pprint

ec2client = boto3.client('ec2')




def ask_decision(instance_id,instance_tag):
    print("Do you want to keep this instance ?")
    print(instance_id)
    print(instance_tag)
    decision = input(" Y/N ")
    if decision == 'N' or decision == 'n':
        delete_instance(instance_id)
    if decision == 'y' or decision == 'y':
        print("Fine")
    else:
        print("Fine")

def delete_instance(instance_id):
    pprint.pprint(ec2client.terminate_instances(InstanceIds=[instance_id]))

def main():
    response = ec2client.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # This sample print will output entire Dictionary object
            # pprint.pprint(instance)
            # This will print will output the value of the Dictionary key 'InstanceId'
            ask_decision(instance["InstanceId"],instance["Tags"])

    return 0

if __name__ == "__main__":
    main()

