
class Matrice:

    def __init__(self,liste):
        self.liste = liste
        self.shape = self.__shape()
        self.row
        self.line

    def __shape(self):
        self.row = len(self.liste[0])
        self.line = len(self.liste)
        return (self.row, self.line)

    def ValueRow(self,x):
        listreturn = []
        for i in range((len(self.liste))):
            listreturn.append(self.liste[i][x])
        return listreturn

    def ValueLine(self, x):
        return self.liste[x]

    def Calcul(self, index:int, st: str, status: str):
        """ La Somme/Différence/Multiplication d'une ligne ou colonne"""

        line = self.ValueLine(index) if st == "line" else self.ValueRow(index)
        result = 1 if status == "mul" else 0

        for number in line:
            if status == "add":
                result += number
            elif status == "sub":
                result -= number
            elif status == "mul":
                result *= number

        return result

    def Average(self, index: int, st: str):
        """ Fait la moyenne d'une ligne ou colonne"""

        line = self.ValueLine(index) if st == "line" else self.ValueRow(index)
        result = self.Calcul(index, st, "add") / len(line)
        return round(result,2)

    def Identitaire(self):
        final_mat = []
        compteur = 0
        for i in range(self.shape[1]):
            final_mat.append([])
            for j in range(self.shape[0]):
                if j == compteur:
                    final_mat[i].append(1)
                else :
                    final_mat[i].append(0)
            compteur +=1
        return Matrice(final_mat)

    def __CheckShape(func):
        def inner(self,other):
            if type(other) == Matrice:
                if (other.shape != self.shape):
                    print("Les matrices sont de taille différentes")
                    return self
                return func(self,other)
        return inner

    @__CheckShape
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            self.__basicChange(other, 0)
        elif type(other) == Matrice:
            return self.__MatriceChange(other,True)


    @__CheckShape
    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            self.__basicChange(other,1)
        elif type(other) == Matrice:
            return self.__MatriceChange(other,False)


    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            self.__basicChange(other, 2)
        elif type(other) == Matrice:

            if self.row == other.line:

                finalList = []

                for i in range(self.line):
                    finalList.append([])
                    for j in range(self.row):
                        result = 0
                        line = self.ValueLine(i)
                        line2 = other.ValueRow(j)

                        for k in range(len(line)):
                            result += line[k] * line2[k]

                        finalList[i].append(result)

                return Matrice(finalList)

            else:
                print("Le nombre de colonnes de la première matrice doit correspondre au nombre de lignes de la deuxième matrice.")
                return self



    def __basicChange(self,x,state):

        for i in range(self.line):
            for j in range(self.row):
                if state == 0:
                    self.liste[i][j] += x
                elif state == 1:
                    self.liste[i][j] -= x
                else:
                    self.liste[i][j] *= x

    def __MatriceChange(self,x,state):
        finalListe = []
        for i in range(self.line):
            finalListe.append([])
            for j in range(self.row):
                if state:
                    finalListe[i].append(self.liste[i][j] + x.liste[i][j])
                else:
                    finalListe[i].append(self.liste[i][j] - x.liste[i][j])

        return Matrice(finalListe)


    def __str__(self):
        for liste in self.liste:
            print(liste)

        return ""


MatA = Matrice([
    [1,2,3,4,5,6],
    [1,2,3,5,5,6]
])
MatB = Matrice([
    [1,2,3,4,5,6],
    [5,5,5,5,5,5]
])
MatC = MatA - MatB

MatD = Matrice([
    [2,2,3],
    [5,6,8]
])

MatE = Matrice([
    [7,5,6],
    [22,9,5],
    [2,0,3]
])

print(MatE.Identitaire())

MatK = MatD * MatE

print(MatK)
print(MatK.Identitaire())