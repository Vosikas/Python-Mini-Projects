import requests
import json
def trims():
    make=input("Brand: ")
    year=input("Year: ")

    url = "https://www.carqueryapi.com/api/0.3/"
    params = {
        "cmd": "getModels",
        "make": make,
        'year':year
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    #'model_engine_fuel': 'Flex-Fuel (Unleaded/E85)'
    #'model_lkm_mixed': '30.0'
    response = requests.get(url, params=params,headers=headers)
    trim1=(response.json().get("Models"))
    for item in trim1:
        print(item.get("model_name"))
    model =input("Which model do you have(Copy the full edition)? ")
    params2 = {
        "cmd": "getTrims",
        "make_id": make,
        "model": model,
        "year": year,

    }
    response = requests.get(url, params=params2,headers=headers)
    trim2=(response.json().get("Trims"))
    for item in trim2:
        trim=item.get("model_trim")
        print(trim)
    trim=input("Which edition do you have(Copy the full edition)? ")
    params3 = {
        "cmd": "getTrims",
        "make_id": make,
        "model": model,
        "year": year,
        "trim": trim
    }
    response = requests.get(url, params=params3,headers=headers)
    trim3=(response.json().get("Trims"))
    for item in trim3:
        if item.get("model_trim")==trim:
            fuel=item.get("model_engine_fuel")
            avg= item.get("model_lkm_mixed")
    print (fuel,avg)
