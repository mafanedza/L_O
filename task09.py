def vowel(word):
    vowels = "aeiuoAEIOU"
    word_as_set = set(word)
    vowels_as_set = set(vowels)
    lst = (word_as_set & vowels_as_set )
    lst_as_str = ', '.join(lst)
    return "Vowels: "+ lst_as_str
print(vowel('Mafanedza'));
