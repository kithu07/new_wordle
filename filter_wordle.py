import random
def match_contains(words: list, letter: str, pos: int):
    return [word for word in words if letter in word]

def match_exact(words: list, letter: str, pos:int):
    return [word for word in words if word[pos] == letter]

def match_excludes(words: list, letter: str, pos: int):
    return [word for word in words if letter not in word]

filter = {'R': match_excludes, 'Y': match_excludes, 'G': match_exact}

def choose(words: list, guess: str='', feedback: str=''):
    for pos, (letter, fb) in enumerate(zip(guess, feedback)):
        words = filter[fb](words, letter, pos)
    return random.choice(words)

def exact_words(filename: str, size: int=5):
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [lines.strip() for line in lines]
    return lines