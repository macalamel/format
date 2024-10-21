class Erreur:
    def check_type(self, var, _type) -> bool:
        """
        fonction qui vérifie le type de la variable

        #input: la variable a tester, son type attendu
        #output: bool 
        """
        return type(var)==_type
    
    def check_input(self, data) -> None:

        for i in data:
            if not self.check_type(i[0],i[1]):
                self.error(f"erreur de type sur une variable")
    
    def error(self, type: str) -> None:
        """
        fonction pour la gestion d'erreur
        #input: type de l'erreur (srt)
        #output: None
        """
        print(f"Error: {type} \nfin du programme...")
        exit()
        return None
    
if __name__=="__main__":
    test=10
    Erreur().check_input([[test,str]])