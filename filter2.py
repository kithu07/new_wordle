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
    
sowpod_words = load_data("sowpods_words.txt")