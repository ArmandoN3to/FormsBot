from modules.formsBase import FormsBase

class FormEndereco(FormsBase):
    def __init__(self, cpf, nome, data_nascimento,cep, rua, numero, bairro, cidade):
        super().__init__(cpf, nome, data_nascimento)
        self.__cep = cep
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade

    
    def preencher_forms(self):
        return print(f" Nome: {self.nome} \n Cpf: {self.cpf} \n Data nascimento: {self.data_nascimento} \n CEP: {self.__cep} \n Rua: {self.__rua} \n Número: {self.__numero} \n Bairro: {self.__bairro} \n Cidade: {self.__cidade}\n")
    

