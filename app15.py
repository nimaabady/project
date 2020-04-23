customer = {
    "name": "john smith",
    "age": 30,
    "is_verified": True
}
customer["brihtdate"] = "nov 1 2020"
print(customer.get("birthdate", "not a key in dictonary"))
