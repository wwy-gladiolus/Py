def identify_vowel(letter):
    match letter.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print("This letter is a vowel.")
        case _:
            print("This letter is a consonant.")
