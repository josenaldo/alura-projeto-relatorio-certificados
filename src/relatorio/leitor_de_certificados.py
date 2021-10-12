import os
from datetime import datetime

from src.relatorio.certificado import Certificado, Escola


class LeitorDeCertificados:

    def __init__(self, diretorio_de_certificados):
        """Cria um leitor de certificados
        O leitor de certificados lê todos os certificados de um dado diretório, e monta uma lista de certificados
        a partir dos arquivos encontrados

        :param diretorio_de_certificados: diretório onde estão armazenados os certificados
        """
        self.__diretorio_de_certificados = diretorio_de_certificados

    @property
    def diretorio_de_certificados(self):
        return self.__diretorio_de_certificados

    @diretorio_de_certificados.setter
    def diretorio_de_certificados(self, value):
        self.__diretorio_de_certificados = value

    def lista_arquivos(self):
        caminho = self.diretorio_de_certificados
        arquivos = [arq for arq in os.listdir(caminho) if os.path.isfile(os.path.join(caminho, arq))]

        return arquivos

    def converte_arquivo_em_certificado(self, arquivo):
        partes = arquivo.split("_")
        data = datetime.strptime(partes[0], "%Y%m%d")
        escola = Escola.escola_por_nome(partes[1])
        titulo = os.path.splitext(partes[2])[0]

        return Certificado(data, escola, titulo)

    def cria_certificados(self, arquivos):
        certificados = []

        for arquivo in arquivos:
            certificado = self.converte_arquivo_em_certificado(arquivo)
            certificados.append(certificado)

        return certificados
