import sklearn
import csv

with open("immondizia e co.csv", newline="", encoding="ISO-8859-1") as filecsv:
    lettore = csv.reader(filecsv,delimiter=",")

    spazzaturaArr=[]
    save=""
    for row in lettore:
        
        spazzaturaArr.append(row[1])
    
    print(spazzaturaArr)