import boto3
client = boto3.client('ec2')

ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
"""
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # This sample print will output entire Dictionary object
        #print(instance)
        print("hello")
        # This will print will output the value of the Dictionary key 'InstanceId'
        #print(instance["InstanceId"])
"""


response = client.create_image(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdh',
            'Ebs': {
                'VolumeSize': '100',
            },
        },
        {
            'DeviceName': '/dev/sdc',
            'VirtualName': 'ephemeral1',
        },
    ],
    Description='An AMI for my server',
    InstanceId='i-1234567890abcdef0',
    Name='My server',
    NoReboot=True,
)

print(response)