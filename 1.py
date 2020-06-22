print("Rechnung")

Eingabe = str(input())

Rechenzeichenpos = 0
Rechenzeichen = ""

for Pos in range(len(Eingabe)): 

    if Eingabe[Pos] == "+": Rechenzeichen = "+"
    
    if Eingabe[Pos] == "-": Rechenzeichen = "-"

    if Eingabe[Pos] == "/": Rechenzeichen = "/"
    
    if Eingabe[Pos] == "*": Rechenzeichen = "*"
    
   
    

def Plus():

    Term1,Term2 = Eingabe.split("+")

    Term1, Term2 = int(Term1),int(Term2)

    Ergebnis = Term1 + Term2

    print(Ergebnis)

def Minus():

    Term1, Term2 = Eingabe.split("-")

    Term1, Term2 = int(Term1), int(Term2)

    Ergebnis = Term1 - Term2

    print(Ergebnis)

def Mal():

    Term1, Term2 = Eingabe.split("*")

    Term1, Term2 = int(Term1), int(Term2)

    Ergebnis = Term1 * Term2

    print(Ergebnis)

def Durch():

    Term1, Term2 = Eingabe.split("/")

    Term1, Term2 = int(Term1), int(Term2)

    Ergebnis = Term1 / Term2

    print(Ergebnis)



if Rechenzeichen != "": 
    
    if Rechenzeichen == "+": Plus()

    if Rechenzeichen == "-": Minus()
    
    if Rechenzeichen == "/": Durch()

    if Rechenzeichen == "*": Mal()


else: print("kein Rechenzeichen enthalten")
