import os
import random
import re


def chain(path):
    markovchain = {}  # Generated chain stored as dictionary
    word1 = ""
    word2 = ""
    for file in path:
        with open(os.path.relpath(path)) as file: # Open sesame
            for line in file:
                for current_word in line.split():
                    if current_word is not "":
                        markovchain.setdefault((word1, word2), []).append(current_word)
                        word1 = word2
                        word2 = current_word
    return markovchain


# Generate sentences
def sentence(markovchain, wc):
    sentence = ""
    word_tuple = random.choice(markovchain.keys())
    w1 = word_tuple[0]
    w2 = word_tuple[1]

    for i in xrange(wc):
        new_word = random.choice(markovchain[(w1,w2)])
        sentence += " " + new_word
        w1 = w2
        w2 = new_word



# WHAT MY ENGLISH TEACHERS TAUGHT ME

    # Ending sentences
    if sentence[-1] != ".":
        if sentence[-1] in ["!", "?"]:
            pass
        if sentence[-1] == [","]:
            sentence[-1] = "."
        else:
            sentence += sentence + "."

    # Sentence case (thanks Blender!)
    def capitalizer(match):
        return match.group(0).upper()

    # Yung regex doin' its thang
    s = re.sub(r'(?:^\s*|[.?]\s+)(\w)', capitalizer, sentence)

    return s


# Pass in relative path where file.txt is located
markov = chain("../doc/zarathustra.txt")

sentence = sentence(markov, wc = 60)


print sentence
