with open('test.txt', 'w') as file:
    print(f'inside with: file closed? {file.closed}')


print(f'after with:file closed? {file.closed}')


