#aqui se importa el archivo utils.py
import utils
import read_csv
import charts

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
  data = read_csv.readCSV('population.csv')
  #filtrar los datos para solo obtener el continente de Sudamerica
  data = list(filter(lambda item : item['Continent'] == 'South America', data))
  # Obtenemos una lista de paises
  countries = list(map(lambda item: item['Country'], data))
  # Obtenemos una lista del porcentaje de poblacion mundial
  percentages = list(map(lambda item: item['World Population Percentage'], data))
  charts.generatePieChart(countries, percentages)

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

