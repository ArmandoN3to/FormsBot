from modules.formContato import FormContato
from modules.formEndereco import FormEndereco
from modules.formLogin import FormsLogin

login = FormsLogin('060.445.262-40','Armando','02/02/2003','armando','1234')
login.preencher_forms()
endereco = FormEndereco('060.445.262-40','Armando','02/02/2003','69070120','Rio Branco','65','Educado','manacapuru')
endereco.preencher_forms()
contato = FormContato('060.445.262-40','Armando','02/02/2003','3232-1033',celular='99923-2932',email='emaildoarmando@hotmail.com')
contato.preencher_forms()