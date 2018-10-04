import os
_author_ = 'WilRs'

#Tem algumas coisas para corrigir -> Tem operaçoes que tao dando errp

def lista_pastas():
    #Imprime os arquivos contidos no pasta na tela.
    
    print(70 * '-')
    for num, pastas in enumerate(os.listdir(os.getcwd())):
        if os.path.isdir(pastas):
            print('{} {} {} {} Diretorio'.format(num,
                                                 ( 10 - len(str(num))) * '-',
                                                 pastas,
                                                 (45 - ( len(pastas) ) ) * '-'))
        else:
            print('{} {} {} {} Arquivo'.format(num,
                                                 ( 10 - len(str(num))) * '-',
                                                 pastas,
                                                 (45 - ( len(pastas) ) ) * '-'))
    print(70 * '-')

while True:
    lista_pastas()

    print()
    print('Você está em -> ', os.getcwd())
    print()

    print('''[ V ] para voltar um diretorio atraz.
[ A ] para ir até um diretorio.
[ S ] para sair do programa.
[ C ] para criar um diretorio.
[ Q ] para renomear um arquivo/diretorio.
[ R ] para remover um diretorio.
[ D ] para digitar um endereço.''') 

    print()    
    opcao = input('O que deseja fazer: ')

    if opcao in 'Ss':
        #Para a aplicaçao.
        
        break
    
    elif opcao in 'Vv':
        #Opçao para Voltar uma pasta.
        
        os.chdir( os.pardir )
        
    elif opcao in 'Aa':
        #Opçao para ir até outro diretorio.
        
        lista_pastas()

        print()
        ir = int(input('Digite o numero da pasta que deseja ir: '))
        os.chdir('./{}'.format(os.listdir(os.getcwd())[ir]))

    elif opcao in 'Cc':
        #Opçao para Criar um diretorio.
        
        nome = input('Digite o nome do diretorio: ')
        os.mkdir('{}'.format(nome))

    elif opcao in 'Rr':
        #Opçao remove um diretorio/arquivo.
        
        print()
        lista_pastas()
        remove = int(input('Digite o numero da pasta a ser removida: '))
        a_ser_removido = os.listdir(os.getcwd())[remove]
        
        try:
            if os.path.isdir( a_ser_removido ):
                os.rmdir('{}'.format( a_ser_removido ))
                print()
                print('{} REMOVIDO COM SUCESSO'.format( a_ser_removido ))
                print()
                
            else:
                os.remove ( a_ser_removido )
                print()
                print('{} REMOVIDO COM SUCESSO'.format( a_ser_removido ))
                print()
                
        except OSError:
           print('-------------------\nDEU ERRADO\n-------------------')

    elif opcao in 'Qq':
        #Opçao para renomear um diretorio/arquivo.
        
        lista_pastas()
        num = int(input('Digite o numero da pasta a ser renomeada: '))
        a_ser_renomeado = os.listdir(os.getcwd())[num]

        print('-->OBS: SE FOR UM ARQUIVO COLOQUE A EXTENÇAO')
        print('-->EX: MEUARQUIVO.TXT OU CARRINHO.RAR')
        nome = input('Digite o nome que voce quer: ')
        os.rename(a_ser_renomeado, nome)

    elif opcao in 'Dd':
        #Opçao de digitar o diretorio.
        print()
        print('EX: c:/MinhaPasta')
        endereco = input('Digite o endereço: ')
        os.chdir(endereco)
        
