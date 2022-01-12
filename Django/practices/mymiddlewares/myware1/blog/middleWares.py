# def my_middleware(get_response):
#     print('One Time Initialization')
#     # Logic Before View Called
#     # end
#     def my_func(request):
#         response = get_response(request)
#         print("This is after View")
#         # Logic After View Called
#         # end
#         return response
    
#     return my_func


class my_middleware():
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization")
        
    def __call__(self, request):
        response = self.get_response(request)
        print("This is After View")
        return response