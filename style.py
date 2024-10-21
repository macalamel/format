from unicodedata import name
from erreur import Erreur

class Style:
    def __init__(self, texte: str, italique: bool=False, bold: bool=False, underline: bool=False) -> None:
        Erreur().check_input([[texte, str],
                            [italique, bool],
                            [bold, bool],
                            [underline, bool]])
        self.dico={'\033[3m':italique,
              '\033[1m': bold,
              '\033[4m':underline}
        
        self.texte=format(texte)
        
        
    def format(self,text):
        texte_format=""
        for k,v in self.dico.items():
            if v:
                texte_format+=k
        return 
    
    def __str__(self) -> str:
        return self.texte

if __name__=="__main__":
    test="ceci est un texte a formater"
    print(Style(test,bold=True))