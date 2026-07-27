print("Enter the size of array : ")
size = int(input())

# int *Arr = (int *)malloc(sizeof(int) * size); C
# int Arr[] = new int[size]; C++
# int Arr[] = new int[size]; Java

Arr = [0] * size

print("Size of array is : ",len(Arr))

print(Arr[0])
print(Arr[1])
print(Arr[2])
print(Arr[3])

# free(Arr)     C
# delete(Arr)   C++
# Arr = null    Java
# System.gc()   Java

del Arr