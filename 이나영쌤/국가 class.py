class Country:
  """Super Class"""
  def __init__(self, name, population, capital):
    self.name = name
    self.population = population
    self.capital = capital

  def show(self):
    print("""
          국가의 이름은 {} 입니다.
          국가의 인구는 {} 입니다.
          국가의 수도는 {} 입니다.
          """.format(self.name, self.population, self.capital)
    )

class Korea(Country):
  """Super Class"""
  def __init__(self, name, population, capital):
    self.name = name
    self.population = population
    self.capital = capital


country = Korea('한국', '1000명', '서울')
country.show()