# ------------------------------
# ruby code
# ------------------------------

# require 'ostruct'
#
# city = OpenStruct.new(
#   name: 'Rivendell',
#   population: 100,
#   region: 'Eriador'
# )
#
# city.name # Rivendell
# city.population # 100
# city.region # Eriador

# ------------------------------
# python code
# ------------------------------
from collections import namedtuple

City = namedtuple('City', [
  'name',
  'population',
  'region'
])

print(type(City))
# <class 'type'>

city = City('Rivendell', 100, 'Eriador')
print(type(city))
# <class '__main__.City'>

print(city.name) # Rivendell
print(city.population) # 100
print(city.region) # Eriador
