## READ DATA FROM TEXT we use ReadFromText beam io connecter ############
import apache_beam as beam
with beam.Pipeline() as Pipeline:
    lines = Pipeline | beam.io.ReadFromText("gs://mybucket_nameinput.csv")
    lines | 'PrintOutput' >>beam.Map(print)

# WriteToText beam.io connecter : used write data to text files 

import apache_beam as beam
with beam.Pipeline()as Pipeline:
    data=Pipeline | 'CreateData' >>beam.Create(['appale','banana','cherry'])
    transformed_data = data | 'ConvertToUpper' >> beam.Map(lambda word:word.upper())
    transformed_data | 'WriteTotext' ("gs://mybucket_name")

### ReadFromBigquery ###########
import apache_beam as beam
with beam.Pipeline() as pipeline:
    bq_data=pipeline | "ReadFromBigQuery" >> beam.io.ReadFromBigQuery(
        query='select * from my_dataset.my_table',use_startdard_sql=True
    )
    bq_data | 'PrintBQData' >>beam.MAp(print)

## WriteToBigquery table ##############
import apache_beam as beam
from apache_beam.io.gcp.bigquery import WriteToBigQuery

with beam.Pipeline() as pipeline:
    data=pipeline | 'CreateData' >> beam.Create([
        {"name":'john','age':28},
        {"name":"jane",'age':32}
    ])

    data | "WriteToBigquery" >> WriteToBigQuery(
        "my_dataset.Table_name",
        schema='name:string,age:INTEGER',
        write_disposition=beam.io.BigQueryDisposition.Write_APPEND,
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
    )


###  ReadFromPubSUb ##############
import apache_beam as beam
with beam.Pipeline() as pipeline:
    messages = pipeline | "ReadFromPubSub" >> beam.io.ReadFromPubSUb(topic='project/my_project/topic/subscribtion')
    messages | 'PrintMessages' >>beam.Map(print)


##WriteToPubSub #############
import apache_beam as beam

with beam.Pipeline() as pipeline:
    data=pipeline | 'CreateMessages' >> beam.Create(['message 1','Message 2'])
    data | 'WriteToPubSub' >> beam.io.WriteToPubSub(topic: "project/my_project/topics/mytopics")


