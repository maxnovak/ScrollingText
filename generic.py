import csv
import random
with open('text.txt', 'rb') as csvfile:
    directoryNames  = csv.reader(csvfile, delimiter = ' ', quotechar='|')
    items = []
    for item in directoryNames:
        items.append(item)
    print items
    for i in range(10):
        rand = random.randint(1,len(items)-1)
        rand1 = random.randint(1,len(items)-1)
        print ' '.join(items[rand]) + '/' + ' '.join(items[rand1])
