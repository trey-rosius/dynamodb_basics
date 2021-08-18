from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_user(username, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Users')

    try:
        response = table.get_item(Key={'username': username})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    user= get_user("Rosius Ndimofor")
    if user:
        print("Get user succeeded:")
        pprint(user,sort_dicts=False)