import config as config
import boto3


def addToDynamodb(table, list):
    try:
        session = boto3.Session(
            aws_access_key_id=config.AWS_SERVER_PUBLIC_KEY,
            aws_secret_access_key=config.AWS_SERVER_SECRET_KEY,
            region_name=config.AWS_REGION
        )

        dynamodb = session.resource('dynamodb')

        table = dynamodb.Table('Games')
        response = table.put_item(
            Item={
                "Date": "Current",
                "NintendoList": nintendo_list,
                "SteamList": steam_list
            }
        )

        return response

    except RuntimeError:
        return ("ERROR: add to DynamoDB")