import json

def json_extration():

    with open("product.json","r") as file:
        python_data=json.load(file)

    with open("product.txt","w+") as file:
        for key, value in python_data.items():
            file.write(f"{key} : {value}\n")

json_extration()