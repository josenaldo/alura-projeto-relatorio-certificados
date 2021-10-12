from datetime import datetime

import pytest
from unittest.mock import patch

from src.relatorio.leitor_de_certificados import LeitorDeCertificados
from src.relatorio.certificado import Certificado

class TestLeitorDeCertificados:

    @pytest.fixture
    def diretorio_de_certificados(self):
        return "z:\\arquivos"

    @pytest.fixture
    def arquivos(self):
        return ["20210101_ALURA_CURSO 01.pdf",
                "20210630_ALURA_CURSO 02.pdf",
                "20211231_GRASSHOPER_CURSO 03.pdf"]

    @pytest.fixture
    def certificados_esperados(self):
        data_curso_1 = datetime.strptime("20210101", "%Y%m%d")
        data_curso_2 = datetime.strptime("20210630", "%Y%m%d")
        data_curso_3 = datetime.strptime("20211231", "%Y%m%d")

        return [
            Certificado(data_curso_1, "ALURA", "CURSO 01"),
            Certificado(data_curso_2, "ALURA", "CURSO 02"),
            Certificado(data_curso_3, "GRASSHOPER", "CURSO 03"),
        ]

    @patch("src.relatorio.leitor_de_certificados.os.listdir")
    @patch("src.relatorio.leitor_de_certificados.os.path.isfile")
    def test_leitor_de_certificados_deve_retornar_uma_lista_com_os_nomes_dos_arquivos_dos_certificados_de_um_diretorio(
            self, stub_de_isfile, stub_de_listdir, diretorio_de_certificados, arquivos ):
        stub_de_listdir.return_value = arquivos
        stub_de_isfile.return_value = True

        leitor = LeitorDeCertificados(diretorio_de_certificados)
        arquivos_de_certificados = leitor.lista_arquivos()

        assert arquivos_de_certificados == arquivos

    def test_leitor_deve_converter_lista_de_arquivos_em_lista_de_certificados(self, diretorio_de_certificados, arquivos, certificados_esperados):
        certificados = []

        leitor = LeitorDeCertificados(diretorio_de_certificados)
        certificados = leitor.cria_certificados(arquivos)
        assert certificados == certificados_esperados


    def test_leitor_deve_converter_o_nome_do_arquivo_em_um_certificado(self, diretorio_de_certificados, arquivos, certificados_esperados):
        leitor = LeitorDeCertificados(diretorio_de_certificados)
        certificado = leitor.converte_arquivo_em_certificado(arquivos[0])
        assert certificado == certificados_esperados[0]


