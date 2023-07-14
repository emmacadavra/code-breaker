from classes.colors import Colors

# main logo
def main_logo():
    """
    Displays the main logo for the game
    """
    print(f"""
     {Colors.blue}(__)
     [//]
     [\\\]
     [//]{Colors.pink}
  /\_[{Colors.blue}\\/{Colors.pink}]_/\ 
 //__{Colors.yellow}<()>{Colors.pink}__\\\ 
/// \[{Colors.cyan}/\{Colors.pink}]/ \\\\\     {Colors.yellow}/\\\,/\\\,               ,{Colors.pink}
\(   {Colors.cyan}||||{Colors.pink}   )/    {Colors.yellow}/| || ||    _          ||{Colors.cyan}
     ||||         {Colors.yellow}|| || ||   < \,  _-_, =||=  _-_  ,._-_{Colors.cyan}
     ||||         {Colors.yellow}||=|= ||   /-|| ||_.   ||  || \\\  ||{Colors.cyan}
     ||||        {Colors.yellow}~|| || ||  (( ||  ~ ||  ||  ||/    ||{Colors.cyan}
     ||||         {Colors.yellow}|, \\\,\\\,  \/\\\ ,-_-   \\\, \\\,/   \\\,{Colors.cyan}
     ||||        {Colors.yellow}_-{Colors.cyan}
     ||||                   {Colors.yellow},- _~.        |\{Colors.cyan}
     ||||                  {Colors.yellow}(' /|           \\\{Colors.cyan}
     ||||                 {Colors.yellow}((  ||    /'\\\  / \\\  _-_{Colors.cyan}
     ||||                 {Colors.yellow}((  ||   || || || || || \\\\{Colors.cyan}
     ||||                  {Colors.yellow}( / |   || || || || ||/{Colors.cyan}
     ||||                   {Colors.yellow}-____- \\\,/   \\\/  \\\,/{Colors.cyan}
     \\\//
      \/{Colors.default}
      \n""")

def header_image():
    """
    A header/banner image that shows above the game/instructions areas
    """
    print(f"""
                    {Colors.yellow}╔╦╗╔═╗╔═╗╔╦╗╔═╗╦═╗  ╔═╗╔═╗╔╦╗╔═╗{Colors.pink}
         />         {Colors.yellow}║║║╠═╣╚═╗ ║ ║╣ ╠╦╝  ║  ║ ║ ║║║╣{Colors.pink}
        //          {Colors.yellow}╩ ╩╩ ╩╚═╝ ╩ ╚═╝╩╚═  ╚═╝╚═╝═╩╝╚═╝{Colors.blue}
[//////{Colors.pink}<*>|||<{Colors.cyan}==========================================-----------{Colors.pink}
        \\\ 
         \>{Colors.default}
        \n""")

# divider
def divider_image():
    """
    Displays a divider image of two swords"
    """
    print("""
              O                                     O
        {o)xxx|===============-  *  -===============|xxx(o}
              O                                     O
        """)

# Triforce
def triforce():
    """
    Displays the Triforce 'bonus' content - code by John Cartwright (see credits in README.md)
    """
    clear_screen()

    tri = f"{Colors.yellow}▲"
    big_tri = []
    for i in range(1,21,2):
        big_tri.append(" "*int((19-i)/2) + tri*i + " "*int((19-i)/2))
    for t1 in big_tri:
        print(" "*10 + t1 + " "*10)
    for t2 in big_tri:
        print(t2 + " " + t2)


def you_win():
    """
    Displays a 'You Win!' graphic when the player wins
    """
    print(f"""
        
       ██╗   ██╗ ██████╗ ██╗   ██╗
    .  ╚██╗ ██╔╝██╔═══██╗██║   ██║    0
   / \  ╚████╔╝ ██║   ██║██║   ██║    8
   | |   ╚██╔╝  ██║   ██║██║   ██║ `--8--'
   | |    ██║   ╚██████╔╝╚██████╔╝   |:|
   |.|    ╚═╝    ╚═════╝  ╚═════╝    |:|
   |.|                               |.|
   |:|   ██╗    ██╗██╗███╗   ██╗██╗  |.|
   |:|   ██║    ██║██║████╗  ██║██║  | |
 `--8--' ██║ █╗ ██║██║██╔██╗ ██║██║  | |
    8    ██║███╗██║██║██║╚██╗██║╚═╝  \ /
    O    ╚███╔███╔╝██║██║ ╚████║██╗   .
          ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝ 
          \n""")


def game_over():
    """
    Displays a 'Game Over' graphic when the player loses
    """
    print(f"""{Colors.red}

  ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
░ ░   ░   ░   ▒   ░      ░      ░   
 ▒█████   ██▒ ░ █▓▓█████ ░██▀███░  ░
▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒  
▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒  
▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄    
░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒  
░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░  
  ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░  
░ ░ ░ ▒       ░░     ░     ░░   ░   
    ░ ░        ░     ░  ░   ░       
              ░                     
    {Colors.default}""")