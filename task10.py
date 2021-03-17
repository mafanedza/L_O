word_1 = "cans"
word_2 = "cons"
def common_letters(x,y):
    for i in x :
        if i in y:
            print("common letter " + i)
print(common_letters(word_1,word_2))