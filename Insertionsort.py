import csv
import sys 

with open('MOCK_DATA.csv') as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_reader.__next__()

    for i in csv_reader: 
     
        min_idx = i 
        for j in csv_reader: 
            if [min_idx] > [j]: 
                min_idx = j 
                          
        [i], [min_idx] = [min_idx], [i] 
  
 
    for row in csv_reader:
        print( row[0] + ', ' + row[1] + ', ' + row[2] )
