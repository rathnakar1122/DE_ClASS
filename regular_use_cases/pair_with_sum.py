list= [ 1,2,3,4,5,6,7,8,9,10]
sum = 11

def find_pairs(num, sum):
    empty_set=set()
    for i in range (len(num)):
       for j in range (i+1,len(num)):
         if num[i] + num [j] ==sum:
           empty_set.add((num[i],num[j]))
    return empty_set

result = find_pairs(list,sum)
print(result)
    
##############################################
number = [1,2,3,4,5,6,7,8,9]
target_sum=11

def find_pairs(num, target_sum):
    empty_set=set()
    for i in range (len(num)):
        for j in range (len(num)):
            if num[i]+num[j]==target_sum:
                empty_set.add((num[i],num[j]))
    return empty_set

result = find_pairs(number, target_sum)
print(result)
#####################################################


List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 11
pairs = []
set_numbers = set()

for number in List:
    final = total - number  # Find the complement
    if final in set_numbers:
        pairs.append((final, number))
    set_numbers.add(number)  # Add the current number to the set

print(pairs)

