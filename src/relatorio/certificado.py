from datetime import datetime


class Certificado:

    def __init__(self, data, escola, titulo):

        if(not isinstance(data, datetime)):
            raise ValueError("A data precisa ser do tipo datetime")

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
        return self.data.strftime("%d/%m/%Y")

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