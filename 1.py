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

for Pos in range(len(Eingabe)): 

    if Eingabe[Pos] == "+": Rechenzeichen = "+"; Plus_pos.append(Pos+1) 
    
    if Eingabe[Pos] == "-": Rechenzeichen = "-"; Minus_pos.append(Pos+1)

    if Eingabe[Pos] == "/": Rechenzeichen = "/"; Durch_pos.append(Pos+1)
    
    if Eingabe[Pos] == "*": Rechenzeichen = "*"; Minus_pos.append(Pos+1)
    
    if Eingabe[Pos] == "(": Klammern_auf.append(Pos+1)

    if Eingabe[Pos] == ")": Klammern_zu.append(Pos+1)

# Fügt die einzelnen Listen zu einer zusammen 
if len(Plus_pos)  > 0: Liste_Rechenzeichen_gesamt += Plus_pos
if len(Minus_pos) > 0: Liste_Rechenzeichen_gesamt += Minus_pos
if len(Durch_pos) > 0: Liste_Rechenzeichen_gesamt += Durch_pos
if len(Mal_pos)   > 0: Liste_Rechenzeichen_gesamt += Mal_pos

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


def Rechenzeichen_vor_der_Klammer(vor_der_klammer):

    temp = vor_der_klammer
    temp = temp[len(temp)-1]

    if temp == "+": return "+"
    elif temp == "-": return "-"
    elif temp == "/": return "/"
    elif temp == "*": return "*"

    else: raise SyntaxError("Kein Rechenzeichen vor der Klammer")
    

# Tested ob die Klammern richtig gesetzt sind
def Klammer_test(Klammern_liste_auf,Klammern_liste_zu,Liste_Rechenzeichen_gesamt):

    # Tested auf Syntax fehler in der Klammersetzung    

    # Gibt es Klammer in der Eingabe
    if len(Klammern_liste_auf)> 0 or len(Klammern_liste_zu) > 0:

        temp1 = Klammern_liste_auf
        temp2 = Klammern_liste_zu

        # Sind gleich viele Klammer auf, wie zu in der Eingabe enthalten
        if len(temp1) == len(temp2):

            if len(Liste_Rechenzeichen_gesamt) > 0: 

                # Tested ob ein Rechenzeichen vor der Klammer steht
                for index in Liste_Rechenzeichen_gesamt:

                    if index+1 in Klammern_liste_auf: return False
                    
                    else: return "Syntaxerror: Es steht kein Reichenzeichen vor der Klammer"

                

            for index in range(len(temp1)):

                # Test auf korrekte Stellung der Klammern                
                if (temp1[index]) >= temp2[index]-1: return "Syntaxerror: Die Klammer wurden Falsch gesetzt"
                   
                else: 
                    
                    for Zeichen in Rechenzeichen:

                        if temp1[index] > Zeichen > temp2[index]:
                            print("in der Klammer ist ein Rechenzeichen enthalten") 
        
        else: return False
 
    else: return False
    

def Eingabecutter(Anfang,Ende,Eingabe):

    ###
    # Zerlget die Eingabe in 3 teile,  1 vor, 1 in, 1 nach, der Klammer 
    ###
        
    inder_Klammer = ""

    for i in range(Anfang, Ende-1): inder_Klammer += Eingabe[i]

    vor_der_klammer = ""

    for i in range(Anfang-1):vor_der_klammer += Eingabe[i]

    nach_der_Klammer = ""

    for i in range(Ende,len(Eingabe)): nach_der_Klammer += Eingabe[i]

    return vor_der_klammer,inder_Klammer, nach_der_Klammer

# Tested ob zwischen den Rechenzeichen mit des ein anderes zeichen ist
def Syntax_test():

    temp =  Klammer_test(Klammern_auf, Klammern_zu, Liste_Rechenzeichen_gesamt)

    if temp == False: print("es ist eine Klammer enthalten")

    else:print(temp)

Syntax_test()
