import boto3
from datetime import datetime, timedelta
from botocore.exceptions import ClientError

REGION = "ap-south-1"
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:036950456823:CostOptimizerAlerts"

ec2 = boto3.client('ec2', region_name=REGION)
cloudwatch = boto3.client('cloudwatch', region_name=REGION)
sns = boto3.client('sns', region_name=REGION)

def lambda_handler(event, context):
    message = ""

    try:
        # -------- EC2 CHECK --------
        response = ec2.describe_instances()

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']

                if state == 'running':
                    metrics = cloudwatch.get_metric_statistics(
                        Namespace='AWS/EC2',
                        MetricName='CPUUtilization',
                        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                        StartTime=datetime.utcnow() - timedelta(days=7),
                        EndTime=datetime.utcnow(),
                        Period=86400,
                        Statistics=['Average']
                    )

                    if metrics['Datapoints']:
                        avg_cpu = sum(
                            dp['Average'] for dp in metrics['Datapoints']
                        ) / len(metrics['Datapoints'])

                        if avg_cpu < 10:
                            message += (
                                f"⚠️ EC2 Instance {instance_id} "
                                f"has low CPU usage ({avg_cpu:.2f}%). "
                                "Consider stopping it.\n"
                            )

        # -------- UNATTACHED EBS CHECK --------
        volumes = ec2.describe_volumes(
            Filters=[{'Name': 'status', 'Values': ['available']}]
        )

        for vol in volumes['Volumes']:
            message += f"⚠️ Unattached EBS Volume detected: {vol['VolumeId']}\n"

        # -------- SEND SNS ALERT --------
        if message:
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="AWS Cost Optimization Alert",
                Message=message
            )

        return {
            'statusCode': 200,
            'body': 'Cost optimization check completed successfully'
        }

    except ClientError as e:
        print("ERROR:", e)
        raise e
