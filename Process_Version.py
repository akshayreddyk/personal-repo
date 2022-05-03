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

def ProcessVersion():
    access_token=authentication()
    Process=input("Enter Process Name : ")
    try: 
        ApiUrl="https://uiporchestratorsbx.kellyservices.com/odata/Processes?$filter=contains(Id,'"+Process+"')"
        response = requests.get(ApiUrl, headers={'Content-Type' : 'application/json','Authorization': access_token} )
        processDetails= response.json()
        VersionDetails=''
        for each in processDetails['value']:
            VersionDetails=VersionDetails+(each['Key'])+'\n'       
        return(VersionDetails)
    except:
        print("Invalid Process Name")

def main():
    VersionDetails=ProcessVersion()
    print(VersionDetails)
    
if __name__ == "__main__":
    main()
