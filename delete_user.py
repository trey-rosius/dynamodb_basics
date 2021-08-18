from decimal import Decimal
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def delete_user(username, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    user= dynamodb.Table('Users')

    try:
        response = table.delete_item(
            Key={
                'username': username,
              
            },
        
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
       
    else:
        return response


if __name__ == '__main__':
    
    delete_response = delete_user("Rosius Ndimofor")
    if delete_response:
        print("User deleted successfully:")
        pprint(delete_response, sort_dicts=False)