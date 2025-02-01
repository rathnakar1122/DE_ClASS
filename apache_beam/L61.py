import apache_beam as beam

word_list = ['apple', 'banana', 'cherry']

def eliminating_last_char(element):
    row = element.split()  # Split the row into a list of words
    result = striping_last_unnecessary_character(row)
    output = ",".join(result)
    return output

def striping_last_unnecessary_character(word_list):
    empty_list = []
    for i in range(len(word_list) - 1):
         empty_list.append(word_list[i][:-1])  # Remove the last character from each word
    empty_list.append(word_list[-1])  # Append the last word as it is
    return empty_list


with beam.Pipeline() as pipeline:
    pcoll = pipeline | "Read Input" >> beam.io.ReadFromText(word_list)
    transformation = pcoll | "Transformations" >> beam.Map(eliminating_last_char)
    result = transformation | "Write to Output" >> beam.io.WriteToText(print)


import apache_beam as beam
from apache_pipeline.options.pipeline_options import PipelineOptions 

with beam.Pipeline() as beam: 

with beam.Pipeline(options=Pipeline_options) as pipeline:
    (
        p
        | "input" >>beam.io.ReadFromText(word_list)
        
    )