d = {'2': 'абвг',
     '3': 'дeжз',
     '4': 'ийкл',
     '5': 'мноп',
     '6': 'рсту',
     '7': 'фхцч',
     '8': 'шщъы',
     '9': 'ьэюя',
     '1': '.,-'}
a = input().split()
comb = input()
for word in a:
    if len(word) >= len(comb) and \
            all(w.lower() in d[c] for w, c in zip(word, comb)):
        print(word, end=' ')