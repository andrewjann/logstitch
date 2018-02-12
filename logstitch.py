import re
import os
import zipfile

## TODO
## Generate a GUI
## Be able to access a ZIP file

def logStitch():
    print('This is Andrew\'s Logstitch program!\n')

## given the root folder directory and logtype will search for bluetooth or session logs
def findFiles(logType):
    if logType == 's':
        log = 'session'
    elif logType == 'b':
        log = 'bluetooth'
    else:
        raise ValueError('Invalid Input')
    
    dir = input('Enter the file directory below: ')
    if os.path.exists(dir) == False:
        raise NameError('Invalid Directory')
    elif zipfile.is_zipfile(dir) == True:
        with zipfile.ZipFile(dir) as unzip:
            unzip.extractall()
        dir = dir.replace(".zip","")
    #go through directory and find all appropriate files
    filtFiles = []
    for root, dirs, files in os.walk(dir):
        for i in range(len(files)):
                if re.search('^'+log+'(.*)'+'.dec$',files[i]) != None:             
                    filtFiles.append(files[i])
    return filtFiles, root, log

## generates text file with the list of files
def createLog(files,dir,log):
    os.chdir(dir)
    stitchLog = 'stitchLog_'+ log + '.txt'
    f_new = open(stitchLog,'w+'); f_new.close()
    for i in range(len(files)):
        print(files[i])
        with open(files[i]) as f:
            with open(stitchLog,'a') as f_new:
                for line in f:
                    f_new.write(line)
                f_new.write('\n')

## navigate to correct directory call quicksort function
def sortFiles(files,root):
    os.chdir(root)
    l = len(files)-1
    quicksort(files,0,l)
    return files

## quicksort algorithm
def quicksort(arr,low,high):
    if (low < high):
        pIndex = partition(arr,low,high)
        quicksort(arr,low,pIndex-1)
        quicksort(arr,pIndex+1,high)

## part of quicksort; opens first timestamp in each log file and sorts in chronological order
## future iteration: be able to handle duplicate files with different titles
def partition(arr,low,high):
    with open(arr[low]) as f:
        pVal = f.read(23)
    pInd = low
    for i in range(low+1,high+1):
        with open(arr[i]) as f:
            fileDate = f.read(23)
        if fileDate < pVal:
            pInd += 1
            arr[i], arr[pInd] = arr[pInd], arr[i]
    arr[low], arr[pInd] = arr[pInd], arr[low]
    return pInd
        
if __name__ == '__main__':
    logStitch()
    a,b,c = findFiles('s')
    sortFiles(a,b)
    createLog(a,b,c)
