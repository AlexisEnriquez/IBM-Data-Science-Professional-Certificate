# Course 4
# Python for Data Science, AI & Development
# 09- Reading Files with Open

#Reading Files Python

#Download Data
import urllib.request
url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

# Download Example file
!wget -O /resources/data/Example1.txt https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt4

#Reading Text Files

# Read the Example1.txt
example1 = "Example1.txt"
file1 = open(example1, "r")

# Print the path of file
file1.name

# Print the mode of file, either 'r' or 'w'
file1.mode

# Read the file
FileContent = file1.read()
FileContent

# Print the file with '\n' as a new line
print(FileContent)

# Type of file content
type(FileContent)

# Close file after finish
file1.close()

#A Better Way to Open a File
# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed
file1.closed

# See the content of file
print(FileContent)

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars

# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()

# Print the first line
FileasList[0]

# Print the third line
FileasList[2]

#Exercise

##Download the file 

!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/ex4.csv

import matplotlib.pyplot as plt

statData ="ex4.csv"

def getNAvg(file,N):
    """
    file - File containting all the raw weather station data
    N - The number of days to compute the moving average over

    Return a list of containg the moving average of all data points
    """
    row = 0 # keep track of rows
    lastN = [] # keep track of last N points
    mean = [0] # running avg


    with open(file,"r") as rawData: 
        for line in rawData:
            if (row == 0): # Ignore the headers
                row = row + 1
                continue

            line = line.strip('\n')
            lineData = float(line.split(',')[1])

            if (row<=N): 
                lastN.append(lineData)
                mean[0] = (lineData + mean[0]*(row-1))/row
            else:
                mean.append( mean[row - N -1]+ (lineData - lastN[0])/N)
                lastN = lastN[1:]
                lastN.append(lineData)

            row = row +1            
        return mean

def plotData(mean,N):
        """ Plots running averages """
        mean = [round(x,3) for x in mean]
        plt.plot(mean,label=str(N) + ' day average')
        plt.xlabel('Day')
        plt.ylabel('Precipiation')
        plt.legend()

plotData(getNAvg(statData,1),1)
plotData ([0 for x in range(1,5)]+ getNAvg(statData,5),5 )
plotData([0 for x in range(1,7)] + getNAvg(statData,7),7)

#You can use the code below to verify your progress -