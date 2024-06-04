from operacoesbd import *
opcao = -1
con = criarConexao('127.0.0.1', 'root', '102030@eiUU', 'sistema_ouvidoria')
while opcao != 6:
  print("Opções \n1-Adicionar manifestação \n2-Consultar manifestações \n3-Relatório de manifestações \n4-Pesquisar manifestações \n5-Pesquisar manifestações por tipo \n6-Excluir manifestação \n7-Sair ")
  opcao = int(input("Digite a sua opção: "))

  if opcao == 1:
    nome = input("Digite o seu nome: ")
    manifestacao = input("Digite a sua manifestação: ")
    tipo = input("Digite o tipo da manifestação: ")

    consultaInsert = 'insert into ouvidoria (nome,manifestacao,tipo) values(%s,%s,%s)'
    dados = [nome, manifestacao, tipo ]

    insertNoBancoDados(con, consultaInsert, dados)
    print("Filme adicionado com sucesso!")

  elif opcao == 2:
    consultaListar = 'select * from ouvidoria'
    ouvidoria = listarBancoDados(con, consultaListar)

    if len(ouvidoria) == 0:
      print("Não há manifestações a serem exibidas!")
    else:
      print("Lista de Manifestações")
      for item in ouvidoria:
        print('Código:', item[0],'/ Manifestação:', item[2], '/ Categoria:', item[3])

  elif opcao == 3:
    quantidadeLista = 'select count(*) from ouvidoria'

    ouvidoria = listarBancoDados(con, quantidadeLista)

    numeroManifestacoes = ouvidoria[0][0]
    print("A empresa tem",numeroManifestacoes,"manifestações")

  elif opcao == 4:
    codigoPesquisa = int(input("Digite o código: "))

    consultaListar = 'select * from ouvidoria where id = ' + str(codigoPesquisa)
    ouvidoria = listarBancoDados(con, consultaListar)

    if len(ouvidoria) == 0:
      print("Não existe manifestação para o código informado")
    else:
      print("Manifestação Pesquisada:")
      for item in ouvidoria:
        print('Código:', item[0], '- Manifestação:', item[2], '- tipo:', item[3])

  elif opcao == 5:
    categoriaBuscada = input("Digite o tipo: ")
    consultaListar = "select * from ouvidoria where tipo = '" + categoriaBuscada + "'"
    ouvidoria = listarBancoDados(con, consultaListar)

    if len(ouvidoria) == 0:
      print("Não existem manifestações para o tipo informado")
    else:
      print("Lista de manifestações do tipo", categoriaBuscada)
      for item in ouvidoria:
        print('Código:', item[0], '- Manifestação:', item[2], '- Tipo:', item[3])

  elif opcao == 6:
    excluir = input("Digite seu código: ")

    excluirLista = 'delete from ouvidoria where id = %s'
    dados = [excluir]
    ouvidoria = excluirBancoDados(con, excluirLista, dados)
    print("Manifestação Excluída com Sucesso!")

  elif opcao != 7:
    print("Opção inválida!")

encerrarBancoDados(con)
print("Obrigado por usar o nosso sistema")