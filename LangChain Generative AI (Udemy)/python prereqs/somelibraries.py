import array
arr= array.array('i',[1,2,3,4])
print(arr)

import math
print(math.sqrt(4))
print(math.pi)

import random 
print(random.randint(1,10))
print(random.choice(['apple','banana','cherry']))

## File and Directory Access

import os
print(os.getcwd()) #current directory the file is in
# os.mkdir('test_dir') #make test directory (folder)

## High level operations on files and collections of files
import shutil

shutil.copyfile('C:/Users/jinwi/Programming Files/AI/LangChain Generative AI (Udemy)/shutilsource.txt', 'destination.txt')

## Data Serialization
import json
data = {'name':'Krish','age':25}
json_str = json.dumps(data) #convert a Python object into a JSON string
print(json_str)
print(type(json_str))

parsed_data = json.loads(json_str) #convert JSON string into a Pytho dictionary
print(parsed_data)
print(type(parsed_data))

## csv

import csv
with open('example.csv', mode='w', newline = '') as file: #newline = '' ensures \n, \r are read correctly
# ‘r’	Read (default)	Open a file for read only
# ‘w’	Write	Open a file for write only (overwrite)
# ‘a’	Append	Open a file for write only (append)
# ‘r+’	Read+Write	open a file for both reading and writing
# ‘x’	Create	Create a new file
    writer = csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['Krish',32])

with open('example.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

## datetime
from datetime import datetime, timedelta #timedelta --> change the time
now=datetime.now()
print(now)

yesterday = now-timedelta(days=1)
print(yesterday)

## time --> realtime, pauses, etc.
import time
print(time.time())
time.sleep(2)
print(time.time())

## regular expression
# check if matching strings
import re
pattern = r'\d+' 
# r'(\d+)' This is a Regular Expression pattern \d is a regex pattern for digit + is a regex pattern for at least (one or more) since they are enclosed in a ( ) that means the group that you want to capture
# checks a match for regex digits
text = 'There are 123 apples 456'
match = re.search(pattern, text)
print(match.group())

