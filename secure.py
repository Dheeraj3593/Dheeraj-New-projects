from termcolor import cprint

secure=(('a','@'),("b","!"),("c","("),("d","4"),("e","%"),("f","-"),("g","~"),("h","]"),("i","("),("j",")"),("k","!"),('l','/'),('m','*'),('n','+'),("o","0"),("p","^"),
        ("q",'&'),("r","}"),("s","{"),("t","_"),("u",'='),("v",'?'),('w','.'),("x",'<'),('y',">"),("z",":"),('1','9'),('2','8'),('3','7'),('4','19'),('5','28'),('6','37'),('7','45'),('8','12'),('9','47'))

def secure_Password(password):
    for a,b in secure:
        password=password.replace(a,b)
    return password



cprint("#"*50)
cprint(("SECURE THE PASSWORD").center(50),"yellow")
cprint("#"*50)
user=input("Enter your password\n")
password_secured=secure_Password(user)
print("Your secures password is {}".format(password_secured))
