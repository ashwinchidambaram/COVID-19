import csv
import os

dataDirectoryPath = '/Users/ashwinc 1/github/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports'
dataFileHead = '/Users/ashwinc 1/github/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/'
directory = os.fsencode(dataDirectoryPath)
writeFile = 'compiledData.csv'

header = []
data = []

for file in os.listdir(directory):

    fileName = os.fsdecode(file)

    if fileName.endswith(".csv"):

        readFile = dataFileHead + fileName

        # Reading csv file
        with open(readFile, 'r') as csvfile:

            # Creating new csv reader object
            csvreader = csv.reader(csvfile)

            # Get old fields and store to disposal array
            header = csvreader.__next__()

            # Extract data row by row from csv file
            for row in csvreader:

                if row[0] == ' ':

                    row[0] == 'NA'

                elif row[1] == ' ':

                    row[1] == 'NA'

                for x in range(3,5):

                    row[x] == 0

                    if row[3] == 0 and row[4] == 0 and row[5] == 0:
                        csvreader.__next__()

                    else:
                        data.append(row)

        # Write to compiledData.csv
        with open(writeFile, 'w') as csvfile:

            # Create new csv writer object
            csvwriter = csv.writer(csvfile)

            # Write updated fields row to new csv file
            csvwriter.writerow(header)

            # Write all data to compiledData.csv
            csvwriter.writerows(data)

    else:
        pass

#directory = os.path.join("c:\\","/Users/ashwinc 1/github/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports")
#for root,dirs,files in os.walk(directory):
#    for file in files:
     #  if file.endswith(".csv"):
    #       f=open(file, 'r')

    #       print(num(files))

          # f.close()
#
