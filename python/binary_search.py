if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 11
    
    def binary_search(array, x, low, high):
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if array[mid] == x:
                return mid
            elif array[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    result = binary_search(lst, target, 0, len(lst) - 1)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")