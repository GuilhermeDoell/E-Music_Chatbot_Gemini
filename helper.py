def carrega(nome_do_arquivo):
  try:
    with open(nome_do_arquivo, "rb") as arquivo:
      dados = arquivo.read()
      return dados
  except IOError as e:
    print(f"Erro ao carregar o arquivo: {e}")

def salva(nome_do_arquivo, conteudo):
  try:
    with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
      arquivo.write(conteudo)
  except IOError as e:
    print(f"Erro ao salvar o arquivo: {e}")