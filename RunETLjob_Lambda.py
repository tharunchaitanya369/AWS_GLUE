import json
import boto3
client=boto3.client("glue")
def lambda_handler(event, context):
    # TODO implement
    response=client.start_job_run(
          JobName='s3jsonparquet'
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
