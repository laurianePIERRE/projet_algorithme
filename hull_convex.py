import random
import math
import matplotlib.pyplot as plt
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


def axe_abscisse_point(point)  :
    """
    Détermine l'axe des abscisses par rapport à un point
    :param point:
    :return:
    """
    c = point[1]
    return c
def calcul_angle_abscisse(point, pivot):
    """
    Calcule de l'angle entre le point, le pivot et l'axe des abscisse
    :param point:
    :param pivot:
    :return:
    """

    # calcul du segment
    delta_x = point[0] - pivot[0]
    delta_y = point[1] - pivot[1]

    # gestion des exeptions
    if delta_x == 0:
        return math.pi / 2 if delta_y > 0 else -math.pi / 2
    elif delta_y == 0:
        return 0 if delta_x > 0 else math.pi
    c = axe_abscisse_point(pivot)

    # calcul de l'angle ( voir shéma)
    angle = math.atan((point[1] - c) / delta_x )

    # ajustement de l'angle dans le bon quadrant

    if delta_x < 0:
        angle += math.pi

    # angle en radian

    return angle



def trie_angle(coordonnees):
    order=[]
    # definir pivot
    pivot = coordonnee_gauche(coordonnees)
    order.append(pivot)
    # drop pivot in list
    coordonnees.remove(pivot)
    while coordonnees:
        angles = []
        for cordonnee in coordonnees:
            angle = calcul_angle_abscisse(cordonnee,pivot)
            angles.append((cordonnee,angle)) # on garde langle et la coordonnee associee
        # trie les angles
        angles.sort(key=lambda x:x[1])
        print("angles : ",angles)
        # on recupere la cordonnee avec l angle le plus faible
        next_point=angles[0][0]

        print("next_point :",next_point)
        order.append(next_point)
        # retrait du point utilis
        coordonnees.remove(next_point)
        pivot = next_point
    return order # liste des points composants envellope convexe

#generate_fich_points()
def plot_point_envellope():
    points = list_coordonnes("points_random.txt")
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    enveloppe_convexe = trie_angle(points)
    print(points)

    x_enveloppe = [point[0] for point in enveloppe_convexe]
    y_enveloppe = [point[1] for point in enveloppe_convexe]

    plt.scatter(x_coords, y_coords, color="blue")
    plt.plot(x_enveloppe + [x_enveloppe[0]], y_enveloppe + [y_enveloppe[0]], color="red")  # Fermer la forme géométrique

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Points et enveloppe convexe')
    plt.grid(True)

    # Afficher et sauvegarder le graphique
    plt.savefig('enveloppe_convexe.png')
    plt.show()

    print("Fichier créé: enveloppe_convexe.png")


coordonnees = list_coordonnes("points_random.txt")
print(coordonnees)
coordonnee_initiale = coordonnee_gauche(coordonnees)
print (coordonnee_initiale)
print(coordonnees[0])
print(calcul_angle_abscisse(coordonnees[0],coordonnee_initiale))
print(trie_angle(coordonnees))
plot_point_envellope()
0