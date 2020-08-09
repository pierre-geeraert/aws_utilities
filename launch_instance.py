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
    UserData='#!/bin/bash'
             'sudo yum update -y amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2'
             'sudo yum install -y httpd mariadb-server'
             'sudo systemctl start httpd'
             'sudo systemctl enable httpd'
             'sudo usermod -a -G apache ec2-user'
             'sudo chown -R ec2-user:apache /var/www'
             'sudo chmod 2775 /var/www'
             'sudo find /var/www -type d -exec chmod 2775 {} \;'
             'sudo find /var/www -type f -exec chmod 0664 {} \;'
             'sudo echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php',
    InstanceInitiatedShutdownBehavior='terminate',
    InstanceMarketOptions={
            'MarketType': 'spot',
            'SpotOptions': {
                'MaxPrice': '0.003',
                'SpotInstanceType': 'one-time',
                'BlockDurationMinutes': 60,
                'InstanceInterruptionBehavior': 'terminate'
            }
    },
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
