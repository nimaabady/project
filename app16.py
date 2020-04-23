phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
output = ""
i = 0
for ch in phone:
    if i == 3 or i == 6:
        output += "- "
    output += digits_mapping.get(ch, "!") + " "
    i += 1
print(output)
