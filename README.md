# GFG 

This simple Docker container:
 * sets up a local Pyspark environment (configuring it to access aws)
 * does some transformations
 * saves the results on an s3 bucket in parquet format

## Build the container

```
docker build -t gfg .
```

## Run the container

```
docker run -e AWS_ACCESS_KEY_ID=<PROVIDED ACCESS KEY> -e AWS_SECRET_ACCESS_KEY=<PROVIDED SECRET ACCESS KEY>  -d gfg:latest
```

Due to the fact that s3 only has only eventual consistency I chose to save the processed files locally first to avoid data loss when spark creates temporary files during the write process. Also instead of creating an upload method with boto3 I have preferred to use the aws cli since it's definitely more optimized.