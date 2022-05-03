import requests



def authentication() :
    Auth_URL = 'https://uiporchestratorsbx.kellyservices.com/api/account/authenticate'
    tenancyName = 'Default'
    username = '587sres'
    password = 'kelly123'

    response = requests.post(Auth_URL,data={'tenancyName': tenancyName,'usernameOrEmailAddress': username,'password' : password})

    json_response = response.json()

    access_token='Bearer '+ json_response['result']
    return (access_token)

  


def queueDef():

    access_token= authentication()
    print(access_token)
    response = requests.get('https://uiporchestratorsbx.kellyservices.com/odata/QueueDefinitions', headers={'Content-Type' : 'application/json','Authorization': access_token} )

    Queue_Def= response.json()

    for each in Queue_Def['value']:
        print(each['Name'])


if __name__ == '__main__':
    print("execution started")
    queueDef()
