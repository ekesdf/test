print("Rechnung")

Eingabe = str(input())

Rechenzeichenpos = 0
Rechenzeichen = ""

Zahl = []
Plus_pos = []
Minus_pos = []
Mal_pos = []
Durch_pos = []
Klammern_auf = []
Klammern_zu = []
Liste_Rechenzeichen_gesamt = []

for Pos in range(len(Eingabe)):

    if Eingabe[Pos] == "+":
        Rechenzeichen = "+"
        Plus_pos.append(Pos+1)

    elif Eingabe[Pos] == "-":
        Rechenzeichen = "-"
        Minus_pos.append(Pos+1)

    elif Eingabe[Pos] == "/":
        Rechenzeichen = "/"
        Durch_pos.append(Pos+1)

    elif Eingabe[Pos] == "*":
        Rechenzeichen = "*"
        Minus_pos.append(Pos+1)
    
    elif Eingabe[Pos] == "(":
        Klammern_auf.append(Pos+1)

    elif Eingabe[Pos] == ")":
        Klammern_zu.append(Pos+1)
    
    else: Zahl.append(Pos+1)

# Fügt die einzelnen Listen zu einer zusammen
if len(Plus_pos) > 0:  Liste_Rechenzeichen_gesamt += Plus_pos
if len(Minus_pos) > 0: Liste_Rechenzeichen_gesamt += Minus_pos
if len(Durch_pos) > 0: Liste_Rechenzeichen_gesamt += Durch_pos
if len(Mal_pos) > 0:   Liste_Rechenzeichen_gesamt += Mal_pos

# Sortiert die Liste aufsteigend
Liste_Rechenzeichen_gesamt.sort()

# Rechenoperation: Plus
def Plus(Term):

    Term1, Term2 = Term.split("+")

    Term1, Term2 = int(Term1), int(Term2)

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

def Eingabecutter(Anfang, Ende, Eingabe):

    ###
    # Zerlget die Eingabe in 3 teile,  1 vor, 1 in, 1 nach, der Klammer
    ###

    inder_Klammer = ""

    for i in range(Anfang, Ende-1):
        inder_Klammer += Eingabe[i]

    vor_der_klammer = ""

    for i in range(Anfang-1): vor_der_klammer += Eingabe[i]

    nach_der_Klammer = ""

    for i in range(Ende, len(Eingabe)): nach_der_Klammer += Eingabe[i]

    return vor_der_klammer, inder_Klammer, nach_der_Klammer


def Rechenzeichen_test():

    temp = Liste_Rechenzeichen_gesamt

    if len(Mal_pos) > 0 :

        if Mal_pos[0] != 1 :
            
            if len(temp) > 1:

                for Zeichen in temp :
                    
                    if Zeichen > 1 and Zeichen < len(Eingabe):
                        
                        if Zeichen+1 in temp or Zeichen-1 in temp: return "Error"

        else: return "Error"

    elif len(Durch_pos) > 0:

            if Durch_pos[0] != 1:

                if len(temp) > 1:

                    for Zeichen in temp:

                        if Zeichen > 1 and Zeichen < len(Eingabe):

                            if Zeichen+1 in temp or Zeichen-1 in temp: return "Error"

            else: return "Error"
        
    elif len(temp) > 1:

            for Zeichen in temp:

                if Zeichen > 1 and Zeichen < len(Eingabe):

                    if Zeichen+1 in temp or Zeichen-1 in temp: return "Error"






















if Rechenzeichen_test() == "Error":

    print("die Rechenzeichen wurden falsch gesetzt")
