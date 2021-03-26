word_1 = "cans"
word_2 = "cons"
def common_letters(word1,word2):
    set1 = set(word1)
    set2 = set(word2)
    lst = (set1 & set2)
    lst_as_str = ','.join(lst)
    return 'common letters:' + lst_as_str
print(common_letters(word_1,word_2));
