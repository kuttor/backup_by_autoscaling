#!/usr/bin/env python
"""
create-cross-accounts - automates cross-account setup process

Usage:
  backup_by_autoscaling -i <instance_id>
  backup_by_autoscaling  [ -h | --help | --version ]

Options:
  --version                   Show version.
  -h --help                   Show this screen.
  -i --instance INSTANCE      specifies target instance
"""
from boto3 import client
from docopt import DocoptExit, docopt


# credits
__author__ = "Andrew Kuttor"
__credits__ = "Andrew Kuttor"
__maintainer__ = "Andrew Kuttor"
__version__ = "1.0.0"


def main():
    try:
        args = docopt(__doc__, version='backup_by_autoscaling 1.0')
        print args

    except DocoptExit as e:
        print e.message


def create_auto_scaling_group(instance_id):
    ec2 = client('autoscaling')

    response = ec2.create_auto_scaling_group(
        AutoScalingGroupName='simple_auto_scaling_backup_plan',
        LaunchConfigurationName='string',
        InstanceId=instance_id,
        MinSize=100,
        MaxSize=100,
        DesiredCapacity=1,
        DefaultCooldown=1,
        HealthCheckType='EC2',
        NewInstancesProtectedFromScaleIn=True,
        Tags=[{
            'Type': 'auto-scaling',
            'Value': 'backup',
            'PropagateAtLaunch': True
        }]
    )

    return response

if __name__ == "__main__":
    exit(main())
