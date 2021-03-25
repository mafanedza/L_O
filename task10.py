word_1 = "cans"
word_2 = "cons"
def common_letters(x,y):
    s1 = set(x)
    s2 = set(y)
    lst = (s1 & s2)
    lst_as_str = ','.join(lst)
    print('common letters:' + lst_as_str)
common_letters(word_1,word_2)
