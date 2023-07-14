from classes.colors import Colors

# main logo
def main_logo():
    """
    Displays the main logo for the game
    """
    print(f"""{Colors.yellow}
    
                                      _             ___          _      
                      /\/\   __ _ ___| |_ ___ _ __ / __\___   __| | ___ 
                     /    \ / _` / __| __/ _ \ '__/ /  / _ \ / _` |/ _ \\
                 /\ / /\/\ \ (_| \__ \ ||  __/ | / /__| (_) | (_| |  __/
                /  |\/    \/\__,_|___/\__\___|_| \____/\___/ \__,_|\___|
  *            /  /________________________________________________
 (O)77777777777)  7                                                `~~--__
8OO>>>>>>>>>>>>] <===========================================>          __-
 (O)LLLLLLLLLLL)  L________________________________________________.--~~
  *            \  \
                \  |
                 \/ 
                                                    
{Colors.default}\n""")

# divider
def divider_image():
    """
    Displays a divider image of two swords"
    """

# Triforce
def triforce():
    """
    Displays the Triforce 'bonus' content - code by John Cartwright (see credits in README.md)
    """
    tri = f"{Colors.yellow}▲"
    big_tri = []
    for i in range(1,21,2):
        big_tri.append(" "*int((19-i)/2) + tri*i + " "*int((19-i)/2))
    for t1 in big_tri:
        print(" "*10 + t1 + " "*10)
    for t2 in big_tri:
        print(t2 + " " + t2)