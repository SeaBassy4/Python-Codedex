class City: 
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

Hermosillo = City('Hermosillo', 'Mexico', 900000, ["Dogos Miami", "Plaza Centenario", "El Galerias"])
Kyoto = City('Kyoto', 'Japan', "idk", ["place1", "place2"])
print(vars(Hermosillo))
print(vars(Kyoto))