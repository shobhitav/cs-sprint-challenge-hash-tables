def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    
    length=len(weights)
    cache={}
    # populate the cache with values and indices from weights
    for i in range(len(weights)):
        cache[weights[i]] = i
    print(cache) 

    # look up index from weights list and corresponding value in cache for key which 
    # satisfies condition (limit - weight)
    for index,weight in enumerate(weights):
        w=limit-weight
        if w in cache :
            return (index,cache[w]) if index > i else (cache[w],index)

      


print(get_indices_of_item_weights([ 4, 6, 10, 15, 16 ],5,21))