import apache_beam as beam
import datetime 

input_file_path = r"C:\my_virtual_env\DE_class\apache_beam\sample.csv"
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
output_file_path = f"C:\\my_virtual_env\\DE_class\\apache_beam\\sample_output_{timestamp}.csv"

def incremental_func(element):
    try:
        return element *2
    except ValueError:
        return element

with beam.Pipeline() as pipeline:
    pcoll = pipeline | 'Read input ' >> beam.io.ReadFromText(input_file_path)
    trasformation = pcoll | " Incremental values  " >> beam.Map (incremental_func)
    output = pcoll | "Write output " >> beam.io.WriteToText("output_path")

    
