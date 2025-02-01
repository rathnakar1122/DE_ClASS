import apache_beam as beam

# Path to input and output files
input_file = r'C:\ENV\PREP\DE_class\apache_beam\sample.txt'
output_file = r'C:\ENV\PREP\DE_class\apache_beam\output'

# Define the Beam pipeline
with beam.Pipeline() as p1:
    # Read the data
    consultas = (
        p1
        | 'Read Text File' >> beam.io.ReadFromText(input_file)  # Read the file line by line
        | 'Parse Stringified List' >> beam.Map(lambda line: eval(line.split('\t')[1]))  # Parse the stringified list
        | 'Filter Age > 18' >> beam.Filter(lambda record: int(record[2]) > 18)  # Filter where age > 18
        | 'Filter Salary > 2500' >> beam.Filter(lambda record: int(record[3]) > 2500)  # Filter where salary > 2500
        | 'Format Output' >> beam.Map(lambda record: f"{record[0]}\t{record}")  # Add index back and format as a string
        | 'Write to File' >> beam.io.WriteToText(output_file, file_name_suffix='.txt')  # Write to output file
    )
