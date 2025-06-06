import sys
import os

# On ajoute le dossier courant à la liste des chemins de recherche Python
# pour que "from app import create_app" fonctionne dans les tests.
sys.path.insert(
    0,  # en première position
    os.path.abspath(os.path.dirname(__file__))  # chemin absolu du dossier du fichier courant
)

# Pourquoi on fait ça dans un projet ?
# Parce que les tests sont parfois dans un dossier à part (tests/), et Python ne sait pas remonter automatiquement vers app/
#
# Pour éviter ModuleNotFoundError
#
# Pour garder une structure propre sans déplacer les fichiers