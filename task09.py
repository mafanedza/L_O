def vowel(word):
    vowels = "aeiuoAEIOU"
    word_set = set(word)
    vowels_set = set(vowels)
    lst = (word_set & vowels_set )
    print("Vowels: " + str(lst))
vowel('Mafanedza');
