from pprint import pprint
import boto3


def put_user(username, occupation, age, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Users')
    response = table.put_item(
       Item={
            'username': username,
           
            'info': {
                'occupation': occupation,
                'age': age
            }
        }
    )
    return response


if __name__ == '__main__':
    user_resp = put_user("Rosius Ndimofor",
                           "Programmer", 33)
    print("Put user succeeded:")
    pprint(user_resp, sort_dicts=False)