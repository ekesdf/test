print("Rechnung")

Eingabe = str(input())

Rechenzeichenpos = 0
Rechenzeichen = ""

Plus_pos  = []
Minus_pos = []
Mal_pos   = []
Durch_pos = []



for Pos in range(len(Eingabe)): 

    if Eingabe[Pos] == "+": Rechenzeichen = "+"; Plus_pos.append(Pos+1) 
    
    if Eingabe[Pos] == "-": Rechenzeichen = "-"; Minus_pos.append(Pos+1)

    if Eingabe[Pos] == "/": Rechenzeichen = "/"; Durch_pos.append(Pos+1)
    
    if Eingabe[Pos] == "*": Rechenzeichen = "*"; Minus_pos.append(Pos+1)
    
   
    

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



# if Rechenzeichen != "": 
    
#     if Rechenzeichen == "+": Plus()

#     if Rechenzeichen == "-": Minus()
    
#     if Rechenzeichen == "/": Durch()

#     if Rechenzeichen == "*": Mal()


# else: print("kein Rechenzeichen enthalten")

Errors = []

def Syntax_test(liste,Rechenzeichen):
    
    for Pos in liste:

        if Pos+1 or Pos-1 in liste:
            Errors.append((Rechenzeichen, Pos))



Syntax_test(Plus_pos,"+")
Syntax_test(Minus_pos,"-")
Syntax_test(Mal_pos,"*")
Syntax_test(Durch_pos,"/")

print(Errors)