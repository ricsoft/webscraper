import config as config
import boto3
import pytz
from datetime import datetime

def addToDynamodb(breweryList):
    dbName = 'dynamodb'
    tableName = 'Webscraper'
    primaryPartition = 'Breweries'

    pst = pytz.timezone('America/Los_Angeles')
    fmt = '%b %d, %Y'
    currentDate = datetime.now(pst).strftime(fmt)

    try:
        session = boto3.Session(
            aws_access_key_id=config.AWS_SERVER_PUBLIC_KEY,
            aws_secret_access_key=config.AWS_SERVER_SECRET_KEY,
            region_name=config.AWS_REGION
        )

        dynamodb = session.resource(dbName)

        table = dynamodb.Table(tableName)

        response = table.put_item(
            Item={
                'id': primaryPartition,
                'date': currentDate,
                'data': breweryList
            }
        )

        return response

    except:
        return ('ERROR: add to DynamoDB')
