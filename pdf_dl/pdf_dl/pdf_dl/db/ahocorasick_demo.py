import ahocorasick

A = ahocorasick.Automaton()
# A.addword('手续费')
for index, word in enumerate('手续费 保证金'.split()):
    A.add_word(word, (index, word))
A.make_automaton()
for item in A.iter('明天提高IF手续费'):
    print(item)

ans = list(A.iter('明天提高IF手续费'))

ans3 = list(A.iter('明天提高payment'))

for item in A.iter('明天提高I'):
    print(item)