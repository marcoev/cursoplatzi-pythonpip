import csv

'''
def readCSV(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') #aqui tenemos una lista y hay que convertirlo a un diccionario
    for row in reader: 
      print('***'*5)
      print(row)
'''

def readCSV(path):
  with open(path, 'r') as csvfile:
    #reader es un iterable
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    #print(header)
    for row in reader: 
      iterable = zip(header, row) #arreglo de tuplas
      #print('***'*5)
      #print(list(iterable))
      #generar el diccionario con Dictionary Comprehension
      #countryDict = {key: value for key, value in iterable}
      #otra opcion es la siguiente linea para crear el diccionario tomando el iterable como parametro
      countryDict = dict(iterable)
      data.append(countryDict)
    return data

if __name__ == '__main__':
  data = readCSV('./app/data.csv')
  print(data[0]) #imprimir solo el primero en el arreglo

