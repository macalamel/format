"""
Author: Martin Calamel
Created: 2024-10-08
Description: class pour gérer un affichage avec des couleurs
TODO: faire la class avec un dictionnaire et une fonction par couleur
"""

class Color:
    def __init__(self):
        """
        reset  : \033[
        
        gris   : \033[90m
        rouge  : \033[91m
        vert   : \033[92m
        jaune  : \033[93m
        D_bleu : \033[94m
        violet : \033[95m
        bleu   : \033[96m
        blanc  : \033[97m
        
        """
        self.reset = "\033[0m"

        self.gris = 'gris'
        self.red  = 'red'
        self.green   = 'green'
        self.yellow  = 'yellow'
        self.darkBlue = 'darkBlue'
        self.purple = 'purple'
        self.blue   = 'blue'
        self.white  = 'blanc'

        self.dico_color={"gris" : '\033[90m',
                         "red" : '\033[91m',
                         "green" : '\033[92m',
                         "yellow" : '\033[93m',
                         "darkBlue" : '\033[94m',
                         "purple" : '\033[95m',
                         "blue" : '\033[96m',
                         "white" : '\033[97m'}
    
    def is_color(self, color: str) -> bool:
        """
        fonction pour verifier si une couleur est disponible

        #input: nom de la couleur (str)
        #output: existence (bool)
        """
        return color in self.dico_color.keys()
    
    def error(self, type: str) -> None:
        """
        fonction pour la gestion d'erreur
        #input: type de l'erreur (srt)
        #output: None
        """
        print(self.dico_color[self.red]+f"Error: {type} \nfin du programme...{self.reset}")
        exit()
        return None

    
    def color(self, text: str,color: str = "blanc") -> str:
        """
        génère une chaîne de caractère qui permet un affichage coloré

        #input: texte a colorer (str), Nom de la couleur (str)
        #output: chaîne modifier
        """
        if self.is_color(color):
            return self.dico_color[color]+text+self.reset
        
        return self.error(f"Couleur {color} Inexistante")
    
    def _print(self, text: str, color: color) -> None:
        """
        fonction pour afficher une chaîne de caractère dans une certaine couleur

        #input: texte a afficher(str), couleur du texte(str)
        #output: None
        """
        print(self.color(text, color))
        
        return None

if __name__ == "__main__":
    c=Color()
    print(c.color("hey","yellow"))
    c._print('hey','bla')
    c._print('hey',"blue")