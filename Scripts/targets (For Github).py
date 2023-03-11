####################################
## Input private Tokens for API's ##
####################################

'''

Use this file to retreive your API tokens on the edge device globally.



'''


def thingsboard_api_json():
    ## Thingsboard Device URL and Token
    url = "pctips.ca"
    token = "7lKHbbyvfERjik7edVeJ" 
    api = "https://{0}/api/v1/{1}/telemetry".format(url, token)
    return api

def thingsboard_api_mqtt():
    broker = "<Dashboard IP>" # Have it pointing to external IP
    port = 1883
    token = "7lKHbbyvfERjik7edVeJ"
    topic = "v1/devices/me/telemetry"
    return broker, port, token, topic

