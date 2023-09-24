
import pygame
import random

pygame.init()

# Paramètres du jeu
largeur_fenetre = 400
hauteur_fenetre = 500
taille_case = 25
vitesse_chute = 1

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
couleurs_pièces = [(0, 255, 255), (255, 0, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255), (128, 0, 128)]

# Formes des pièces
tetrominos = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

# Classe pour les pièces
class Piece:
    def __init__(self, x, y, forme):
        self.x = x
        self.y = y
        self.forme = forme
        self.couleur = random.choice(couleurs_pièces)
        self.rotation = 0

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Tetris")

# Fonction pour dessiner la grille
def dessiner_grille():
    for y in range(hauteur_fenetre // taille_case):
        for x in range(largeur_fenetre // taille_case):
            pygame.draw.rect(fenetre, blanc, (x * taille_case, y * taille_case, taille_case, taille_case), 1)

# Fonction pour dessiner une pièce
def dessiner_piece(piece):
    for y, ligne in enumerate(piece.forme[piece.rotation]):
        for x, case in enumerate(ligne):
            if case:
                pygame.draw.rect(fenetre, piece.couleur, (piece.x + x * taille_case, piece.y + y * taille_case, taille_case, taille_case))




print(15)            
