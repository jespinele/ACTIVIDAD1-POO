class Edades:
  @staticmethod
  def calcular_edadalberto(edjuan):
    return (2 * edjuan)/3
  @staticmethod
  def calcular_edadana(edjuan):
    return (4 * edjuan) / 3
  @staticmethod
  def calcular_edadmama(edjuan,edadalberto,edadana):
    return edjuan + edadalberto + edadana
  
edjuan = float(input("Ingrese la edad de Juan "))
edadalberto = Edades.calcular_edadalberto(edjuan)
edadana = Edades.calcular_edadana(edjuan)
edadmama = Edades.calcular_edadmama(edjuan,edadalberto,edadana)
print (f"la edades son: Alberto = {edadalberto:.2f}, Juan = {edjuan:.2f}, Ana = {edadana:.2f}, Mamá = {edadmama:.2f}" )



