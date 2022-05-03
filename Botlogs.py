import requests

def authentication():

    Auth_URL = 'https://uiporchestratorsbx.kellyservices.com/api/account/authenticate'
    tenancyName = 'Default'
    username = '587sres'
    password = 'kelly123'

    response = requests.post(Auth_URL,data={'tenancyName': tenancyName,'usernameOrEmailAddress': username,'password' : password})

    json_response = response.json()

    access_token='Bearer '+ json_response['result']
    return (access_token)

def ErrorLogs():
    access_token=authentication()
    response = requests.get('https://uiporchestratorsbx.kellyservices.com/odata/RobotLogs?$top=10&$filter=Level eq UiPath.Core.Enums.LogLevel%27Fatal%27', headers={'Content-Type' : 'application/json','Authorization': access_token} )

    logsdef= response.json()
    logs=''
    for each in logsdef['value']:
        logs=logs+(each['Message'])+'\n--'
    print(logs)


def main():
    print("in main")
    ErrorLogs()
    
if __name__ == "__main__":
    main()



    
def getBotId():
    access_token=authentication()
    botName = input(" Enter Bot Name ")
    try:
        Url="https://uiporchestratorsbx.kellyservices.com/odata/Robots?$filter=contains(Name,'"+botName+"')"
        response = requests.get(Url,headers={'Content-Type' : 'application/json','Authorization': access_token})
        BotDef=response.json()
        Id=BotDef['value'][0]['Id']
        return BotDef['value'][0]['Id']
    except:
        print("Invalid User Name")

        
def ReleaseKey():
    access_token=authentication()
    ProcessName = input(" Enter Process Name ")
    try:
        Url="https://uiporchestratorsbx.kellyservices.com/odata/Releases?$filter=contains(Name,'"+ProcessName+"')"
        response = requests.get(Url,headers={'Content-Type' : 'application/json','Authorization': access_token})
        ProDef=response.json()
        Key=ProDef['value'][0]['Key']
        print(ProDef['value'][0]['Name'])
        return Key
    except:
        print("Invalid Process Name")

    
def StartJob():
    access_token=authentication()
    Id=getBotId()
    Key=ReleaseKey()
    Parameterjson= {
                  "startInfo": {
                    "ReleaseKey": Key,
                    "RobotIds": [ ],
                    "NoOfRobots": 0,
                    "Strategy": "All",
                    "Source":"Manual",
                  }
                }
    response = requests.post('https://uiporchestratorsbx.kellyservices.com/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs',
                            headers={'Content-Type' : 'application/json','Authorization': access_token},
                            json=Parameterjson)

    return(response)
    

