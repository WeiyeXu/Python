import sys

# 1.

# does not return the size of any individual float, 
# it returns the size of the float class. 
# That class contains a lot more data than just any single float, 
# so the returned size will also be much bigger.
# https://stackoverflow.com/questions/49318826/getting-size-of-primitive-data-types-in-python/49318989

print ("The size of bool is : " + str(sys.getsizeof(bool)) + " bytes\n")

print ("The size of bool is : " + str(sys.getsizeof(bool())) + " bytes\n")

# Python 里面没有char
# https://www.zhihu.com/question/37055272/answer/70300775
# print ("The size of char is : " + str(sys.getsizeof(char())) + " bytes\n")

# Python 里面没有short
# print ("The size of short is : " + str(sys.getsizeof(short())) + " bytes\n")

print ("The size of int is : " + str(sys.getsizeof(int())) + " bytes\n")

# Python3 的 int 是没有限制大小的，可以当作 Long 类型使用，所以Python3没有Python2的 Long 类型
# print( "The size of long is " + str(sys.getsizeof(long)) + " bytes\n")
# print ("The size of long long is " + str (sys.getsizeof(long long())) + "bytes\n")

print ("The size  of float is " + str(sys.getsizeof(float())) + " bytes\n")

# Python 没有 double 类型
# print ("The size of double is " + str(sys.getsizeof(double())) + " bytes\n")

# print("The size  of long double is " + str(sys.getsizeof(long double()) + " bytes\n")

#########################################################################################

