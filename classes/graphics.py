
# main logo
def main_logo():
    print(f"""{Colors.yellow}
    
                      _             ___          _      
      /\/\   __ _ ___| |_ ___ _ __ / __\___   __| | ___ 
     /    \ / _` / __| __/ _ \ '__/ /  / _ \ / _` |/ _ \\
    / /\/\ \ (_| \__ \ ||  __/ | / /__| (_) | (_| |  __/
    \/    \/\__,_|___/\__\___|_| \____/\___/ \__,_|\___|
                                                    
{Colors.default}\n""")


# Triforce
def triforce():
    tri = f"{Colors.yellow}▲"
    big_tri = []
    for i in range(1,21,2):
        big_tri.append(" "*int((19-i)/2) + tri*i + " "*int((19-i)/2))
    for t1 in big_tri:
        print(" "*10 + t1 + " "*10)
    for t2 in big_tri:
        print(t2 + " " + t2)