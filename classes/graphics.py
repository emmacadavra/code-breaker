# colour class
class Colours:
    """
    ANSI escape codes to be used with their respective colours
    """
    default = "\033[0;37;40m"
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    yellow = "\033[1;33;40m"
    blue = "\033[1;34;40m"
    pink = "\033[1;35;40m"
    cyan = "\033[1;36;40m"
    white = "\033[1;37;40m"
    red_block = "\033[1;31;41m"
    green_block = "\033[1;32;42m"
    yellow_block = "\033[1;33;43m"
    blue_block = "\033[1;34;44m"
    pink_block = "\033[1;35;45m"
    cyan_block = "\033[1;36;46m"
    white_block = "\033[1;37;47m"


# main logo
def main_logo():
    print(f"""{Colours.yellow}
    
                      _             ___          _      
      /\/\   __ _ ___| |_ ___ _ __ / __\___   __| | ___ 
     /    \ / _` / __| __/ _ \ '__/ /  / _ \ / _` |/ _ \
    / /\/\ \ (_| \__ \ ||  __/ | / /__| (_) | (_| |  __/
    \/    \/\__,_|___/\__\___|_| \____/\___/ \__,_|\___|
                                                    
{Colours.default}\n""")


# Triforce
def triforce():
    tri = f"{Colours.yellow}▲"
    big_tri = []
    for i in range(1,21,2):
        big_tri.append(" "*int((19-i)/2) + tri*i + " "*int((19-i)/2))
    for t1 in big_tri:
        print(" "*10 + t1 + " "*10)
    for t2 in big_tri:
        print(t2 + " " + t2)