import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(input_data):
    converted_input_data = input_data.casefold()
    if converted_input_data in data:
        return data[converted_input_data]
    elif converted_input_data.title() in data:
        return data[converted_input_data.title()]
    elif converted_input_data.upper() in data:
        return data[converted_input_data.upper()]
    elif len(get_close_matches(converted_input_data, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Press 'Y' if yes, or 'N' if no: " % get_close_matches(converted_input_data, data.keys(), cutoff=0.8)[0])
        if yn.casefold() == "y":
            return data[get_close_matches(converted_input_data, data.keys(), cutoff=0.8)[0]]
        elif yn.casefold() == "n":
            return "%s is not exists. Please recheck." % input_data
        else:
            return "You didn't enter the right key. Try again"
    else:
        return "%s is not exists. Please recheck." % input_data

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for defination in output:
        print("- %s" % defination)
else:
    print(output)

