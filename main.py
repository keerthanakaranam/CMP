"""
Request Body

{
    "data": [
        {
            "Last_Name": "Sales Lead",
            "sequence_number": 1
        },
        {
            "Last_Name": "Quality Control",
            "sequence_number": 2
        }
    ]
}

"""

from flask import Request, jsonify, make_response
import requests
import json
import zcatalyst_sdk
url = "https://www.zohoapis.in/crm/v6/Contacts"
def handler(request: Request):
    try:
        app = zcatalyst_sdk.initialize()  # Initializing Catalyst SDK
        accesstoken = getAlienCountFromCatalystDataStore(app)
        print("The value of access token is")
        print(accesstoken)
        req_data = request.get_json()
        payload = req_data.get('request')
        print("The payload is")
       # print(payload)

        headers = {
                'Authorization': 'Zoho-oauthtoken '+accesstoken,
                'Content-Type': 'application/json',
                'Cookie': '1a99390653=e971ac9b8bc0886b07172d4aa3ed0bfb; _zcsr_tmp=46cfcc73-c5a1-49de-b023-177ce0185075; crmcsr=46cfcc73-c5a1-49de-b023-177ce0185075'
            }

            # Make the POST request
        print(payload)
        res = requests.post(url, headers=headers, json=payload)

            # Check for successful response
        if res.status_code == 201:
                print("Successfully created leads.")
                response = make_response(jsonify({
                "message": res.text
            }), res.status_code)
                return response
        else:
                print(f"Error: {res.status_code} - {res.text}")
                response = make_response(jsonify({
                "message": res.text
            }), res.status_code)
                return response

    except Exception as e:
        print(f"An error occurred: {str(e)}")

#Example usage with a valid requests object
#example_request = requests.Request(url=url, method="POST")
#prepared_request = example_request.prepare()
#handler(prepared_request)
def getAlienCountFromCatalystDataStore(app):   # Checks whether an alien encounter is already reported for the given city by querying the Data Store table
        connector = app.connection({
            'ConnectorName': {
            'client_id': '1000.5B7BV29R2ADSCTQSEXVLWTVH6QYSWH',
            'client_secret': '8ea228d6c174eb7b9ddfdb55127144f2a52983044a',
            'auth_url': 'https://accounts.zoho.in/oauth/v2/token',
            'refresh_url': 'https://accounts.zoho.in/oauth/v2/token',
            'refresh_token': '1000.2d4fbefb192a514a1c2cc206073fdf25.9a3e42b61b715155ab035637f94de0c1'
            }
            }).get_connector('ConnectorName')
        access_token = connector.get_access_token()
        print(access_token)
        return access_token