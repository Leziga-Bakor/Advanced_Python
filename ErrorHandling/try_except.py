try:
    f = open('test_file.txt')
    if f.name == 'test_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception:
    print(('Sorry. file does not exist'))
else:
    print('this session handled what code does if try block doesnt catch error')
finally:
    print('This runs no regardless of what happens in the  try block')
    
'''
More general exception should be last
'''