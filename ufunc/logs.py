# import numpy as np
# arr=np.arange(1,10)
# print(np.log2(arr))

# print("\n")
# print(np.log10(arr))

# print("\n")
# print(np.log(arr))

# from math import log 
# import numpy as np
# n=np.frompyfunc(log,2,1)
# print(n(1000,10))


# Summations

# import numpy as np
# aee=np.array([1,2,3,4])
# abb=np.array([3,4,5,6])
# ner=np.add(aee,abb)                       # add()
# sum=np.sum([aee,abb])                     # sum()
# s=np.sum([aee,abb],axis=1)                # sum() along axis=1
# so=np.cumsum(aee)                         # cumsum()
# print(ner,"\n",sum,"\n",s,"\n",so)


# import numpy as np
# a=np.array([1,2,3,4])
# b=np.array([3,4,5,6])
# x=np.prod(a)                                  # prod()
# y=np.prod([a,b])                              #prod(2array)
# y1=np.prod([a,b],axis=1)                      #prod() along axis=1
# y2=np.cumprod(a)                              #cumprod()
# print(x,y,y1,y2)


# import numpy as np
# a=np.array([1,2,3,4])
# b=np.array([3,4,5,6])
# n=np.diff([a,b])                                  # diff()
# o=np.diff(a,n=2)                                  # diff(array,times=2)
# print(n,o)

# import numpy as np
# num=24
# num1=28
# a=np.array([1,2,3,4])
# b=np.arange(1,10)
# x=np.lcm(num,num1)                      #lcm of two numbers(lcm())
# y=np.lcm.reduce(a)                      #lcm of an array(lcm.reduce())                  
# z=np.lcm.reduce(b)                      #lcm of an array(lcm.reduce(),arange())
# print(x,y,z)



# import numpy as np
# num=24
# num1=28
# a=np.array([1,2,3,4])
# b=np.arange(1,10)                          #greatest common factor(gcd() and gcd.reduce(arr))
# x=np.gcd(num,num1)
# y=np.gcd.reduce(a)   
# print(x,y)


# trigonometric ratios
# import numpy as np
# x=np.sin(np.pi/6)
# y=np.array([np.pi/4,np.pi/6,np.pi/3,np.pi/2])
# z=np.array([90,45,60,120])
# a=np.array([1,-1,0.1])
# print(x)                                        #finding the value using radian
# print(np.tan(y))                                #finding value using radian in array
# print(np.deg2rad(z))                            #conversion degree to radian
# print(np.rad2deg(y))                            #conversion radian to dgree
# print(np.arcsin(1.0))                           #inverse of sin,cos,tan(arcsin(),arccos(),arctan())
# print(np.arcsin(a))                             #inverse of sin,cos,tan(arcsin(),arccos(),arctan()) in array
# base=3
# perp=4
# print(np.hypot(base,perp))                      #find the hypotenuse through perpendicular and base



# hyperbolic functions        --cosh(np.pi/2), or in array(cosh(arr))
# Finding Angles              --np.arcsin(1.0) ---produce radian values for corresponding sinh, cosh and tanh values given.
# Angles of Each Value in Arrays---
# import numpy as np
# a=np.array([1,-1,0.1])
# print(np.arctan(a))


# NumPy Set Operations
# set---a collection of unique elements.
import numpy as np
arr=np.array([1,1,1,1,2,3,44,3,2,23,3])                 
arr1=np.array([12,13,15,19,2,3,44,3,2,23,30])                 
x=np.unique(arr)
y=np.union1d(arr,arr1)
y1=np.intersect1d(arr,arr1,assume_unique=True)
print(x,y,y1)

