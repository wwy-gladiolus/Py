#定义一个模拟菜单的函数。
def menu_simulate(choice):
    """This function simulates a menu.

        The virtual menu provides three items:
        Setting: chosen by input 1
        Help: chosen by input 2
        Logout: chosen by input 3
    """

    legal = False

    match choice:
        case 1:
            legal = True
            print("Setting\n")
        case 2:
            legal = True
            print("Help\n")
        case 3:
            legal = True
            print("Logout\n")

    if legal:
        return 0
    else:
        return 1


#仅当脚本在顶层环境中运行时才执行。
if __name__ == '__main__':
    choice = 0
    while choice != 3:
        choice = int(input("Menu:\n1 Setting\n2 Help\n3 Logout\n"))
        if menu_simulate(choice):
            print(str(choice) + ' is an illegal menu item!\n')

