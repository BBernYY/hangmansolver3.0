from english_words import get_english_words_set
import dutch_words
from unidecode import unidecode
from itertools import islice
# li = dutch_words.get_ranked()
import copy
li = get_english_words_set(['web2'], lower=True, alpha=True)
def guess(advicefunc):
    options2 = copy.copy(li)
    f = False
    anti = []
    while True:
        options = copy.copy(options2)
        options2 = []
        info = input("info?\n")
        a = input("anti?\n")
        if a != '':
            anti.append(a)
        for i in options:
            i = unidecode((i)).lower().replace("'", "").replace("(c)", "")
            for m in i:
                if m in anti:
                    f = True
                    break
            if f:
                f = False
                continue
            if (len(i) != len(info)):
                continue
            for j in range(len(info)):
                if not ((i[j] == info[j]) or ((info[j] == "_") and (i[j] not in info))):
                    break
                if j == len(info)-1:
                    options2.append(i)
            
        if len(options2) == 1:
            print("word is "+options2[0])
            break
        elif len(options2) == 0:
            print("word does not exist")
            break
        print(*advicefunc(options2, info), anti, sep="\n")
def advice(possibles, info):
    letters = {}
    for i in possibles:
        used = []
        for j in i:
            if j in used:
                continue
            if j in letters:
                letters[j] += 1
            else:
                letters[j] = 1
            used.append(j)
    best = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    best_possibles = {}
    with open("wordfreq.txt", "r") as f:
        freq = f.read().split("\n")
        for i in possibles:
            best_possibles[i] = 5052
            if i in freq:
                best_possibles[i] = freq.index(i)
    out = {}
    best_possibles = dict(sorted(copy.copy(best_possibles).items(), key=lambda item: item[1], reverse=False))
    for k,v in best.items():
        if not k in info:
            out[k] = v
    return (out, list(islice(best_possibles, 20)), len(possibles))
guess(advice)