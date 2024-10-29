 # **AWS_GLUE**
 I have created an ETL process that triggers a Lambda function when a JSON object is uploaded to an S3 bucket. Once the crawler completes successfully, a CloudWatch rule triggers another Lambda function to start the Glue ETL job. When the Glue job succeeds, it uploads a Parquet file to S3. Upon successful completion of the Glue job, another CloudWatch rule triggers an SNS topic, which sends a notification email.

 This is the architecture of the AWS Glue Job
 
 ![Workflow of the Glue Job](Architecture)

 ## **Workflow:**

  ### S3 Upload (Triggering Lambda)
  - A JSON file is uploaded to an S3 bucket.
  - This upload triggers Lambda Function 1, which initiates further processes.
   [Lambda Function 1](TriggerCrawler_lambda.py)

  ### AWS Glue Crawler
  - The Glue crawler scans the uploaded data and updates the Glue Data Catalog.
  -  When the crawler completes successfully, a CloudWatch Rule triggers Lambda Function 2. [Lambda Function 2](RunETLjob_Lambda.py)

  ### Cloudwatch Rule
  - We Will create a cloudwatch glue Crawler state change rule this will trigger lambda function 2 [cloudwatch Rule for triggering Lambda Function 2](cloudwatch_trigger_etl_lambda.txt)

  ### AWS Glue ETL Job
  - Lambda Function 2 starts the Glue ETL job.
  - The ETL job processes the data and uploads the transformed output as a Parquet file back to the S3 bucket.
  -  This is the glue ETL code [Glue ETL](ETLjobe_Glue.py)

  ### Notification via SNS
  - Upon the successful completion of the Glue job, another CloudWatch Rule triggers an SNS Topic [cloudwatch Rule for Glue job state change](cloudwatch_etlstatechange.txt)
  - The SNS topic sends a notification email confirming the job's success.

  ### Key AWS Services Used:

  - AWS Lambda: To trigger events and execute custom code.
  - Amazon S3: For data storage and triggers.
  - AWS Glue: For data cataloging and transformation jobs.
  - Amazon CloudWatch: To monitor job status and trigger events.
  - Amazon SNS: To send email notifications on job completion.

Setup Instructions:

 1. Upload JSON files to the designated S3 bucket to initiate the process.
 2. Ensure that the Glue crawler and ETL jobs are properly configured and associated with the correct Lambda functions.
 3. Monitor the process through CloudWatch logs and metrics.
 4. Receive email notifications for job completion through SNS.
