import matplotlib.pyplot as plt

def generateBarChart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generatePieChart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('./imgs/pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a','b','c']
  values = [100,200,30]
  # generateBarChart(labels, values)
  generatePieChart(labels, values)