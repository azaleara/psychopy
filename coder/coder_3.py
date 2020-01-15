### Importar y exportar datos
## Example: saving your data

#!/usr/bin/env python
import csv
 
## Experiment Section, collect data here
data = [1, 0, 1, 1, 1, 0, 0, 1, 1]
 
## Closing Section
datafile = open("data.csv", "wb")
writer = csv.writer(datafile, delimiter=";")
for i, row in enumerate(data):
    writer.writerow([i, row])
datafile.close()


### importar
#!/usr/bin/env python
import csv
 
## Setup section, read experiment variables size and color from file
size = []
color = []
datafile = open("stimuli.csv", "rb")
reader = csv.reader(datafile, delimiter=";")
for row in reader:
    size.append(float(row[0]))
    color.append(row[1])
datafile.close()
 
## Experiment Section, use experiment variables here
for trial in range(len(size)):
    print("size = {}, color = {}".format(size[trial], color[trial]))