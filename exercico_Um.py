from ler_arquivos import ler_arquivos
from ler_dados import ler_dados
from criar_arquivo import criar_arquivo

if __name__ == '__main__':
        dados_alunos = ler_dados()
        criar_arquivo(dados_alunos = dados_alunos)
        ler_arquivos()
