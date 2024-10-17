from modules.formsBase import FormsBase

class FormsLogin(FormsBase):
    def __init__(self, cpf, nome, data_nascimento,login,senha):
        self.login = login
        self.__senha = senha
        super().__init__(cpf, nome, data_nascimento)

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self,novo_senha):
        self.__senha = novo_senha

    def fazer_login(self,login,senha):
        if login == self.login and senha == self.senha:
            print("Login realizado com sucesso\n")
        elif login == self.login and senha!=self.senha or login != self.login and senha ==self.senha:
            print("Usuario ou senha estao errados\n")

        
        
    
