class calcular:
    @staticmethod
    def valor_salbruto(horas_trabajadas,valor_hora):
        return horas_trabajadas * valor_hora
    @staticmethod
    def valor_retefuente(porcentaje_retefuente, salbruto):
        return porcentaje_retefuente * salbruto
    @staticmethod
    def porcentaje_retefuente(retefuente):
        return retefuente/100
    @staticmethod
    def valor_salneto(salbruto,valor_retefuente):
        return salbruto - valor_retefuente
horas_trabajadas = 48
valor_hora = 8000
retefuente = 12.5
salbruto = calcular.valor_salbruto(horas_trabajadas, valor_hora)
porcentaje = calcular.porcentaje_retefuente(retefuente)
valor_rete = calcular.valor_retefuente(porcentaje, salbruto)
salneto = calcular.valor_salneto(salbruto, valor_rete)
print(f"El salario bruto es: {salbruto}, El salario neto es: {salneto}, y la retencion en la fuente es del {retefuente}%")
