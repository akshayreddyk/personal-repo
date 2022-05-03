import requests
import inspect
queue_list=[]

def authentication():

    Auth_URL = 'https://uiporchestratorsbx.kellyservices.com/api/account/authenticate'
    tenancyName = 'Default'
    username = '587sres'
    password = 'kelly123'

    response = requests.post(Auth_URL,data={'tenancyName': tenancyName,'usernameOrEmailAddress': username,'password' : password})

    json_response = response.json()

    access_token='Bearer '+ json_response['result']
    return (access_token)



    
def ProcessVersion():
    access_token=authentication()
    if inspect.stack()[1].function == '<module>':
        ApiUrl='null'
    else:
        Process=input("Enter Process Name")
        try: 
            ApiUrl="https://uiporchestratorsbx.kellyservices.com/odata/Processes?$top=1&$filter=contains(Id,'"+Process+"')"
            response = requests.get(ApiUrl, headers={'Content-Type' : 'application/json','Authorization': access_token} )
            processDetails= response.json()
            VersionDetails =processDetails['value'][0]['Key']
            return(VersionDetails)
        except:
            print("error")

            
def QueueNames():
    access_token=authentication()
    response = requests.get('https://uiporchestratorsbx.kellyservices.com/odata/QueueDefinitions', headers={'Content-Type' : 'application/json','Authorization': access_token} )

    Queue_Def= response.json()
    queue_name=''
    for each in Queue_Def['value']:
        queue_name=queue_name+(each['Name'])+'\n'
    return(queue_name)



def ErrorLogs():
    access_token=authentication()
    response = requests.get('https://uiporchestratorsbx.kellyservices.com/odata/RobotLogs?$top=10&$filter=Level eq UiPath.Core.Enums.LogLevel%27Fatal%27', headers={'Content-Type' : 'application/json','Authorization': access_token} )

    logsdef= response.json()
    logs=''
    for each in logsdef['value']:
        logs=logs+(each['Message'])+'\n--'
    return(logs)


def ProcessList():
    access_token=authentication()
    response = requests.get('https://uiporchestratorsbx.kellyservices.com/odata/Processes', headers={'Content-Type' : 'application/json','Authorization': access_token} )
    process_Def= response.json()
    process_list=''
    for each in process_Def['value']:
        process_list=process_list+(each['Key'])+'\n'
    return(process_list)




    

