import csv

def readCSV(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    print(header)
    for row in reader: 
      iterable = zip(header, row) #arreglo de tuplas
      #print('***'*5)
      #print(list(iterable))
      #generar el diccionario con Dictionary Comprehension
      countryDict = {key: value for key, value in iterable}
      data.append(countryDict)
    return data

if __name__ == '__main__':
  data = readCSV(r'./app/population.csv')
  print(data[0])
  

