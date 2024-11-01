arr = [10,51,81,21,22,35,0,24]

def selection_sort(input_arr=arr):
    # len_of_array = len(input_arr)
    for i in range(len(input_arr)-1):
        min_index = i
        for j in range(i+1,len(input_arr)):
            if input_arr[j] < input_arr[min_index]:
                min_index = j 
        input_arr[i],input_arr[min_index] = input_arr[min_index],input_arr[i]

    print(f"The sorted array by selection sort is {input_arr}")

def bubble_sort(input_arr=arr):
    # len_of_array = len(input_arr)
    for i in range(1,len(input_arr)+1):
        
        for j in range(len(input_arr)-1):
            if input_arr[j] > input_arr[j+1]:
                 
                input_arr[j],input_arr[j+1] = input_arr[j+1],input_arr[j]

    print(f"The sorted array is by bubble sort is {input_arr}")


def insertion_sort(input_arr=arr):
    # len_of_array = len(input_arr)
    for i in range(1,len(input_arr)):
        
        j = i
        while j>0 and input_arr[j-1]>input_arr[j]:
            input_arr[j-1],input_arr[j] = input_arr[j],input_arr[j-1]
            j -= 1

    print(f"The sorted array is by insertion sort is {input_arr}")

import pandas as pd
import os
data = {"Name":["Bruce","Clarke"],"AKA":["Batman","Superman"]}
df = pd.DataFrame(data)
path = os.getcwd()
filepath = os.path.join(path,"export_try.xlsx")
df.to_excel(filepath)
status = os.path.exists(filepath)
if status == True:
    df = pd.read_excel(filepath)

print(df)
print(f"The file exists status:{status}")





if __name__ == "__main__":
    selection_sort()
    bubble_sort()
    insertion_sort()

        
