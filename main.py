import csv
import matplotlib.pyplot as plt

filename = 'data.csv'

population_per_continent = {}

with open(filename,'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for line in reader:
    continent = line['continent']
    year = line['year']
    population = line['population']
    
    if continent not in population_per_continent:
      population_per_continent["Africa"] = {'population':[], 'years':[]}
   
    population_per_continent[continent] ['population'].append(population)
    population_per_continent[continent] ['years'].append(year) 

plt.plot([2000, 2010, 2020, 2030], [100, 200, 300, 400], label="Europe", marker="o")
plt.plot([2000, 2010, 2020, 2030], [300, 200, 400, 600], label="Asia", marker="o")

plt.title("Internet Population per continent")
plt.xlabel("Year")
plt.ylabel("Internet users")
plt.grid(True)
plt.legend()

plt.show()