import boto3

client = boto3.client('appstream')

stack_name = 'YOUR STACK NAME'
fleet_name = 'YOUR FLEET NAME'
user_id = 'YOUR USER ID'
application_id = 'YOUR APPLICATION ID' # use 'Desktop' for desktop mode
validity = 3600 # For how long the URL will be active

# See full documentation here:
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_streaming_url
response = client.create_streaming_url(
    StackName=stack_name,
    FleetName=fleet_name,
    UserId=user_id,
    ApplicationId=application_id,
    Validity=validity,
)

streaming_url = response['StreamingURL']
expiration = response['Expires']

print("Streaming URL: ", streaming_url)
print("Expiration: ", expiration)

try:
    import webbrowser
    webbrowser.open(streaming_url, new=2)
except Exception:
    pass