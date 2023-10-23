def criar_arquivo (dados_alunos):
        with open ("alunos.txt", "w") as arquivo:
             for chave, valor in dados_alunos.items():
                  linha = f'{chave}:{valor}\n'
                  arquivo.write(linha)
