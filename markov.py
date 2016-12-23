import random, re

text = []

with open('corpus.txt') as fh:
    for line in fh:
        line = re.sub(r'([\,\.\!\?\;\:])', r' \1 ', line)
        line = re.sub(r'[^a-zA-Z0-9|\,|\.|\!|\?|\;|\:|\'|\’]', ' ', line)
        text += [word.lower().strip() for word in line.split() if word.strip() != ''] + ['\n']

markov_chain = {}
for previous_word, current_word, next_word  in zip(text, text[1:], text[2:]):
    markov_chain.setdefault((previous_word, current_word), []).append(next_word)

previous_word, current_word = random.choice(list(markov_chain.keys()))
sentence = [previous_word]

for i in range(0,20):
    sentence.append(current_word)
    if (previous_word, current_word) in markov_chain and len(markov_chain[(previous_word, current_word)]) > 0:
        previous_word, current_word = current_word, random.choice(markov_chain[(previous_word, current_word)])
    else:
        break

print(' '.join(sentence).replace('\n ', '\n'))