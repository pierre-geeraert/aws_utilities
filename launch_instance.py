import boto3
client = boto3.client('ec2')


response = client.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdh',
            'Ebs': {
                'VolumeSize': 100,
            },
        },
    ],
    ImageId='ami-07d9160fa81ccffb5',
    InstanceType='t2.micro',
    KeyName='Debian_buster_kp',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'sg-0be7eaf90b053653b',
    ],
    SubnetId='subnet-06592162726fc29ed',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Purpose',
                    'Value': 'test',
                },
            ],
        },
    ],
)

print(response)
