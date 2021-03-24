word_1 = "cans"
word_2 = "cons"
def common_letters(x,y):
    s1 = set(x)
    s2 = set(y)
    lst = (s1 & s2)
    print('common letters:' + str(lst))
common_letters(word_1,word_2)
