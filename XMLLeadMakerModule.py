#parser 3

def makexml(custname,custnum):
    f1 = open('xml-template.txt','r')
    f2 = open('xml-lead.txt', 'w')
    checkWords = ("Chevrolet","Blazer","1999", "John Doe", "393-999-3922", "Acura of Bellevue")
    repWords = ("Chevy","Silverado 7500","2020",custname,custnum,"Store Name")
    for line in f1:
        for check, rep in zip(checkWords, repWords):
            line = line.replace(check, rep)
            #print(line)
        f2.write(line)
    f1.close()
    f2.close()
    with open('xml-lead.txt', 'r') as file:
        data = file.read()
    print(data)
    return data





if __name__=="__main__":
    makexml()
