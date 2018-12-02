import boto3
import os

session = boto3.Session(profile_name='imtakingmarta')
dynamodb = session.resource('dynamodb')
if 'USER_TABLE_NAME' in os.environ:
    table_name = os.environ['USER_TABLE_NAME']
    table = dynamodb.Table(table_name)
else:
    print "Service initialized without USER_TABLE_NAME environment variable, only expected in unit tests."


def get_user(user_id):
    response = table.get_item(TableName=table_name,
                              Key={'userId': user_id}
                              )

    if response is None or 'Item' not in response:
        return None
    else:
        return response['Item']


def save_user(user):
    table.put_item(TableName=table_name,
                   Item=user)
