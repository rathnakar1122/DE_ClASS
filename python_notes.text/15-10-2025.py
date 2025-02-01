#####################
 Date: 15-10-2024
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
append, extend, insert, index
index()	Returns the index of the first element with the specified value
list = [2, 1,2,3,4,1] # 1 index positions - 0, 4
in the place of 1 - I would like to insert 5 - 
index - returns the index of the first element occurance
list = [2, 1,2,3,4,1] # 1 index positions - 0, 4
result = list.index(1) # this transformation is transitive transformation
print(result)
# in the place of 1 - I would like to insert 5 - 
result1 = list.insert(result, 5) # it takes two input parameters - index-position, value to be inserted
print(result1) # insert method of list is intranstive
# the new value to be inserted will inserted in the position of index position you provide, and 
# the actual values to be replaced is moved to the next index-position


insert()	Adds an element at the specified position 
 
Apache Beam:
-------------
   
# cli: pip install 'apache-beam[gcp]'
 

beam.io methods: (Create)
--------------------------
['BeamJarExpansionService', 'BigQueryDisposition', 'BigQueryQueryPriority', 'BigQuerySink', 'BigQuerySource', 'ExternalTransform', 'FileBasedSink', 'GenerateSequence', 
'LexicographicKeyRangeTracker', 'MultipleReadFromPubSub', 'OffsetRangeTracker', 'OrderedPositionRangeTracker', 'PubSubSourceDescriptor', 'PubsubMessage', 'Read', 'ReadAllFromAvro', 'ReadAllFromAvroContinuously', 'ReadAllFromBigQuery', 'ReadAllFromParquet', 'ReadAllFromParquetBatched', 'ReadAllFromTFRecord', 'ReadAllFromText', 'ReadAllFromTextContinuously', 'ReadFromAvro', 'ReadFromBigQuery', 'ReadFromBigQueryRequest', 'ReadFromCsv', 'ReadFromJson', 'ReadFromMongoDB', 'ReadFromParquet', 'ReadFromParquetBatched', 'ReadFromPubSub', 'ReadFromTFRecord', 'ReadFromText', 'ReadFromTextWithFilename', 'ReadStringsFromPubSub', 'SCHEMA_AUTODETECT', 'Sink', 'TableRowJsonCoder', 'UnsplittableRangeTracker', 'Write', 'WriteResult', 'WriteStringsToPubSub', 'WriteToAvro', 'WriteToBigQuery', 'WriteToCsv', 'WriteToJson', 'WriteToMongoDB', 'WriteToParquet', 'WriteToParquetBatched', 'WriteToPubSub', 'WriteToTFRecord', 'WriteToText', 'Writer', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'avroio', 'aws', 'azure', 'concat_source', 'filebasedsink', 'filebasedsource', 'filesystem', 'filesystemio', 'filesystems', 'gcp', 'gcsio', 'hadoopfilesystem', 'iobase', 'localfilesystem', 'mongodbio', 'parquetio', 'range_trackers', 'restriction_trackers', 'textio', 'tfrecordio']


Programme 1:(Reading Data from inmemory source)
------------------------------------------------
import apache_beam as beam # batch + stream

'''
Apache Beam SDK for Python
Apache Beam provides a simple, powerful programming model for building both batch and streaming parallel data processing pipelines.

The Apache Beam SDK for Python provides access to Apache Beam capabilities from the Python programming language.
'''

# We are creating the input pcollection
# The possible input pcollection, we can create are -- Create Method - ReadFromBigQuery - ReadFromPubSub - ReadFromText
# The input pcollection creation depends on the source format - source

list = [1,2,3,4,4,5]
# it is inmemory data - data source - 
gcspath = 'gs://bucket/rawdata.csv' # it is not - in-memory data source - It is an External Source - 

# Then there is no requirement of exteranl udf creation

with beam.Pipeline() as pipeline:
    pcollection = pipeline | 'Creating input Pcollection' >> beam.Create(list)
    result = pcollection | 'printing' >> beam.Map(print) # it is for printing and debugging purpose
    

Programme 2:(Reading Data from EXTERNAL source)[GCS, S3, LOCAL]
----------------------------------------------------------------

import apache_beam as beam # batch + stream

