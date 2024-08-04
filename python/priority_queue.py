if __name__ == '__main__':
    customers = []
    
    for i in range(10):
        customers.append((i, f'Customer_{i}'))
    customers.sort(reverse=True)
    
    while customers:
        print(customers.pop(0))