def match_specials(v):
    match v:
        case True:
            print("True")
        case False:
            print("False")
        case None:
            print("None")
        case _:
            print("Unkown")

