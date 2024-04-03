import random

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




#generate_fich_points()
list_coordonnes("points_random.txt")
