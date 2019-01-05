def even_numbers():
    count = 0
    for i in range(1,10):
        if i%2 == 0:
            print(i)
            count+=1
    return count
print("There are totally: " + str(even_numbers()) + " even numbers")