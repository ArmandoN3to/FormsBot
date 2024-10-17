from modules.formsBase import FormsBase

class FormContato(FormsBase):
    def __init__(self, cpf, nome, data_nascimento,telefone,celular, email:str):
        self.telefone = telefone
        self.celular = celular
        self.email =email
        super().__init__(cpf, nome, data_nascimento)
    
    def preencher_forms(self):
        return print(f'nome: {self.nome} cpf: {self.cpf} data de nascimento: {self.data_nascimento} Telefone: {self.telefone} Celular: {self.celular} Email: {self.email}')