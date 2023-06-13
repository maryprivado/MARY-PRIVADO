nome = input('digite o nome do aluno: ')
cod = input('digete o codigo:' )
disci = input('digite o nome da disciplina:')

nota1= float(input(' digite a primeira nota: '))
nota2= float(input('digite a segunda nota: '))
nota3= float(input('digite terceira nota: '))
 
if nota1 > 10 or nota2 > 10 or nota3 > 10:
    print('nota invalida')
    

total= nota1 + nota2 + nota3

media = total/3

if total>=21:
    print('aprovado direto')

if total >= 15 and total < 21 and total <= 29.9:
        print('aluno de final')
        final= float(input('digite nota final: '))
        mediafinal= (media +final) /2
        if mediafinal>=5:
            print('aprovado na final!!!')
        else:
            print('aluno reprovado!!!')
            
if total < 15:
    print('reprovado direto!!!')
if total == 30:
        print('parabens nota maxima')
        
        print('nome do aluno:' ,nome)
        print('codigo do aluno:', cod)
        print('digite disciplina:', disci)