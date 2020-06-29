print("Rechnung")

Eingabe = str(input())

Rechenzeichenpos = 0
Rechenzeichen = ""

Plus_pos  = []
Minus_pos = []
Mal_pos   = []
Durch_pos = []
Klammern_auf = []
Klammern_zu = []
Liste_Rechenzeichen_gesamt = []

Errors = []

for Pos in range(len(Eingabe)): 

    if Eingabe[Pos] == "+": Rechenzeichen = "+"; Plus_pos.append(Pos+1) 
    
    if Eingabe[Pos] == "-": Rechenzeichen = "-"; Minus_pos.append(Pos+1)

    if Eingabe[Pos] == "/": Rechenzeichen = "/"; Durch_pos.append(Pos+1)
    
    if Eingabe[Pos] == "*": Rechenzeichen = "*"; Minus_pos.append(Pos+1)
    
    if Eingabe[Pos] == "(": Klammern_auf.append(Pos+1)

    if Eingabe[Pos] == ")": Klammern_zu.append(Pos+1)

# Fügt die einzelnen Listen zu einer zusammen 
Liste_Rechenzeichen_gesamt += Plus_pos
Liste_Rechenzeichen_gesamt += Minus_pos
Liste_Rechenzeichen_gesamt += Durch_pos
Liste_Rechenzeichen_gesamt += Mal_pos

# Sortiert die Liste aufsteigend
Liste_Rechenzeichen_gesamt.sort()


# Rechenoperation: Plus
def Plus(Term):

    Term1,Term2 = Term.split("+")

    Term1, Term2 = int(Term1),int(Term2)

    Ergebnis = Term1 + Term2

    print(Ergebnis)

# Rechenoperation: Minus
def Minus(Term):

    Term1, Term2 = Term.split("-")

    Term1, Term2 = int(Term1), int(Term2)

    Ergebnis = Term1 - Term2

    print(Ergebnis)

# Rechenoperation: Mal
def Mal(Term):

    Term1, Term2 = Term.split("*")

    Term1, Term2 = int(Term1), int(Term2)

    Ergebnis = Term1 * Term2

    print(Ergebnis)

# Rechenoperation: Durch
def Durch(Term):

    Term1, Term2 = Term.split("/")

    Term1, Term2 = int(Term1), int(Term2)

    Ergebnis = Term1 / Term2

    print(Ergebnis)

# Tested ob die Klammern richtig gesetzt sind
def Klammer_test(Klammern_liste_auf,Klammern_liste_zu,Liste_Rechenzeichen_gesamt):

    # Tested auf Syntax fehler in der Klammersetzung    

    # Gibt es Klammer in der Eingabe
    if len(Klammern_liste_auf)> 0 or len(Klammern_liste_zu) > 0:

        temp1 = Klammern_liste_auf
        temp2 = Klammern_liste_zu

        # Sind gleich viele Klammer auf, wie zu in der Eingabe enthalten
        if len(temp1) == len(temp2):

            for index in range(len(temp1)):

                # Test auf korrekte Stellung der Klammern                
                if (temp1[index]) >= temp2[index]-1: return True
                   
                else: return False
        
        else: return False
    
    else: return False
    







def Eingabecutter(Anfang,Ende,Eingabe):
        
    inder_Klammer = ""

    for i in range(Anfang, Ende-1): inder_Klammer += Eingabe[i]

    vor_der_klammer = ""

    for i in range(Anfang-1):vor_der_klammer += Eingabe[i]


    nach_der_Klammer = ""

    for i in range(Ende,len(Eingabe)): nach_der_Klammer += Eingabe[i]

    return vor_der_klammer,inder_Klammer, nach_der_Klammer











# Tested ob zwischen den Rechenzeichen mit des ein anderes zeichen ist
def Syntax_test(liste,Rechenzeichen):
    
    if len(liste) > 1:

        for Pos in liste:
        
            if Pos+1 or Pos-1 in liste: Errors.append((Rechenzeichen, Pos))


# Tested auf eventuelle Syntax Fehler
Syntax_test(Plus_pos,"+")
Syntax_test(Minus_pos,"-")
Syntax_test(Mal_pos,"*")
Syntax_test(Durch_pos,"/")


print(Klammer_test(Klammern_auf, Klammern_zu, Liste_Rechenzeichen_gesamt))

if Klammer_test(Klammern_auf, Klammern_zu,Liste_Rechenzeichen_gesamt) or len(Errors) > 0: print("Error")

    

else: 
    print("Keine Syntaxerror")
    try:
        print(Eingabecutter(Klammern_auf[0], Klammern_zu[0], Eingabe))
    except IndexError as e:
        print("der String enthält kein Klammer")
