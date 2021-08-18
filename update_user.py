from decimal import Decimal
from pprint import pprint
import boto3


def update_user(username, occupation, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Users')

    response = table.update_item(
        Key={
            'username': username,
           
        },
        UpdateExpression="set info.occupation=:o",
        ExpressionAttributeValues={
           
            ':o': occupation
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_user(
        "Rosius Ndimofor", "barber")
    print("Update user succeeded:")
    pprint(update_response, sort_dicts=False)