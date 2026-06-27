from ouvidoria import *

conexao = criarConexao("localhost", "root", "1664", "esquema")

while True:
    print(
        "OUVIDORIA! \n1) Inserir \n2) Quantidade de Comentário \n3) Listar \n4) Pesquisar com código \n5) Pesquisar por Categoria \n6) Atualizar com Código \n7) Excluir pelo Código \n8) Sair")
    opcao = int(input("Digite a opção desejada: "))
    print()

    if opcao == 1:
        inserir_comentario(conexao)
        print()

    elif opcao == 2:
        quantidade_de_comentarios(conexao)
        print()

    elif opcao == 3:
        listar_comentarios(conexao)
        print()

    elif opcao == 4:
        pesquisar_pelo_codigo(conexao)
        print()

    elif opcao == 5:
        pesquisar_pela_categoria(conexao)
        print()

    elif opcao == 6:
        atualizar_pelo_codigo(conexao)
        print()

    elif opcao == 7:
        excluir_pelo_codigo(conexao)
        print()

    elif opcao == 8:
        break

    else:
        print("Digite uma opção válida!")
        print()

encerrarConexao(conexao)
print("Obrigado por usar o app!")