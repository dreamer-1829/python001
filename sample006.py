original = [1, 3, 5, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(original)) 

result = [] 
for x in original: 
    if x not in result: 
        result.append(x) 

print ("The list after removing duplicates : " + str(result)) 
