import pandas as pd
from math import sqrt; from itertools import count, islice

#PART 1
def findtype(n):
    if n<= 1:
        return "NA"
    elif all(n%i for i in islice(count(2), int(sqrt(n)-1))) :
        return "prime"
    else: return "composite"

result=np.asarray([findtype(num) for num in number_list])
np.save("key",result)


#PART 2
for query in query_arrays:
    print(np.sum(np.absolute((imgs_array-query)),axis=(1,2)).argmin())
# 2 6 8 6

#PART3
def customer_login_func():
    sum,i=0,2
    while True:
            if(findtype(i)=='prime'):
                sum = sum + i
                yield sum
            else:
                yield sum
            i+=1