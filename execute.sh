python -u gfg.py
aws s3 sync /tmp/parquet-data/ s3://gfg.challenge.dwh.valerio/ --exclude '.*'
echo 'Uploaded'