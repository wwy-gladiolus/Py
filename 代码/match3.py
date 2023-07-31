def number_match(a, b):
    match a + b:
        case 0j:
            print("They are opposite numbers.")
        case 10.0:
            print("They are complementary numbers against 10.")
        case 100:
            print("They are complementary numbers against 100.")
        case _:
            print("They have no special relations.")

