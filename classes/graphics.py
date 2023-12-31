from classes.colors import Colors


# main logo image function
def main_logo():
    """
    Displays the main logo for the game
    """
    print(f"""
      {Colors.blue}(__)
       []
       []           {Colors.yellow}/\\\,/\\\,               ,{Colors.purple}
   /\_[{Colors.blue}/\{Colors.purple}]_/\      {Colors.yellow}/| || ||    _          ||{Colors.purple}
  //__{Colors.yellow}<()>{Colors.purple}__\\\     {Colors.yellow}|| || ||   < \,  _-_, =||=  _-_  ,._-_{Colors.purple}
 /// \[{Colors.cyan}/\{Colors.purple}]/ \\\\\    {Colors.yellow}||=|= ||   /-|| ||_.   ||  || \\\  ||{Colors.purple}
 \(   {Colors.cyan}||||{Colors.purple}   )/   {Colors.yellow}~|| || ||  (( ||  ~ ||  ||  ||/    ||{Colors.cyan}
      ||||         {Colors.yellow}|, \\\,\\\,  \/\\\ ,-_-   \\\, \\\,/   \\\,{Colors.cyan}
      ||||        {Colors.yellow}_-{Colors.cyan}
      ||||                 {Colors.yellow},- _~.        |\{Colors.cyan}
      ||||                {Colors.yellow}(' /|           \\\{Colors.cyan}
      ||||               {Colors.yellow}((  ||    /'\\\  / \\\  _-_{Colors.cyan}
      ||||               {Colors.yellow}((  ||   || || || || || \\{Colors.cyan}
      ||||                {Colors.yellow}( / |   || || || || ||/{Colors.cyan}
      ||||                 {Colors.yellow}-____- \\\,/   \\\/  \\\,/{Colors.cyan}
      ||||
      \\\//
       \/{Colors.default}
    """)


# header/banner image function
def header_image():
    """
    A header/banner image that shows above the game/instructions areas
    """
    print(f"""
             {Colors.yellow}╔╦╗╔═╗╔═╗╔╦╗╔═╗╦═╗  ╔═╗╔═╗╔╦╗╔═╗{Colors.purple}
         />  {Colors.yellow}║║║╠═╣╚═╗ ║ ║╣ ╠╦╝  ║  ║ ║ ║║║╣{Colors.purple}
        //   {Colors.yellow}╩ ╩╩ ╩╚═╝ ╩ ╚═╝╩╚═  ╚═╝╚═╝═╩╝╚═╝{Colors.blue}
[//////{Colors.purple}<*>|||<{Colors.cyan}==========================================-----------{Colors.purple}
        \\\\
         \>{Colors.default}
    """)


# divider image function
def divider_image():
    """
    Displays a divider image of two swords"
    """
    print("""
         O                                     O
   {o)xxx|===============-  *  -===============|xxx(o}
         O                                     O
    """)


# Triforce function
def triforce():
    """
    Displays the Triforce 'bonus' content - code by John Cartwright (see credits in README.md)
    """
    tri = f"{Colors.yellow}▲"
    big_tri = []
    for i in range(1, 21, 2):
        big_tri.append(" "*int((19-i)/2) + tri*i + " "*int((19-i)/2))
    for t1 in big_tri:
        print(" "*10 + t1 + " "*10)
    for t2 in big_tri:
        print(t2 + " " + t2)

    print(f"{Colors.cyan} Hey, listen! These golden triangles possess mystical powers...")
    print(f"{Colors.default} Would you like to play MasterCode? ('Y' to play, 'N' to return to the menu)")


# You Win! graphic function
def you_win():
    """
    Displays a 'You Win!' graphic when the player wins
    """
    print(f"""
       {Colors.green}██╗   ██╗ ██████╗ ██╗   ██╗{Colors.white}
    .  {Colors.green}╚██╗ ██╔╝██╔═══██╗██║   ██║{Colors.white}    0
   / \  {Colors.green}╚████╔╝ ██║   ██║██║   ██║{Colors.white}    8
   | |   {Colors.green}╚██╔╝  ██║   ██║██║   ██║{Colors.white} `--8--'
   | |    {Colors.green}██║   ╚██████╔╝╚██████╔╝{Colors.white}   |:|
   |.|    {Colors.green}╚═╝    ╚═════╝  ╚═════╝{Colors.white}    |:|
   |.|                               |.|
   |:|   {Colors.green}██╗    ██╗██╗███╗   ██╗██╗{Colors.white}  |.|
   |:|   {Colors.green}██║    ██║██║████╗  ██║██║{Colors.white}  | |
 `--8--' {Colors.green}██║ █╗ ██║██║██╔██╗ ██║██║{Colors.white}  | |
    8    {Colors.green}██║███╗██║██║██║╚██╗██║╚═╝{Colors.white}  \ /
    O    {Colors.green}╚███╔███╔╝██║██║ ╚████║██╗{Colors.white}   .
          {Colors.green}╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝{Colors.default}
    """)


# Game Over graphic function
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
               ░{Colors.default}
    """)
