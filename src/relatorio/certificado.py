from datetime import datetime

FORMATO_DA_DATA = "%Y%m%d"

class Escola:

    def __init__(self, nome, data_de_matricula):
        self.__nome = nome
        self.__data_de_matricula = data_de_matricula

    def __eq__(self, other):
        return self.nome == other.nome and self.data_de_matricula == other.data_de_matricula

    def __repr__(self):
        return f"Escola(nome='{self.nome}' data_de_matricula='{self.data_de_matricula}')"

    @property
    def nome(self):
        return self.__nome

    @property
    def data_de_matricula(self):
        return self.__data_de_matricula

    @staticmethod
    def escola_por_nome(name):

        escolas = {
            "ALURA": Escola("ALURA", datetime.strptime("20210901", FORMATO_DA_DATA)),
            "GRASSHOPER": Escola("GRASSHOPER", datetime.strptime("20210901", FORMATO_DA_DATA)),
        }

        try:
            escola = escolas[name]
            return escola
        except KeyError as e:
            raise ValueError(f"Essa escola não existe: {name}")


class Certificado:

    def __init__(self, data, escola, titulo):

        if not isinstance(data, datetime):
            raise ValueError("A data precisa ser do tipo datetime")

        if not isinstance(escola, Escola):
            raise ValueError("A escola precisa ser do tipo Escola")

        self.__data = data
        self.__escola = escola
        self.__titulo = titulo

    def __eq__(self, other):
        return self.data == other.data and self.escola == other.escola and self.titulo == other.titulo

    def __repr__(self):
        return f"Certificado(data='{self.data_formatada}' escola='{self.escola}' titulo='{self.titulo}')"

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def data_formatada(self):
        return self.data.strftime(FORMATO_DA_DATA)

    @property
    def escola(self):
        return self.__escola

    @escola.setter
    def escola(self, value):
        self.__escola = value

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

        
class Relatorio:
    def __init__(self, certificados):
        self.certificados = certificados

    def cursos_por_escola(self):
        pass
