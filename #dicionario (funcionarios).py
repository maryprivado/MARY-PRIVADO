 #dicionario (funcionarios)
funcionarios = {}
#criando uma funcao para cadatrar os funcionarios
def cadastro_funcionario():
    nome= input("digite o nome do funcionario: ")
    idade= int(input('digite a idade do funcinario: '))
    cargo= input('digite o cargo deo funcionario: ')
    salario = float(input('dugite valor do salario do funcinario:'))
    
    #segundo dicionario criado
    funcionario = {
        'nome': nome,
        'idade': idade,
        'cargo': cargo,
        'salario': salario
    }
    #passando o mnome doa funcionarios para dentro do dicionario
    funcionarios[nome] = funcionario
    print('funcionario cadastrato com sucesso !')
    
    
#funcao para exibir os dados de um funcionario cadastrado
def exibir_funcionario():
    nome = input('digte nome do funcionario: ')
    if nome in funcionarios:
        funcionario = funcionario[nome]
        print('dados do funcionario: ')
        print('nome:' , funcionario[nome])
        print('idade:' , funcionario[idade])
        print('cargo:' , funcionario[cargo])
        print('salario:' , funcionario[salario])
    else:
        print('funcionario nao encontrado!')

#fucao para exibir todos os funcionarios cadastrados
def exibir_funcinarios():
    if funcionarios:
        print('lista de funcionarios: ')
        for nome, funcionario in funcionarios.items():
            print('nome:', funcionario['nome'])
            print('idade:' , funcionario['idade'])
            print('cargo;', funcionario['cargo'])
            print('salario:', funcionario['salario'])
            print('----------------------------------')
    else:
        print('nao ha funcionarios cadastratos')
        
#Funcao para remover um funcinario
def remover_funcionario():
    nome = input('digite o nome do funcionario! ')
    
    if nome in funcionarios:
        del funcionarios[nome]
        print('funcionario removido com sucesso! ')
    else:
        print('funcionario nao encontrado! ')

#Menu Pricipal
while True:
    print('\n=== sistema de cadastro de funcionarios ===')
    print('1 - Cadastro funcionarios ')
    print('2 - Exibir dados de um funcionario ')
    print('3 - Exibir todos os funcionarios cadastrados ')
    print('4 - Remover funcionario ')
    print('0 - Sair')
    
    opcao = input(' Digite a opcao desejada: ')
    
    if opcao == '1':
        cadastro_funcionario()
    elif opcao == '2':
        exibir_funcionario()
    elif opcao == '3':
        exibir_funcinarios()
    elif opcao == '4':
        remover_funcionario()
    elif opcao == '0':
        break
    else:
        print(' Opcao invalida! Digite novamente. ')
