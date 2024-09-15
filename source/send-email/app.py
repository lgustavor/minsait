import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    sender = event['sender']
    recipient = event['recipient']

    bucket = event['bucket']
    s3_output_file = event['s3OutputFileName']

    pre_signed_url = generate_s3_signed_url(bucket, s3_output_file)

    send_email(sender, recipient, pre_signed_url)

    return {"response": "success"}


def generate_s3_signed_url(bucket, s3_target_key):
    return s3_client.generate_presigned_url('get_object',
                                            Params={'Bucket': bucket,
                                                    'Key': s3_target_key},
                                            ExpiresIn=3600)


def send_email(sender, recipient, pre_signed_url):
    subject = "Processo Batch completo:"

    body_text = ("O arquivo foi processado com sucesso\r\n"
                 "Clica no link "
                 + pre_signed_url + "."
                 )

    charset = "UTF-8"

    client = boto3.client('ses')

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': charset,
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': charset,
                    'Data': subject,
                },
            },
            Source=sender,

        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
