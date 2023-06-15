class Pessoa:
    #metodos. todos os metodos criados temos que fazer essa regra(self.+ o nome do metodo)
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
     
     #atribultos   
    def apresentar(self):
        print('Ola meu nome é:' ,self.nome)
        
    def envelhecer(self,anos):
        self.idade +=anos
        print('minha idade agora é:', self.idade)
    
    def mostrarcpf(self):
        print('Este é meu cpf: ', self.cpf)
        
        
#objeto criados:
pessoa1 = Pessoa('Rosimary', 29, '85746525384')
pessoa1.apresentar()
pessoa1.envelhecer(5)
pessoa1.mostrarcpf()

pessoa2 = Pessoa('Roberto', 65, 78945623145)
pessoa2.apresentar()
pessoa2.envelhecer(16)
pessoa2.mostrarcpf()