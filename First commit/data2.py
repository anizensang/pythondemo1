import json
from difflib import get_close_matches
data = json.load(open("E:\My python codes\english thesaures\data.json"))
# data = dict((k.lower(),  v) for k,v in data.items())
my_list= []
# print(data.keys())
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    # elif w.title() in data:
    #     return data[w.title()]

    elif len(get_close_matches(w , data.keys())) > 0 :
        ip = input("Did you mean %s instead? Enter Y/y if yes , or N/n if no: " % get_close_matches(w,data.keys()))

        if ip == 'Y' or ip == 'y':
            for index, item in enumerate(get_close_matches(w,data.keys())):
                     my_list.append(data[get_close_matches(w,data.keys())[index]])
                     index += 1
        
            return my_list

        elif ip == 'N' or ip == 'n':
            return "The word does not exist. Please double check it"
        else:
            return "We didnot understand your entry."

    else:
        return "The word does not exist . Please double check it."

word = input("Enter word: ")

output = translate(word)


# print(output)
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)



