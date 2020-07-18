def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache={}
    result=[]
    for item in a:
        # we only need to store negative numbers in dictionary
        if item < 0:
            cache[item]=item 
    print(cache) 
        #   for each positive value in array, if its negative is in cache ,append the result list 
    for item in a :
        if item > 0 and -item in cache:
            result.append(item)
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
