# import apache_beam as beam
# List = [2000,3000,4000,5000,6000]

# def Increment_func(element):
#     return element * 2

# def Print_Udf(element):
#     print(element)


# with beam.Pipeline() as pipeline:
#     pcoll = pipeline | 'Input pcollection creation' >> beam.Create(list)
#     transformation = pcoll | 'Incrementing the values' >> beam.Map(Increment_func)
#     output = transformation | 'Printing' >> beam.Map(Print_Udf)

import apache_beam as beam

List = [2000,3000,4000,5000,6000]

def Increment_func(element):
    return element *2

def print_udf(element):
    print(element)

with beam.Pipeline () as pipeline:
    pcoll = pipeline | 'input pcollection creation' >> beam.Create(List)
    trasaformation = pcoll|"incremenatal the values " >> beam.Map (Increment_func)
    output = trasaformation | 'printing ' >> beam.Map(print_udf)
