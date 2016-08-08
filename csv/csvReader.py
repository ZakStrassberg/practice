import csv
with open('us-500.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile)
    firstLine = True
    for row in reader:
        if firstLine:           # hacky workaround to skip first line, but
            firstLine = False   # it works pretty well so I'm not bothered
            continue
        print row[0], row[1]
        print "first_name:", row[0]
        print "last_name:", row[1]
        print "company_name:", row[2]
        print "address:", row[3]
        print "city:", row[4]
        print "county:", row[5]
        print "state:", row[6]
        print "zip:", row[7]
        print "phone1:", row[8]
        print "phone2:", row[9]
        print "email:", row[10]
        print "web:", row[11]
        print "--------------------"
