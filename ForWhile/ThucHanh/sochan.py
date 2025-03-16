list_of_lists=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sochan=[]
for sublist in list_of_lists:
    for num in sublist:
        if num%2==0:
            sochan.append(num)
print(sochan)