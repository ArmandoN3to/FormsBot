class FormsBase:
    def __init__(self,cpf,nome,data_nascimento):
        self.__cpf =cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self,novo_cpf):
        self.__cpf = novo_cpf
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome 

    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self,novo_data_nascimento):
        self.__data_nascimento = novo_data_nascimento 
    
    def preencher_forms(self):
        return print(f'nome: {self.nome} cpf: {self.cpf} data de nascimento: {self.data_nascimento}')




    
