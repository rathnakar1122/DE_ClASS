import apache_beam as beam

List = [2000,3000,4000]
def print_Udf(element):
    print(element)


with beam.Pipeline () as pipeline:
    poll = pipeline | "input PCollection" >> beam.Create(List)
    output = poll | "printing " >>beam.Map(print_Udf)

