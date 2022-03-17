# =============================================================================
# list3 = {"one": "freshman", "two":2, "three":True}
# 
# print(list3["two"])
# 
# print(list3.values())
# =============================================================================

# =============================================================================
# def add(num1, num2=5):
#     return num1 + num2
# 
# 
# print (add(2,8))
# =============================================================================

try:
    x = 6/3
except(ArithmeticError):
    print("division by zero is not allowed")
except(Exception):
    print("invalid input...")
else:
    print(x)
finally:
    print("finally block...")