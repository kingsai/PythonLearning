from pip._vendor.colorama import init, Fore
init()
def display(msg, is_warning = False):
    if is_warning:
        print(Fore.RED + msg)
    else:
        print(Fore.BLUE + msg)


# display('this is a msg')

