import requests
request_for_image = "http://openweathermap.org/img/wn/09d@2x.png"
request_for_data = "http://api.openweathermap.org/data/2.5/weather?q=New%20Delhi&appid=976535ec83c4aba2eae773b96f0c6986&units=metric"
response = requests.get(request_for_data)
response.status_code
""" 
if successful, returns 200
>
if response.status_code == 200:
    print('Success!')
else:
    print('Not Found.')

No need to use >
response.encoding = 'utf-8' > converts bytes to string

json_response = response.json() > returns a dictionary whose value can be directly accessed

print(json_response['main']['temp'])
print(json_response['name'])
print(json_response['weather'][0]['main'])
print(json_response['weather'][0]['description'])
print(json_response['weather'][0]['icon'])



