import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job


args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource = glueContext.create_dynamic_frame.from_catalog(database = "post", table_name = "s3csvjson", transformation_ctx = "datasource")

datasink = glueContext.write_dynamic_frame.from_options(frame = datasource, connection_type = "s3", 
connection_options = {"path": "s3://projects3glue/csv/"}, format = "parquet", transformation_ctx = "datasink")
job.commit()