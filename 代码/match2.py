def menu_simulate(choice):
    """This function simulates a menu.

        The virtual menu provides three items:
        Setting: chosen by input 1
        Help: chosen by input 2
        Logout: chosen by input 3
    """

    match choice:
        case 1:
            print("Setting\n")
        case 2:
            print("Help\n")
        case 3:
            print("Logout\n")
        case _:    #这是兜底case子句。
            print(str(choice) + ' is an illegal menu item!\n')


if __name__ == '__main__':
    choice = 0
    while choice != 3:
        choice = int(input("Menu:\n1 Setting\n2 Help\n3 Logout\n"))
        menu_simulate(choice)

