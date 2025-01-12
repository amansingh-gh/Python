# class sm:
#     # @staticmethod
#     def add(a,b):
#         return a*b
    
# result = sm.add(2,5)
# print(result)


# class s_m:
#     @staticmethod
#     def add(a,b):
#         return a+b
# result = s_m.add(5,9)
# print(result)

# class s_method:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
        
#     def add(self):
#         return self.a + self.b


# res = s_method(5,10)
# result = res.add()
# print(result)



class sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    
opp = sum(10,20)
result = opp.add()
print(result)
