if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    def sliding_window(elements, window_size):
        
        if len(elements) <= window_size:
            return
        
        for i in range(len(elements) - window_size + 1):
            print(elements[i:i+window_size])
            
    sliding_window(lst, 3)