import requests, json, random
from filter2 import matches, sowpod_words

s = requests.Session()

register_data = {"name": "Keerthana"}

headers = {'Content-Type' : 'application/json'}

reg_resp = s.post('https://we6.talentsprint.com/game/register', data=json.dumps(register_data), headers=headers)
print(reg_resp.json())
id = reg_resp.json()['id']

create_data={"id": id, "overwrite": True}

create_resp= s.post('https://we6.talentsprint.com/game/create', data=json.dumps(create_data), headers=headers)

print(create_resp.json())

possibles = sowpod_words
guess_word = random.choice(possibles) 

word = {"guess":guess_word, "id": id}
guess_resp = s.post("https://we6.talentsprint.com/game/guess",headers = headers, data = json.dumps(word)) 

back = guess_resp.json()['feedback']

while back != "GGGGG":
    if guess_resp.json()['message'] == '0 guesses left':
        break

    possibles = matches(possibles,guess_word,back)
    guess_word = random.choice(possibles)

    word = {"guess":guess_word, "id": id}
    guess_resp = s.post("https://we6.talentsprint.com/game/guess",headers =headers, data = json.dumps(word)) 
    print(guess_resp.json())

    back = guess_resp.json()['feedback']
    print(guess_word)