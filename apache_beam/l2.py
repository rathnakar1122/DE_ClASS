# import apache_beam as beam

# List = [2000,3000,4000,5000,6000]

# with beam.Pipeline () as pipeline:
#     pcoll = pipeline | 'input pcollection creation' >> beam.Create(List)
#     output = pcoll | 'printing' >> beam.Map(lambda x: print(x))


import apache_beam as beam
List=[2000,3000,4000,5000]

with beam.Pipeline () as pipeline:
    pcoll = pipeline | 'input pcollection creation' >> beam.Create (List)
    output = pcoll | "printung" >> beam.Map(lambda x:print(x))
    output=output | "output ">>beam.Map("print")