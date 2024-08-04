if __name__ == '__main__':
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [3, 4, 5, 6, 7]
    
    #No built-in functions
    lst3 = [value for value in lst1 if value in lst2]
    
    print(lst3)
    
    #Using set() method
    lst4 = list(set(lst1) & set(lst2))
    print(lst4)
    
    #Using set() and intersection() method
    lst5 = list(set(lst1).intersection(lst2))
    print(lst5)