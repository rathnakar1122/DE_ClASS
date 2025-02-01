import apache_beam as beam
import datetime 

input_file_path = r"C:\my_virtual_env\DE_class\File_handling _python.py\sample_file.csv"
output_file_path = r"C:\my_virtual_env\DE_class\File_handling _python.py\sample_file_one.csv"

# timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
# output_file_path = f"C:\\my_virtual_env\\DE_class\\apache_beam\\sample_output_{timestamp}.csv"

def eliminating_last_cher(element):
    row = element.split() # when you split any string object - it will create a list object by following delimeter space
    result = striping_last_unnecessory_character(row)
    output = ",".join(result)
    return output

def striping_last_unnecessory_character(word_list):
    empty_list = []
    for i in range (len(word_list)-1):
        #emptylist.append(list[i][:len(word_list[i])-1])
        empty_list.append(word_list[i][:-1])  # Remove the last character from each word
    #emptylist.append(list[len(list)-1])
    empty_list.append(word_list[-1])  # Append the last word as it is

    #return emptylist
    return empty_list


with beam.Pipeline() as pipeline:
    pcoll = pipeline | "Read Input" >> beam.io.ReadFromText(input_file_path)
    trasformation = pcoll | "trasformations" >> beam.Map(eliminating_last_cher)
    result = trasformation | ' writing to local path' >> beam.io.WriteToText("output_file_path")