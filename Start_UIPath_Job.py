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

    print(response)
    x=response.json()
    
#    job_Key=x['value'][0]['Key']
 #   print(job_Key)
  #  URL="https://uiporchestratorsbx.kellyservices.com/odata/RobotLogs?$filter=contains(JobKey,'"+job_Key+"')"
   # response = requests.get(URL,headers={'Content-Type' : 'application/json','Authorization': access_token})
    #print(response.json())
    
    
    

def main():
    print("This function will start the job in the selected robot system which is already connected to orchestrator")
    StartJob()
    
if __name__ == "__main__":
    main()
