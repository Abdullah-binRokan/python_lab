# dict only got key: value pairs
# we can't have email for person unless
# we use a list of dict i.e. 10_phonebook_listOfDict.py
people = {
    "Ahmed": "0505555555",
    "Khalid": "0544444444",
    "Nasser": "0533333333",
}

name = input("name: ")

for person, number in people.items():
    if person == name:
        print(f"Found {number}")
        break
else:
    print("Not found")