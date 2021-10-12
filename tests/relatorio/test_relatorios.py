from datetime import datetime

import pytest

from src.relatorio.certificado import FORMATO_DA_DATA, Certificado
from src.relatorio.leitor_de_certificados import LeitorDeCertificados
from src.relatorio.relatorios import RelatorioPorEscola


class TestRelatorio:
    
    @pytest.fixture
    def arquivos(self):
        return [
            "20210101_ALURA_CURSO 01.pdf",
            "20210102_ALURA_CURSO 02.pdf",
            "20210103_ALURA_CURSO 03.pdf",
            "20210104_ALURA_CURSO 04.pdf",
            "20210105_ALURA_CURSO 05.pdf",
            "20210106_ALURA_CURSO 06.pdf",
            "20210107_ALURA_CURSO 07.pdf",
            "20210108_ALURA_CURSO 08.pdf",
            "20210101_GRASSHOPER_CURSO 10.pdf",
            "20210101_GRASSHOPER_CURSO 20.pdf",
            "20210101_GRASSHOPER_CURSO 30.pdf",
            "20210101_GRASSHOPER_CURSO 40.pdf",
            "20210101_GRASSHOPER_CURSO 50.pdf",
            "20210101_GRASSHOPER_CURSO 60.pdf",
            "20210101_GRASSHOPER_CURSO 70.pdf",
            "20210101_GRASSHOPER_CURSO 80.pdf",
        ]

    @pytest.fixture
    def certificados(self, arquivos):
        leitor = LeitorDeCertificados("")
        certificados = leitor.cria_certificados(arquivos)
        return certificados

    def test_deve_retornar_certificados_por_escola(self, certificados):
        relatorio = RelatorioPorEscola(certificados)

        resultado = relatorio.executa()

        assert resultado["ALURA"] == 8
        assert resultado["GRASSHOPER"] == 8


