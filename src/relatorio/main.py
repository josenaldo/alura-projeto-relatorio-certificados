from src.relatorio.leitor_de_certificados import LeitorDeCertificados

# Lê o diretório de certificados
leitor = LeitorDeCertificados('C:\\Users\\josen\\OneDrive\\certificados\\2021')
arquivos = leitor.lista_arquivos()
certificados = leitor.cria_certificados(arquivos)


for c in certificados:
    print(c)


# Pra cada arquivo, converte em um objeto Certificado
# Monta uma lista com os certificados da Alura
# Monta uma lista com os certificados grasshoper
# Monta um histórico com os certificados de cada escola
# Mostra relatório de cursos esperados e cursos completados