import os
import re
import shutil

source = '/Users/micoo/OneDrive/Pictures'
target = '/Users/micoo/Downloads/SortedPictures'
EXTENSIONS = ["jpg", "png", "jpeg", "nov", "mp4"]
DATE_PATTERN = r".*(20\d\d)-?([01]\d)-?([0123]\d).*"

files = os.listdir(source)

def getFolder(year, monthNumber):
    if monthNumber == "01":
        monthFolder = "01 January"
    elif monthNumber == "02":
        monthFolder = "02 February"
    elif monthNumber == "03":
        monthFolder = "03 March"
    elif monthNumber == "04":
        monthFolder = "04 April"
    elif monthNumber == "05":
        monthFolder = "05 May"
    elif monthNumber == "06":
        monthFolder = "06 June"
    elif monthNumber == "07":
        monthFolder = "07 July"
    elif monthNumber == "08":
        monthFolder = "08 August"
    elif monthNumber == "09":
        monthFolder = "09 September"
    elif monthNumber == "10":
        monthFolder = "10 October"
    elif monthNumber == "11":
        monthFolder = "11 November"
    elif monthNumber == "12":
        monthFolder = "12 December"
    
    return year + "/" + monthFolder        



exclude_files = input("Name of files you do not want to be moved: ")

def files_not_to_be_moved(exclude_files):
    if exclude_files:
        remove_files = exclude_files.split(" ")
        for file in remove_files:
            if file in files:
                files.remove(file)
    return files

files = files_not_to_be_moved(exclude_files)

def get_date(file):
    match = re.match(DATE_PATTERN, file)
    if match:
        year = match.group(1)
        month = match.group(2)
        return {"year": year, "month": month}
    return None

for file in files:
    if file.lower().endswith(tuple(EXTENSIONS)):
        date = get_date(file)
        if date:
          year = date["year"]
          month = date["month"]        
          folder = getFolder(year, month)

          targetFolder = target + "/" + folder
          if not os.path.exists(targetFolder):
            os.makedirs(targetFolder)

          sourceFile = source + "/" + file
          targetFile = targetFolder + "/" + file
          if not os.path.exists(targetFile):
            shutil.move(sourceFile, targetFile)
        
          else:
            if os.stat(sourceFile).st_size == os.stat(targetFile).st_size:
                print("Duplicate file, deleting... " + file)
                os.remove(sourceFile)            
            else:
                print("Duplicate file, different size: " + file)
            
