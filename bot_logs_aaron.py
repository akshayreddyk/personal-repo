import requests
print("test")

def authentication():

    Auth_URL = 'https://uipathorchestratorprod.kellyservices.com/api/account/authenticate'
    tenancyName = 'Default'
    username = 'sres587'
    password = 'kelly123'

    response = requests.post(Auth_URL,data={'tenancyName': tenancyName,'usernameOrEmailAddress': username,'password' : password})

    json_response = response.json()

    access_token='Bearer '+ json_response['result']
    print(access_token)
    return (access_token)

def ErrorLogs():
    access_token=authentication()
    response = requests.get('https://uipathorchestratorprod.kellyservices.com/odata/RobotLogs?',
                            headers={'Content-Type' : 'application/json','Authorization': access_token} )

    logsdef= response.json()
    print(response)
    logs=''
    for each in logsdef['value']:
        print(each['ProcessName'])
        print(each['Message'])


def main():
    print("This function will start the job in the selected robot system which is already connected to orchestrator")
    ErrorLogs()
    
if __name__ == "__main__":
    main()
