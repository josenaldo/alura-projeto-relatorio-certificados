from src.relatorio.certificado import Escola


class RelatorioPorEscola:

    def __init__(self, certificados):
        self.certificados = certificados

    def imprime(self):
        dados = self.executa()

        print("=" * 80)
        print("Cursos por escola".center(80, "-"))
        print("=" * 80)

        print(f"ALURA: {dados['ALURA']}")
        print(f"GRASSHOPER: {dados['GRASSHOPER']}")
        print("-" * 80)


    def executa(self):
        resultados = {}
        resultados["ALURA"] = self.__conta_certificado_por_escola("ALURA")
        resultados["GRASSHOPER"] = self.__conta_certificado_por_escola("GRASSHOPER")

        return resultados

    def __conta_certificado_por_escola(self, nome_da_escola):
        escola = Escola.escola_por_nome(nome_da_escola)

        certificados_por_escola = [c for c in self.certificados if c.escola == escola]

        return len(certificados_por_escola)
