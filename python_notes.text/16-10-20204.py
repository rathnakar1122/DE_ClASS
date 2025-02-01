#####################
 Date: 16-10-2024
#####################
+++++++++++++++++++++++++++ 
GCP Cloud Data Engineering:
+++++++++++++++++++++++++++
#################################
  Topic: (Apache Beam[Dataflow])
#################################  

+++++++
Agenda:
+++++++

Pre-Requisites:
---------------
Python - Data Types [list, tuple, set, dictionary, String] 
       - Classes [inheritancy] 
       
       
list:
    -- methods
    -- 11 methods
    --  
        Method	Description
         
        clear()	Removes all the elements from the list
        copy()	Returns a copy of the list
        count()	Returns the number of elements with the specified value 
        pop()	Removes the element at the specified position
        remove()	Removes the first item with the specified value
        reverse()	Reverses the order of the list
        sort()	Sorts the list
       
Deep Explanation:
-----------------
 
Apache Beam:
-------------
   
# cli: pip install 'apache-beam[gcp]'
 

beam.io connectors - methods: (Create) 
--------------------------
ReadFromText 
WriteToText
ReadFromBigQuery
WriteToBigQuery
ReadFromPubSub
WriteToPubSub


Programme 1 : A small transformation:
----------------------------------
import apache_beam as beam # batch + stream
 

# EXTERNAL SOURCE
gcspath = 'gs://gcp35batch/claims_invoices.csv' # it is not - in-memory data source - It is an External Source - 
localpath = r'D:\SuperGCPClasses\\gcp_de_demo\dataflow_jobs\\texfile.csv'
# Then there is no requirement of exteranl udf creation

def Printing(element): 
    print(element.split()[1][0:len(element.split()[1])-1]) 

with beam.Pipeline() as pipeline:
    pcollection = pipeline | 'Creating input Pcollection' >> beam.io.ReadFromText(localpath, skip_header_lines=1)
    transformation1 = pcollection | 'Name to be uppercased using UDF' >> beam.Map(Printing) 


input.csv file:
---------------

villager_id, name, age, pension
1, rajasekhar, 20, 3000
2, rani, 61, 3000



Ref Link:
---------
https://www.geeksforgeeks.org/string-slicing-in-python/


Programme_two:
---------------
We need to read a text file from local machine, and then we need to doing uppercase for the name column and then save the output to the local machine.




Questions:
-----------
1. What is range() function in python?

# importing functools for reduce()
list = range(5) # it generates the a series of integers right from 0 and to the n-1 value. The N in this case is 5.
for d in list:
    print(d)
    
    
textfile.csv

3 rows - 4 columns

len(columns) - 4 columns - N=4

1            | 0
rajasekhar   | 1
20           | 2
3000         | 3
1            | 0
rajasekhar   | 1
20           | 2
3000         | 3
1            | 0
rajasekhar   | 1
20           | 2
3000         | 3
1            | 0
rajasekhar   | 1
20           | 2
3000         | 3


2. What is string slicing?

string = 'rajasekhar,'

''' Removing comma '''
print(string)
print(string[::])
# String Slicing: [::] - [start:end:step]
# 1. Every Alternative Character to be printed
print(string[::2])
# 2. First 3 character to be printed
print(string[:3])
# 3. last character to be removed
print(string[:10])
# 4. It should work every input
print(string[:len(string)-1])


3. Programme to strip the last character for any given string

inputstring = str(input("Please eneter your name: "))

def strip_last_character(string):
    print(string[:len(string)-1])
    
strip_last_character(inputstring)


4. How to join an multiple elements of list, tuple and string?

['1,', 'rajasekhar,', '20,', '3000']
['2,', 'rani,', '61,', '3000']
['3,', 'Roja,', '34,', '5000']


input = ['1,', 'rajasekhar,', '20,', '3000']

