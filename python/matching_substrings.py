if __name__ == '__main__':
    test_string = 'abracadabra' 
    test_list = ['ab', 'ra', 'ca', 'da', 'br', 'cs']
    
    # List Comprehension
    res = [substr for substr in test_list if substr in test_string]
    print(res)
    
    # Using filter() and lambda
    res1 = list(filter(lambda x: x in test_string, test_list))
    print(res1)
    
    # Using find() method
    res2 = []
    for substr in test_list:
        if (test_string.find(substr) != -1):
            res2.append(substr)
    print(res2)