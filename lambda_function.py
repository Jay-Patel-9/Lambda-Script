import os

def lambda_handler(event, context):
    variable1 = os.environ.get('SECRET_API_KEY')
    print(f'Value of ENV_VARIABLE_1: {variable1}')

    return {
        'statusCode': 200,
        print(f'Value of ENV_VARIABLE_1: {variable1}')
    }