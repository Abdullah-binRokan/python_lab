# create a list of three dict
people = [
    {"name": "Ahmed", "phone": "0505555555", "email": "ahmed@ds.com"},
    {"name": "Khalid", "phone": "0544444444", "email": "khalid@ds.com"},
    {"name": "Nasser", "phone": "0533333333", "email": "Nasser@ds.com"},
]

name = input("name: ")

for person in people:
    if person["name"] == name:
        print(f"Phone: {person['phone']} \nEmail: {person['email']}")
        break
else:
    print("Not Found")
