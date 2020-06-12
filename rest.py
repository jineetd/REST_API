import requests

val=input("Enter the name of country to search for:")

url = "https://restcountries-v1.p.rapidapi.com/name/"+val

params={
    "name" : "India"
}
headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "9f249e62b7msh8ac5a6e6d404809p1283f7jsnada2c1233d16"
    }

response = requests.request("GET", url, headers=headers,params=params)

#print(type(response))

x=response.json()
name=x[0]['name']
calling_code=x[0]['callingCodes']
subregion=x[0]['subregion']
capital=x[0]['capital']
area=x[0]['area']

print("Name:"+name+"\n"+"Calling code:"+calling_code[0]+"\n"+"Subregion:"+subregion+"\n"+"Capital:"+capital+"\n"+"Area:"+str(area)+"\n")
#print(area)
