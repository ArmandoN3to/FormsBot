from modules.formsBase import FormsBase

class FormContato(FormsBase):
    def __init__(self, cpf, nome, data_nascimento,telefone,celular, email:str):
        self.telefone = telefone
        self.celular = celular
        self.email =email
        super().__init__(cpf, nome, data_nascimento)
    
    def preencher_forms(self):
        return print(f'nome: {self.nome}\n cpf: {self.cpf}\n data de nascimento: {self.data_nascimento}\n Telefone: {self.telefone} \nCelular: {self.celular} \nEmail: {self.email}\n')