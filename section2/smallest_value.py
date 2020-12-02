arr = [5, 3, 9, 2, 5, 2, 6]
arrMin = float('inf')
for i in range(len(arr)):
  if arr[i] < arrMin: # if <=, value will be replaced later value in the list
    arrMin = arr[i]
print(arrMin)