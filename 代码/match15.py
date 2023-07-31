def identify_vowel(letter):
    match letter.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u' as l:
            print(str(l) + " is a vowel.")
        case _ as l:
            print(str(l) + " is a consonant.")
