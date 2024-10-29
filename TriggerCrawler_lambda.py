import json
import boto3
client=boto3.client("glue")
def lambda_handler(event, context):
    # TODO implement
    response=client.start_crawler(
        Name="crawls3json")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
