from formsbase import FormsBase

class Login(FormsBase):
    def __init__(self, cpf, nome, data_nascimento,login,senha):
        self.login = login
        self.__senha = senha
        super().__init__(cpf, nome, data_nascimento)

    def fazer_login(self):
        pass
    
    
