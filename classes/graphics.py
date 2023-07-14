from classes.colors import Colors

# main logo
def main_logo():
    """
    Displays the main logo for the game
    """
    print(f"""{Colors.blue}
     (__)
     [//]
     [\\\]         
     [//]        
  /\_[\\\]_/\     
 //__<()>__\\\    
/// \[/\]/ \\\\\     /\\\,/\\\,               ,              
\(   ||||   )/    /| || ||    _          ||              
     ||||         || || ||   < \,  _-_, =||=  _-_  ,._-_ 
     ||||         ||=|= ||   /-|| ||_.   ||  || \\\  ||   
     ||||        ~|| || ||  (( ||  ~ ||  ||  ||/    ||   
     ||||         |, \\\,\\\,  \/\\\ ,-_-   \\\, \\\,/   \\\,  
     ||||        _-
     ||||                   ,- _~.        |\        
     ||||                  (' /|           \\\         
     ||||                 ((  ||    /'\\\  / \\\  _-_ 
     ||||                 ((  ||   || || || || || \\\\
     ||||                  ( / |   || || || || ||/  
     ||||                   -____- \\\,/   \\\/  \\\,/ 
     \\\//
      \/                       
{Colors.default}\n""")

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
    tri = f"{Colors.yellow}▲"
    big_tri = []
    for i in range(1,21,2):
        big_tri.append(" "*int((19-i)/2) + tri*i + " "*int((19-i)/2))
    for t1 in big_tri:
        print(" "*10 + t1 + " "*10)
    for t2 in big_tri:
        print(t2 + " " + t2)