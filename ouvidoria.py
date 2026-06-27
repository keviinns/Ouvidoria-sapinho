from operacoesbd import *

def inserir_comentario(conexao):
    categoria_da_mensagem = int(input("1- Sugestão \n2- Reclamação \n3- Elogio \nEscolha a categoria desejada: "))

    if categoria_da_mensagem == 1 or categoria_da_mensagem == 2 or categoria_da_mensagem == 3:

        titulo_do_comentario = input("Digite o titulo do assunto: \n")
        novo_comentario = input("Digite seu comentário: \n")
        if categoria_da_mensagem == 1:
            categoria = "Sugestão"
        elif categoria_da_mensagem == 2:
            categoria = "Reclamação"
        else:
            categoria = "Elogio"

        consulta = "insert into ouvidoria(categoria,titulo,comentario) values(%s,%s,%s);"
        dados = [categoria, titulo_do_comentario, novo_comentario]

        nova_solicitacao = insertNoBancoDados(conexao, consulta, dados)
        print("Comentário  adicionado com sucesso nº:", nova_solicitacao)
    else:
        print("Escolha um número válido!")

def quantidade_de_comentarios(conexao):
    consulta = "select count(*) from ouvidoria;"
    numero_de_mensagem = listarBancoDados(conexao, consulta)

    print(numero_de_mensagem[0][0], "- Mensagem(s) disponível(is)")

def listar_comentarios(conexao):
    consulta = "select * from ouvidoria"
    comentarios = listarBancoDados(conexao, consulta)

    if len(comentarios) > 0:
        print("Mensagens registradas na Ouvidoria")
        for intem in comentarios:
            print("- Código:", intem[0], "Categoria:", intem[1], "\nAssunto:", intem[2],
            "\nComentario:", intem[3])
    else:
        print("Sem mensagem disponível")

def pesquisar_pelo_codigo(conexao):
    codigo_da_pesquisa = int(input("Digite o código da mensagem: "))
    consulta = "select * from  ouvidoria where codigo = %s;"
    dados = [codigo_da_pesquisa]

    pesquisa = listarBancoDados(conexao, consulta, dados)

    if len(pesquisa) > 0:
        print("Mensagem encontrada \nCategoria:", pesquisa[0][1], "\nAssunto:", pesquisa[0][2], "\nMensagem:",
                  pesquisa[0][3])
    else:
        print("Sem mensagem para o código informado!")

def pesquisar_pela_categoria(conexao):
    pesquisar_categoria = int(input("1- Sugestão \n2- Reclamação cn3- Elogio \nEscolha a categoria de pesquisa desejada: "))

    if pesquisar_categoria == 1 or pesquisar_categoria == 2 or pesquisar_categoria == 3:

        if pesquisar_categoria == 1:
            categoria = "Sugestão"
        elif pesquisar_categoria == 2:
            categoria = "Reclamação"
        else:
            categoria = "Elogio"

        consulta = "select * from ouvidoria where categoria = %s;"
        dados = [categoria]

        comentarios = listarBancoDados(conexao, consulta, dados)

        if len(comentarios) > 0:
            print("Registros na Ouvidoria")
            for intem in comentarios:
                print("- Categoria:", intem[1], "Assunto:", intem[2], "\nComentario:", intem[3])
        else:
            print("Sem mensagens disponiveis!")

    else:
        print("Escolha um número válido!")

def atualizar_pelo_codigo(conexao):
    codigo_da_mensagem_atualizar = int(input("Digite o código mensagem: "))
    comentario_atualizado = input("Digite a nova mensagem: \n ")

    consulta = "update ouvidoria set comentario = %s where codigo = %s;"
    dados = [comentario_atualizado, codigo_da_mensagem_atualizar]

    atualizacao = atualizarBancoDados(conexao, consulta, dados)

    if atualizacao > 0:
        print("Comentário registrado com sucesso!")
    else:
        print("Código informado é inválido")

def excluir_pelo_codigo(conexao):
    excluir_comentario = int(input("Digite o código da mensagem: "))
    consulta = "delete from ouvidoria where codigo = %s;"
    dados = [excluir_comentario]

    linha_excluida = excluirBancoDados(conexao, consulta, dados)

    if linha_excluida > 0:
        print("Comentário excluído com sucesso!")
    else:
        print("Número de comentario não encontrado")