# from datetime import time

# # x = time (hour=15)
# # print(x)

# import datetime 
# x = datetime.datetime.now()
# print(x)
# a = 33
# b = 200

# # if b > a:
# #   pass

# # having an empty if statement like this, would raise an error without the pass statement

# cars = [
#     {
#         "make": "Toyota",
#         "model": "Camry",
#         "year": 2020,
#         "price": 24000
#     },
#     {
#         "make": "Honda",
#         "model": "Civic",
#         "year": 2021,
#         "price": 22000
#     },
#     {
#         "make": "Tesla",
#         "model": "Model 3",
#         "year": 2022,
#         "price": 40000
#     }
# ]

cars = [
    {
        "make": "Toyota",
        "model": "Camry",
        "year": 2020,
        "price": 24000
    },
    {
        "make": "Honda",
        "model": "Civic",
        "year": 2021,
        "price": 22000
    },
    {
        "make": "Tesla",
        "model": "Model 3",
        "year": 2022,
        "price": 40000
    }
]

output= [cars[0]["make"],cars[1]["make"],cars[2]["make"]]
print(output)