def striping_last_unnecessory_character(list):
    emptylist = []
    for i in range(len(list)-1):
        print(list[i][:len(list[i])-1])
        emptylist.append(list[i][:len(list[i])-1])
        
    emptylist.append(list[len(list)-1]
                                                                            
    return emptylist

output = ['1', 'rajasekhar', '20', '3000']

result = striping_last_unnecessory_character(input)
print(result)


# Updated Version for the above script

input = ['1,', 'rajasekhar,', '20,', '3000']

def striping_last_unnecessory_character(list):
    emptylist = []
    for i in range(len(list)-1): 
        emptylist.append(list[i][:len(list[i])-1])
        
    emptylist.append(list[len(list)-1])
    
    return emptylist

output = ['1', 'rajasekhar', '20', '3000']

result = striping_last_unnecessory_character(input)
print(result)


5. What is the use of ''.join method?


output = ['1', 'rajasekhar', '20', '3000']

result = ",".join(output)
print(result)


6. One Beam Transformation programme:

import apache_beam as beam #  
 

# EXTERNAL SOURCE
gcspath = 'gs://gcp35batch/claims_invoices.csv' # it is not - in-memory data source - It is an External Source - 
localpath = r'D:\SuperGCPClasses\\gcp_de_demo\dataflow_jobs\\texfile.csv'
localoutputpath = r'D:\SuperGCPClasses\\gcp_de_demo\dataflow_jobs\\texfile_output.csv'
# Then there is no requirement of exteranl udf creation

def Eleminating_last_char(element): 
    # print(element.split()[1][0:len(element.split()[1])-1]) 
    row = element.split() # when you split any string object - it will create a list object by following delimeter space
    result = striping_last_unnecessory_character(row)
    output = ",".join(result)
    return output

def striping_last_unnecessory_character(list):
    emptylist = []
    for i in range(len(list)-1): 
        emptylist.append(list[i][:len(list[i])-1])
        
    emptylist.append(list[len(list)-1])
    
    return emptylist



with beam.Pipeline() as pipeline:
    pcollection = pipeline | 'Creating input Pcollection' >> beam.io.ReadFromText(localpath, skip_header_lines=1)
    transformation1 = pcollection | 'Name to be uppercased using UDF' >> beam.Map(Eleminating_last_char) 
    result = transformation1 | 'writing to the local path' >> beam.io.WriteToText(localoutputpath)
    
    
7. cloud export: Reading the data from local machine and storing it into gcs bucket after a single transformation.

import apache_beam as beam #  
 

# EXTERNAL SOURCE
gcspath = 'gs://gcp35batch/claims_invoices.csv' # it is not - in-memory data source - It is an External Source - 
gcspath2 = 'gs://gcp35batch/claims_invoices_output.csv' # it is not - in-memory data source - It is an External Source - 
localpath = r'D:\SuperGCPClasses\\gcp_de_demo\dataflow_jobs\\texfile.csv'
localoutputpath = r'D:\SuperGCPClasses\\gcp_de_demo\dataflow_jobs\\texfile_output.csv'
# Then there is no requirement of exteranl udf creation

def Eleminating_last_char(element): 
    # print(element.split()[1][0:len(element.split()[1])-1]) 
    row = element.split() # when you split any string object - it will create a list object by following delimeter space
    result = striping_last_unnecessory_character(row)
    output = ",".join(result)
    return output

def striping_last_unnecessory_character(list):
    emptylist = []
    for i in range(len(list)-1): 
        emptylist.append(list[i][:len(list[i])-1])
        
    emptylist.append(list[len(list)-1])
    
    return emptylist



with beam.Pipeline() as pipeline:
    pcollection = pipeline | 'Creating input Pcollection' >> beam.io.ReadFromText(localpath, skip_header_lines=1)
    transformation1 = pcollection | 'Name to be uppercased using UDF' >> beam.Map(Eleminating_last_char) 
    result = transformation1 | 'writing to the local path' >> beam.io.WriteToText(gcspath2)
