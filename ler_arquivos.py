def ler_arquivos():
    with open ('alunos.txt', 'r') as arquivo:
        for linha in arquivo:
            print(linha)
