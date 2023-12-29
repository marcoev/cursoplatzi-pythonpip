#aqui se importa el archivo utils.py
import utils
import read_csv
import charts
import pandas as pd

'''
data = [
  {
    'Country':'Colombia',
    'Population': 500
  },
  {
    'Country':'Bolivia',
    'Population': 300
  }
]
'''

def run():
  ''' 
  #filtrar los datos para solo obtener el continente de Sudamerica
  data = list(filter(lambda item : item['Continent'] == 'South America', data))
  # Obtenemos una lista de paises
  countries = list(map(lambda item: item['Country'], data))
  # Obtenemos una lista del porcentaje de poblacion mundial
  percentages = list(map(lambda item: item['World Population Percentage'], data))
  '''

  df = pd.read_csv('population.csv')
  df = df[df['Continent'] == 'Africa']
  countries = df['Country'].values
  percentages = df['World Population Percentage'].values

  charts.generatePieChart(countries, percentages)

  data = read_csv.readCSV('population.csv')

  country = input('Tye country => ')
  print(country)
  result = utils.populationByCountry(data, country)

  if len(result)>0:
    country = result[0]
    print(country)
    keys, values = utils.getPopulation(country)
    charts.generateBarChart(country['Country'], keys, values)

#  country = input('Type country => ')
#  print(result)

#le dice al archivo main.py que si es ejecutado desde la terminal, ejecute la funcion run
if __name__ == '__main__':
  run()

