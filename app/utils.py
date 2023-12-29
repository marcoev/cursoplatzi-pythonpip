'''
def getPopulation():
  keys = ['col', 'bol']
  values = [300, 400]
  return keys, values

'''
def getPopulation(countrydict):
  populationDict = {
    '2022': int(countrydict['2022 Population']),
    '2020': int(countrydict['2020 Population']),
    '2015': int(countrydict['2015 Population']),
    '2010': int(countrydict['2010 Population']),
    '2000': int(countrydict['2000 Population']),
    '1990': int(countrydict['1990 Population']),
    '1980': int(countrydict['1980 Population']),
    '1970': int(countrydict['1970 Population']),
  }
  labels = populationDict.keys()
  values = populationDict.values()
  return labels, values

def populationByCountry(data, country):
  result = list(filter(lambda item: item['Country'] == country, data ))
  return result
