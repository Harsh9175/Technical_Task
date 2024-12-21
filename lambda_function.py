rds = boto3.client('rds-data')
glue = boto3.client('glue')

def lambda_handler(event, context):
    # Logic to read from S3 and write to RDS or Glue
    # This is a simple example that reads from S3 and writes to Glue
    bucket_name = os.environ['S3_BUCKET']
    file_key = event['file_key']

    # Reading data from S3
    file_content = s3.get_object(Bucket=bucket_name, Key=file_key)['Body'].read().decode('utf-8')

    # Check if RDS is available, else write to Glue
    try:
        # Write to RDS (simplified for example)
        rds.execute_statement(
            database='data_db',
            resourceArn=os.environ['RDS_ARN'],
            secretArn=os.environ['RDS_SECRET_ARN'],
            sql="INSERT INTO my_table (data) VALUES (:data)",
            parameters=[{'name': 'data', 'value': {'stringValue': file_content}}]
        )
    except Exception as e:
        print(f"RDS write failed: {e}")
        # If RDS fails, write to Glue (simplified)
        glue.create_table(
            DatabaseName='my_database',
            TableInput={
                'Name': 'my_table',
                'Columns': [{'Name': 'data', 'Type': 'string'}],
                'PartitionKeys': [],
                'StorageDescriptor': {'Columns': [{'Name': 'data', 'Type': 'string'}]},
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully')
    }
