# #what is range function in python : it is used to generate a sequence of numbers it commomnly used in Loops to iterate over the specific set of values 

# #2. what is string slicing in python 
# string = 'rajashekar,'

# """removing comma """

# print(string)
# print(string[::])

# #every alternative charecter should be printted
# print(string [::2])

# #First 3 charecter to be prineted
# print(string[:3])

# #last charecter to be removed'
# print(string[:10])

# #it shoud work for everyinput 
# print(string[:len(string)-1])

# print(string [:len(string)-2])




# #################################################################################
# #3. Programme to strip the last character for any given string
# inputstring=str(input("Please enter your name:"))
# def strip_last_charecter(string):
#     print(string[:len(string)-1])



################################################################################
#How to join the multiple elements in of list, tuple and string
# ['1,', 'rajasekhar,', '20,', '3000']
# ['2,', 'rani,', '61,', '3000']
# ['3,', 'Roja,', '34,', '5000']
# input = ['1,', 'rajasekhar,', '20,', '3000']

# def striping_last_unnecessory_character(list):
#     emptylist = []
#     for i in range(len(list)-1): 
#         emptylist.append(list[i][:len(list[i])-1])
        
#     emptylist.append(list[len(list)-1])
    
#     return emptylist

#output = ['1', 'rajasekhar', '20', '3000']

#     emptylist = []
#     for i in range(len(list)-1):
#         print(list[i][:len(list[i])-1])
#         emptylist.append(list[i][:len(list[i])-1])
        
#     emptylist.append(list[len(list)-1])
                                                                            
#     return emptylist
# output = ['1', 'rajasekhar', '20', '3000']

# result = striping_last_unnecessory_character(input)
# print(result)
#output ['1', 'rajasekhar', '20', '3000']

## Updated Version for the above script

# def striping_last_unnecessory_character(list):
#     emptylist = []
#     for i in range(len(list)-1): 
#         emptylist.append(list[i][:len(list[i])-1])        
#     emptylist.append(list[len(list)-1])    
#     return emptylist
# output = ['1', 'rajasekhar', '20', '3000']
# result = striping_last_unnecessory_character(input)
# print(result)


