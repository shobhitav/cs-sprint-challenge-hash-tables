# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache={}
    result=[]
    for file in files:
        # if key doesn't exist, initialize with empty list and append the file full path
        cache.setdefault(file.split('/')[-1],[]).append(file)
        
    # print(cache)

    for item in queries:
        if item in cache:
            for val in cache[item]:
                result.append(val)
     
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/dir/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
