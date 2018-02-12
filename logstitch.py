import re
import os
import zipfile

## TODO
## Generate a GUI
## Be able to access a ZIP file

def hello():
    print('This is Andrew\'s Logstitch program!\n')

## given the root folder directory and logtype will search for bluetooth or session logs
def inputDir():

    inputFile = input('Enter the file directory: ')
    if os.path.exists(inputFile) == False:
        raise NameError('Invalid Directory')
    elif zipfile.is_zipfile(inputFile) == True:
        rootFolder = re.sub('[^\\\\]+$',"",inputFile)
        os.chdir(rootFolder)
        with zipfile.ZipFile(inputFile,"r") as unzip:
            unzip.extractall()
        inputFile = inputFile.replace(".zip","")
    return inputFile

#go through directory and find all appropriate files, then call sortFiles and createLog
def logstitch(dir,logType):

    if logType == 's':
        log = 'session'
    elif logType == 'b':
        log = 'bluetooth'
    else:
        raise ValueError('Invalid Input')

    filtFiles = []
    for root, dirs, files in os.walk(dir):
        for i in range(len(files)):
            if re.search('^'+log+'(.*)'+'.dec$',files[i]) != None:             
                filtFiles.append(files[i])
    
    sortFiles(filtFiles,root)
    createLog(filtFiles,root,log)

## generates text file with the list of files
def createLog(files,dir,log):
    os.chdir(dir)
    stitchLog = 'stitchLog_'+ log + '.log'
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
    hello()
    dir = inputDir()
    logstitch(dir,'s')
    logstitch(dir,'b')
