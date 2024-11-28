# 3rd party imports
import numpy as np


class Plate:
    """ Plate is a class that contain a (5, 5, 3) numpy array,
        a given score (manually calculated), a calculated score (default 0).
        The method calculate_point will calculate the score of the plate and
        store it the adequate variable.
    """

    # création d'une matrice de taille 5, 5, 3 remplie de 0,
    # avec des scores de 0
    matrice = np.zeros((5, 5, 3))
    score_given = 0
    score_calculated = 0

    # initialistaion de la matrice de la plate
    def __init__(self, matrice, score_given):
        self.matrice = matrice
        self.score_given = score_given

    def calculate_point(self):  # calcul des points de la matrice

        # Calcul des points par ligne
        point = 0
        for i in range(0, 5):
            if np.std(self.matrice[i, np.nonzero(self.matrice[i, :, 0]), 0]) == 0:
                point += self.matrice[i, np.nonzero(self.matrice[i, :, 0]), 0].sum()

        # Calcul des points par colonne
        for i in range(0, 5):
            if np.std(self.matrice[np.nonzero(self.matrice[:, i, 1]), i, 1]) == 0:
                point += self.matrice[np.nonzero(self.matrice[:, i, 1]), i, 1].sum()

        # Calcul des points par travers
        for i in range(-2, +3):
            if np.diagonal(self.matrice[:, :, 2], offset=0+i).sum() == np.diagonal(self.matrice[:, :, 2], offset=0+i)[0]*np.count_nonzero(np.diagonal(self.matrice[:, :, 2], offset=0 + i)):
                point += np.diagonal(self.matrice[:, :, 2], offset=0+i).sum()

        self.score_calculated = point


# 1st plate declaration
plate1_matrice = np.zeros((5, 5, 3), dtype=int)
plate1_matrice[0, 0:3, :] = [[7, 5, 8], [7, 1, 3], [7, 9, 3]]
plate1_matrice[1, 0:4, :] = [[2, 1, 4], [2, 9, 8], [2, 9, 4], [7, 5, 3]]
plate1_matrice[2, 0:5, :] = [[2, 1, 3], [6, 5, 3], [7, 9, 8], [2, 5, 3], [7, 1, 8]]
plate1_matrice[3, 1:5, :] =            [[2, 5, 4], [6, 9, 4], [6, 5, 8], [6, 1, 3]]
plate1_matrice[4, 2:5, :] =                       [[7, 5, 4], [2, 5, 8], [2, 1, 8]]
plate1_score = 84
plate1 = Plate(plate1_matrice, plate1_score)
plate1.calculate_point()

# 2nd plate declaration
plate2_matrice = np.zeros((5, 5, 3), dtype=int)
plate2_matrice[0, 0:3, :] = [[6, 2, 3], [9, 4, 5], [3, 4, 5]]
plate2_matrice[1, 0:4, :] = [[6, 7, 8], [9, 8, 7], [3, 4, 5], [3, 4, 5]]
plate2_matrice[2, 0:5, :] = [[8, 7, 8], [9, 8, 7], [3, 4, 5], [3, 4, 5], [3, 4, 5]]
plate2_matrice[3, 1:5, :] =            [[8, 7, 8], [9, 8, 7], [3, 4, 5], [3, 4, 5]]
plate2_matrice[4, 2:5, :] =                       [[2, 5, 4], [9, 2, 1], [3, 4, 5]]
plate2_score = 45
plate2 = Plate(plate2_matrice, plate2_score)
plate2.calculate_point()