'''
Apache Beam SDK for Python
Apache Beam provides a simple, powerful programming model for building both batch and streaming parallel data processing pipelines.
The Apache Beam SDK for Python provides access to Apache Beam capabilities from the Python programming language.
'''

# We are creating the input pcollection
# The possible input pcollection, we can create are -- Create Method - ReadFromBigQuery - ReadFromPubSub - ReadFromText
# The input pcollection creation depends on the source format - source 

# EXTERNAL SOURCE
gcspath = 'gs://gcp35batch/claims_invoices.csv' # it is not - in-memory data source - It is an External Source - 
localpath = r'D:\SuperGCPClasses\\gcp_de_demo\dataflow_jobs\\texfile.csv'
# Then there is no requirement of exteranl udf creation

with beam.Pipeline() as pipeline:
    pcollection = pipeline | 'Creating input Pcollection' >> beam.io.ReadFromText(gcspath, skip_header_lines=0)
    result = pcollection | 'printing' >> beam.Map(print)

+++++++
Error: 
+++++++
C:\Users\UMESH\AppData\Local\Programs\Python\Python312\Lib\site-packages\google\auth\_default.py:76: UserWarning: Your application has authenticated using end user credentials from Google Cloud SDK without a quota project. You might receive a "quota exceeded" or "API not enabled" error. 
See the following page for troubleshooting: https://cloud.google.com/docs/authentication/adc-troubleshooting/user-creds.
  warnings.warn(_CLOUD_SDK_CREDENTIALS_WARNING)
Traceback (most recent call last):
  File "d:\SuperGCPClasses\gcp_de_demo\dataflow_jobs\apache_beam\core_transformations\basic_beam.py", line 20, in <module>
    pcollection = pipeline | 'Creating input Pcollection' >> beam.io.ReadFromText(gcspath, skip_header_lines=0)
                                                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\UMESH\AppData\Local\Programs\Python\Python312\Lib\site-packages\apache_beam\io\textio.py", line 781, in __init__
    self._source = self._source_class(
                   ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\UMESH\AppData\Local\Programs\Python\Python312\Lib\site-packages\apache_beam\io\textio.py", line 140, in __init__
    super().__init__(
  File "C:\Users\UMESH\AppData\Local\Programs\Python\Python312\Lib\site-packages\apache_beam\io\filebasedsource.py", line 127, in __init__
    self._validate()
  File "C:\Users\UMESH\AppData\Local\Programs\Python\Python312\Lib\site-packages\apache_beam\options\value_provider.py", line 193, in _f  
    return fnc(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\UMESH\AppData\Local\Programs\Python\Python312\Lib\site-packages\apache_beam\io\filebasedsource.py", line 188, in _validate     
    match_result = FileSystems.match([pattern], limits=[1])[0]
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\UMESH\AppData\Local\Programs\Python\Python312\Lib\site-packages\apache_beam\io\filesystems.py", line 239, in match
    return filesystem.match(patterns, limits)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\UMESH\AppData\Local\Programs\Python\Python312\Lib\site-packages\apache_beam\io\filesystem.py", line 804, in match
    raise BeamIOError("Match operation failed", exceptions)
apache_beam.io.filesystem.BeamIOError: Match operation failed with exceptions {'gs://gcp35batch/claims_invoices.csv': Forbidden("GET https://storage.googleapis.com/storage/v1/b/gcp35batch/o/claims_invoices.csv?projection=noAcl&prettyPrint=false: bhaskargsbalina@gmail.com does not have storage.objects.get access to the Google Cloud Storage object. Permission 'storage.objects.get' denied on resource (or it may not exist).")}   

Required Permission:
--------------------
bhaskargsbalina@gmail.com does not have storage.objects.get access.


Program3: A small transformation:
----------------------------------
import apache_beam as beam # batch + stream

'''
Apache Beam SDK for Python
Apache Beam provides a simple, powerful programming model for building both batch and streaming parallel data processing pipelines.
The Apache Beam SDK for Python provides access to Apache Beam capabilities from the Python programming language.
'''

# We are creating the input pcollection
# The possible input pcollection, we can create are -- Create Method - ReadFromBigQuery - ReadFromPubSub - ReadFromText
# The input pcollection creation depends on the source format - source 

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