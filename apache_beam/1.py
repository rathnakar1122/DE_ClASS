import apache_beam  as beam 
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from apache_beam.io import ReadFromText
from apache_beam.io import BigQuerySink
from google.cloud import storage,bigquery
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/45375853/Documents/cs_data_plotform/service_account/dbsr-pdtest-dev-svc-account.json'
os.environ['http_proxy'] = "http://googleapis-dev.gcp.cloud.uk.hsbc:3128"
os.environ['https_proxy'] = "http://googleapis-dev.gcp.cloud.uk.hsbc:3128"


class TransformData (beam.Dofn):
    def process (self, element):
        import csv 
        from io import StringIO
        #create a CSv file reader 
        reader = csv.DictReader (StringIO(element))
        # extract data from CSV yield as dictanary 
        for row in reader :
            yield{
                'id': int (raw['id']),
                'name' : row ['name'],
                'age': int (row['age'])
            }
def run (argv= None):
    pipeline_options = PipelineOptions (argv)
    pipeline_options.view_as (standaedOptions).runner = 'dataflowRunner'
    p = beam.Pipelie (options= options_options)

    #read csv from GCS 
    lines = (
        P
        | "read csv file " >> ReadFromText ("cs-df-events-poc/site-map/site_sample.csv")
    )
    # transform the data 
    transformed = (
        lines 
        | 'transform data ' >> beam.parDo(TransformData())        
    )
    #write data to Bigquery 
    transformed | ' write to bigquery ' >> beam.io.WriteToBigQuery (
        table = "your project name and dataset name ",
        schema = 'id:INTEGER, name:STRING , age:INTEGER',
        write_disposition = beam.io.BigQueryDisposition.WRITE_TRUNCATE  #write_append
    )
    result = p.run ()
    result.wait_until_finish()
if __name__--'__main__' :
    run()