import random

with open("corpus.txt") as file:
    text = file.read()

text = [word.lower() for word in text.split(' ') if word != '']

markov_chain = {}
for current_word, next_word in zip(text, text[1:]):
    markov_chain.setdefault(current_word, []).append(next_word)

current_word = random.choice(list(markov_chain.keys()))
sentence = []

for i in range(0,15):
    sentence.append(current_word)
    if current_word in markov_chain and len(markov_chain[current_word]) > 0:
        current_word = random.choice(markov_chain[current_word])
    else:
        break

print(' '.join(sentence))