import requests
main_api='https://uiporchestratorsbx.kellyservices.com/odata/QueueDefinitions'
json_data=requests.get(main_api).json()
print (json_data)
