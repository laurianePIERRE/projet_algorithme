import random
import math

def generate_fich_points():
    """
    génère une liste de 20 points avec des coordonnées entières
    :return:
    """
    points = []
    with open("points_random.txt","w") as f:
        for i in range(0,20) :
            x = random.randint(0,100)
            y= random.randint(0,100)
            points.append((x,y))
            f.write(str(x)+","+str(y)+"\n")

def list_coordonnes(file) :
    cordonnees = []
    with open(file, 'r') as f :
        for line in f :
            x,y = map(int, line.strip().split(","))
            cordonnees.append((x,y))
    return cordonnees

def coordonnee_gauche(coordonnees) :
    # on initialise
    coordonnees_gauche = coordonnees[0]
    for coord in coordonnees:
        if coord[0] < coordonnees_gauche[0] :
            coordonnees_gauche=coord
    return coordonnees_gauche

def calcul_angle(A,B,pivot) :
    APivot=(pivot[0]-A[0],pivot[1]-A[1])
    PivotB = (B[0]-pivot[0],B[1]-pivot[1])
    print (APivot)
    print(PivotB)
    scal = APivot[0]*PivotB[0] +APivot[1]*PivotB[1]
    print (scal)
    inter= ((pivot[0]-A[0])**2,(pivot[1]-A[1])**2)
    distanceXPivot=math.sqrt((pivot[0]-A[0])**2+(pivot[1]-A[1])**2)
    print(inter)
    print (distanceXPivot)
    inter2 = ((pivot[0]-B[0])**2, (pivot[1]-B[1])**2)
    print (inter2)
    distanceYPivot = math.sqrt((pivot[0]-B[0])**2 + (pivot[1]-B[1])**2)
    print(distanceYPivot)
    cosangle = scal/(distanceXPivot*distanceYPivot)
    print(cosangle)
    angleXPivotY = math.acos(scal/(distanceXPivot*distanceYPivot))
    angle_degres = angleXPivotY*180/math.pi
    return angle_degres

#generate_fich_points()
coordonnees = list_coordonnes("points_random.txt")
print(coordonnees)
coordonnee_initiale = coordonnee_gauche(coordonnees)
print (coordonnee_initiale)
print(coordonnees[0])
print(coordonnees[1])
print(coordonnee_initiale)
print(calcul_angle(coordonnees[0],coordonnees[1],coordonnee_initiale))
