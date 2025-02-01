# Map : 
# map is a function applies a given function to each item is an Iterable (Like, a List tuple and ETC) And it's returns a new Iterable with resulst
#It is used in when you want to trasform the data in same way:

# Filter Operations:
# The filter function filters elemenets from an Iterable based on a function with returns there True or false. It only Keeps the elements for 
# which the function returns True.
# It is Used When you want to select or Filter specific data Based on the condition.
#To keep only the elements that match a specific condition.

import apache_beam as beam
from apache_beam.options.Pipeline_options import PipelineOptions

os.environ = path

gcs=gs://jbsuasnjds

options = PipelineOptions
p=beam.Pipeline(options=options)

sub_data= (
    p
    | " read from gcs" >> beam.io.ReadFromText(gcs_path, skip_header_lines=1)
    | ' print' >> beam.Map(print)

)

p.tun().wait_until_finish()