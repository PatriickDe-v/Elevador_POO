class Elevador:
    def __init__(self) -> None:
        self.__andar = 1 

    def locomover(self, andar): 
        if (andar < 1 or andar > 15): return self.__mensagem_de_erro()
        else: 
            return self.__alterar_andar_e_retornar_informacao(andar)

    def __alterar_andar_e_retornar_informacao(self, andar):
        self.__andar = andar
        if (andar == 1): return self.__mensagem_de_alteracao_para_terreo()
        return self.__transitar_andares()

    def __mensagem_de_erro(self,): 
        return (f'Andar incorreto! Elevador no {self.__andar}° andar') 

    def __transitar_andares(self):
        return (f'Elevador indo para o {self.__andar}° andar')

    def __mensagem_de_alteracao_para_terreo(self):
        return 'Elevador indo para o térreo'