import boto3

# Specify your credentials
ecr_client = boto3.client(
    'ecr',
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name=''  
)

repository_name = "hlombe-monitoring-app"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)
