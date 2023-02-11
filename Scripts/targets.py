####################################
## Input private Tokens for API's ##
####################################

'''

Use this file to retreive your API tokens on the edge device globally.



'''


def thingsboard_api():
    ## Thingsboard Device URL and Token
    url = "<Enter the Address of the RPi with the port hosting Thingsboard or the WAN URL"
    token = "<Enter the Generated API key/Token>" 
    api = "https://{0}/api/v1/{1}/telemetry".format(url, token)
    return api
