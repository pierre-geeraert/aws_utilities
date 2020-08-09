import pprint
from datetime import datetime

import boto3
client = boto3.client('ec2')


response = client.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdh',
            'Ebs': {
                'VolumeSize': 20,
            },
        },
    ],
    ImageId='ami-07d9160fa81ccffb5',
    InstanceType='t3a.nano',
    KeyName='Debian_buster_kp',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'sg-08ee4c5336b8dcba4',
    ],
    SubnetId='subnet-0ec7bfc49d905e146',
    UserData=open("/home/pi-ux-ce/git/aws_infrastructure/userdata.sh").read(),
    InstanceInitiatedShutdownBehavior='terminate',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'test',
                },
{
                    'Key': 'development',
                    'Value': 'true',
                },
            ],
        },
    ],
)

pprint.pprint(response)
