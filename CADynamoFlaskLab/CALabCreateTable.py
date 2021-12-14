import logging
import boto3
from botocore.exceptions import ClientError
import csv
from pathlib import Path
from pprint import pprint
from boto3.dynamodb.types import TypeSerializer
import time
import random

path = Path(__file__).parent / "dynamodb_upload.csv"

class DynamoDBLab:

    #   generate a randomw ID to be used in the DynamDB for each account
    def generate_row_id(self):
        CUSTOMRANDOMENUMBER = 1300000000000
        ts = int(str(time.time()).replace('.', '')) - CUSTOMRANDOMENUMBER
        randomid = random.randint(0,10)
        return (ts*512)+randomid
        
        
    #   Create the DynamoDB table as referenced by table_name and other variables passed in
    def create_lab_table(self, table_name, key_schema, attribute_definitions, region):
        try:
            dynamodb_resource = boto3.resource("dynamodb", region_name=region)
            self.table = dynamodb_resource.create_table(TableName=table_name,KeySchema=key_schema, AttributeDefinitions=attribute_definitions)
          
            print('----Table CReating. START WAITING')
            #   wait until the table exists
            self.table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
            print('----Finish WAITING')
            
        except ClientError as e:
            logging.error(e)
            return False
        return True
      
    #   Add a record to the referenced table
    def put_item(self, region, table_name, itemObj):
        try:
            dynamodb_resource = boto3.resource("dynamodb", region_name=region)
            table = dynamodb_resource.Table(table_name)
            table.put_item(Item=itemObj)
        
        except ClientError as e:
            logging.error(e)
            return False
        return True   
       
    #   Retrieve an item based on the name and ID
    def get_an_item(self,region,table_name,keyInfoDict):
        try:
            dynamodb_resource = boto3.client("dynamodb", region_name=region)
            
            response = dynamodb_resource.get_item(
                TableName = table_name,
                Key = keyInfoDict
            )

            #response = table.get_item(Key=keyInfoObj)
            #item = response['Item']
            #print(item)
            print(response)
  
        except ClientError as e:
            logging.error('GET Error:')
            logging.error(e)
            return False
        return True
            
        
def main():
    region = 'us-east-1'
    d = DynamoDBLab()
    
    table_name = "CPP_ProjectTest2"
    
    key_schema = [
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'   # PARTITION KEY
        },
        {
            'AttributeName': 'id',
            'KeyType': 'RANGE'   # SORT KEY
        }
    ]
    attribute_definitions = [
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        }
    ]
    
    try:
        #   User Has the followingoptions: 
        #       Create table and upload data
        #       View the contents of a table
        #       Generate a UNIQUE record ID
        userInput = int(input("Choose 1 to create and upload table or 2 to display table contents or 3 to generate a random ID: "))
    
        if 1 == userInput:
            #   check if table exists before creating it, otherwise update it with values from teh references CSV file
            if not d.create_lab_table(table_name,key_schema,attribute_definitions,region):
               with path.open() as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    
                    for row in csv_reader:
                        name = row['name']
                        id = row["id"]
                        email = row["email"]
                        account_status = row["account_status"]
                        first_name = row["first_name"]
                        last_name = row["last_name"]
                        s3_bucket_name = row["s3_bucket_name"]
                        s3_profile_image = row["s3_profile_image"]
                        
                        
                        #print('Name ' + name + ' ID ' + id + ' Result ' + result + ' Description ' + desc + ' Date ' + date)
                        
                        metadata_item = {'name': name,'id': id, 'email':email, 'account_status': account_status, 'first_name': first_name, 'last_name': last_name, 's3_bucket_name': s3_bucket_name, 's3_profile_image': s3_profile_image}
                        
                        print('name = '+name)
                        print('id = '+id)
                        print('email = '+email)
                        print('account_status = '+account_status)
                        print('first_name = '+first_name)
                        print('last_name = '+last_name)
                        print('s3_bucket_name = '+s3_bucket_name)
                        print('s3_profile_image = '+s3_profile_image)
                        print('region = '+region)
                        print('table_name = '+table_name)

                        
                        try:
                            upload_response = d.put_item(region, table_name, metadata_item)
                            print("--------DATA ADDED---------"+name)
                        except ClientError as e:
                            #print("Failed to Add "+name)
                            print(e.response['Error']['Message'])
    
                        pass
        elif 2 == userInput:
            
            serializer = TypeSerializer()
            
            keyName = "1a71aa3e-3a2e-43e2-bb43-3cdee3ceff0b"
            print(keyName)
            print(serializer.serialize(keyName) )

            keyId = 8393280243558150661
            print(keyId)
            print(serializer.serialize(keyId) )
            '''
            keyInfoDict = {
              "name": serializer.serialize("testD"),
              "id": serializer.serialize(4)
            }
            '''
            keyInfoDict = {
              'name': keyName,
              'id': keyId
            }
            
            print(table_name)
            
            
            if d.get_an_item(region,table_name,keyInfoDict):
                print('data retrieved')
            else:
                print("Error! Incorrect Entry")
        elif 3 == userInput:
            try:
                rowId = d.generate_row_id()
                print(rowId)
            except ValueError:
                print("Error! Randomw number didn't work.")
                
        
    except ValueError:
        print("Error! This is not a number. Try again.")
        

if __name__ == '__main__':
    main()