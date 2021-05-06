def max_number(list1):
    counter=0
    max1=list1[0]
    while counter<len(list1):
        if list1[counter]>max1:
            max1=list1[counter]
        counter=counter+1
    return max1
def two_list(list1,list2):
    value=list1+list2
    call_function=max_number(value)
    return (call_function)
def odd_even(list):
    list=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,99,234,20]
    list1=[]
    list2=[]
    index=0
    while index<len(list):
        if list[index]%2==0:
            list1.append(list[index])
        elif list[index]%1==0:
            list2.append(list[index])
        index=index+1
    print(list1)
    print(list2)
    callfunction=two_list(list1,list2)
    print(callfunction)
odd_even(list)