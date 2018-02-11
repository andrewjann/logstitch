import re
import os
import zipfile

def logStitch():
    print('This is Andrew\'s Logstitch program!\n')

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
    else:
        #go through directory and find all appropriate files
        filtFiles = []
        for root, dirs, files in os.walk(dir):
            for i in range(len(files)):
                    if re.search('^'+log,files[i]) != None:
                        print(files[i])                       
                        with open(root + '/' + files[i]) as f:
                            print(f.read())
                        f.close()
                        filtFiles.append(files[i])
    filtFiles = sortFiles(filtFiles)
    return filtFiles, dir, log

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

def sortFiles(files):
    l = len(files)-1
    quicksort(files,0,l)
    return files

def quicksort(arr,low,high):
    if (low < high):
        pIndex = partition(arr,low,high)
        quicksort(arr,low,pIndex-1)
        quicksort(arr,pIndex+1,high)

def partition(arr,low,high):
    pVal = arr[low]
    pInd = low
    for i in range(low+1,high+1):
        if arr[i] < pVal:
            pInd += 1
            arr[i], arr[pInd] = arr[pInd], arr[i]
    arr[low], arr[pInd] = arr[pInd], arr[low]
    return pInd
        
    
    
##if __name__ == '__main__':
##    logStitch()
##    a = findFiles('b')

