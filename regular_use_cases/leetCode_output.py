# input_string = ' My NAme is Rathnakar '

# def de_substring(input_string):
#     words=input_string.replace(",",'').replace(",",'').split()
#     return max(words,key=len)
# output_string = de_substring(input_string)
# print(output_string)

#####################################################################





def substring(input_stringg):
    word=input_stringg.replace(",","").replace(",",'').split()
    return max(word,key=len)

def __main__():
    input="with the amazon s3 console ,you can easily access a bucket and modify the bucket properties"
    output_stringg = substring(input)
    print(output_stringg)

if __name__=="__main__":
    __main__()



















##########################################################################
# input_string = ' with the amzon s3 console , you can accessss the bucket'
# def find_larget_substring (input_string):
