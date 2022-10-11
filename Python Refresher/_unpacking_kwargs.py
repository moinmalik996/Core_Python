# def general(**kwargs):
#     print(kwargs)




# def general(**kwargs):
#     print(kwargs)
    

# details = {
#     'name':'Malik Moin',
#     'age':34,
# }
# general(**details)

# def kwargs_print(**kwargs):
#     print(kwargs)

# def print_nicely(**kwargs):
#     kwargs_print(**kwargs)
#     for key, value in kwargs.items():
#         print(f'{key} : {value}')
        
        
# print_nicely(name='Moin', age=24)


def both(*args, **kwargs):
    print(args)
    print(kwargs)
    
    
both(1, 2, 3, name='Moin',age=12)

