import requests, json, random
from filter_wordle import matches, sowpod_words

s = requests.Session()

register_data = {"name": "Keerthana"}

headers = {'Content-Type' : 'application/json'}

reg_resp = s.post('https://we6.talentsprint.com/game/register', data=json.dumps(register_data), headers=headers)
print(reg_resp.json())
id = reg_resp.json()['id']

create_data={"id": id, "overwrite": True}

create_resp= s.post('https://we6.talentsprint.com/game/create', data=json.dumps(create_data), headers=headers)

print(create_resp.json())

current_guess = ''
current_feedback = ''

guess_data = {"id": id, "guess": random.choice(matches(sowpod_words, current_guess, current_feedback))}

while (current_feedback != 'GGGGG' and current_feedback != None):
    api_feedback = s.post('https://we6.talentsprint.com/game/guess', data=json.dumps(guess_data), headers=headers)
    current_feedback = api_feedback['feedback']
    next_guess = matches()