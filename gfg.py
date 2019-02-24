import pyspark
from pyspark.sql.functions import to_date
import os
import sys


AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
LOCAL_TEMP = '/tmp/parquet-data/'
BUCKET = 'gfg.challenge.dwh.data'

spark = pyspark.sql.SparkSession.builder \
            .master("local[*]") \
            .appName("Spark GFG") \
            .config("spark.executor.extraJavaOptions", "-Dcom.amazonaws.services.s3.enableV4=true") \
            .getOrCreate()

# Set the property for the driver. Doesn't work using the same syntax
# as the executor because the jvm has already been created.
spark.sparkContext.setSystemProperty("com.amazonaws.services.s3.enableV4", "true")
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3.eu-central-1.amazonaws.com")
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", AWS_ACCESS_KEY_ID)
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", AWS_SECRET_ACCESS_KEY)

sys.stdout.write('Data processing starting\n')

df = spark.read.csv('s3a://' + BUCKET + '/*', header=False, inferSchema=True, sep='|')
df.dropDuplicates(subset=['_c0', '_c6', '_c7']) \
  .withColumn('_c5', to_date(df._c5, 'yyyy-MM-dd')) \
  .withColumn('_c6', to_date(df._c6, 'yyyy-MM-dd')) \
  .write.mode('overwrite').parquet(LOCAL_TEMP)

sys.stdout.write('Data processing done, uploading...\n')
