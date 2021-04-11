import boto3

print('Loading function')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CounterTable')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    try:
        response = table.get_item(Key={
            'CounterID': 0})
        
        counterValue = int(response['Item']['CounterValue'])
        return counterValue
    except Exception as e:
        print(e)
        print('Something went wrong.')
        raise e
