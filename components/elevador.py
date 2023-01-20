class Elevador:
    def __init__(self) -> None:
        self.__andar = 1 

    def locomover(self, andar): 
        ...

    def mensagem_de_erro(self, andar): 
        return (f'Andar incorreto! Elevador no {self.__andar}° andar') 

    