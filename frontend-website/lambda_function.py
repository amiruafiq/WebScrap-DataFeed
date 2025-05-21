import json
import boto3

bedrock = boto3.client('bedrock-agent-runtime')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        question = body.get('question', '')

        response = bedrock.retrieve_and_generate(
            input={
                "text": question
            },
            retrieveAndGenerateConfiguration={
                "knowledgeBaseId": "<INSERT ID HERE>",
                "modelArn": "<ARN MODEL HERE>"
            }
        )

        answer = response['output']['text']
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'answer': answer})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
