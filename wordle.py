import requests, json, random
s = requests.Session()

data_req = {"name":"keerthana"}
head = {"Content-Type":"application/json"}
reg_resp = s.post("https://we6.talentsprint.com/game/register",headers = head, data = json.dumps(data_req))
id = reg_resp.json()['id'] 
#print(id)

create_data = {"id": id,"overwrite": True}
create_resp = s.post("https://we6.talentsprint.com/game/create", headers = head, data = json.dumps(create_data))
#print(create_resp.json())

def match_contains(words: list[str], letter: str, pos: int) -> list[str]:
    return [word for word in words if letter in word]

def match_exact(words: list[str], letter: str, pos: int) -> list[str]:
    return [word for word in words if word[pos] == letter]

def match_excludes(words: list[str], letter: str, pos: int) -> list[str]:
    return [word for word in words if letter not in word]

filters = {'R': match_excludes, 'G': match_exact, 'Y': match_contains}

def matches(words: list[str], guess: str, feedback: str):
    for pos, (letter, fb) in enumerate(zip(guess, feedback)):
        words = filters[fb](words, letter, pos)
    return words

def load_data(filename: str) -> list[str]:
    with open(filename,'r') as file:
        return [word[:-1] for word in file.readlines() if len(word) == 6]

data = load_data("sowpods_words.txt")
possibles = data
guess_word = random.choice(data) 

word = {"guess":guess_word, "id": id}
guess_resp = s.post("https://we6.talentsprint.com/game/guess",headers = head, data = json.dumps(word)) 

back = guess_resp.json()['feedback']

while back != "GGGGG":
    if guess_resp.json()['message'] == '0 guesses left':
        break

    possibles = matches(possibles,guess_word,back)
    guess_word = random.choice(possibles)

    word = {"guess":guess_word, "id": id}
    guess_resp = s.post("https://we6.talentsprint.com/game/guess",headers = head, data = json.dumps(word)) 
    print(guess_resp.json())

    back = guess_resp.json()['feedback']
    print(guess_word)