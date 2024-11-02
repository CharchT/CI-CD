arr = [-3, -3, -3, -3, 4, 4, 4, 5]

res =[]

first_max = -0.0001
second_max = -0.0001
third_max = -0.0001
fourth_max = -0.0001

first_min = 0.0001
second_min = 0.0001
third_min = 0.0001
fourth_min = 0.0001

for i in range(len(arr)):
  if arr[i]>first_max and len(arr) >= 1:
    fourth_max = third_max
    third_max = second_max
    second_max = first_max
    first_max = arr[i]
    index = i

  if arr[i]<=first_max and arr[i] > second_max and index != i:
    fourth_max = third_max
    third_max = second_max
    second_max = arr[i]
    index = i

  if arr[i] <= second_max and arr[i] > third_max and index != i:
    fourth_max = third_max
    third_max = arr[i]
    index = i

  if arr[i] <= third_max and arr[i] > fourth_max and index != i:
    fourth_max = arr[i]

  if arr[i] < first_min:
    fourth_min = third_min
    third_min = second_min
    second_min = first_min
    first_min = arr[i]
    index = i

  if arr[i] >= first_min and arr[i] < second_min and index != i:
    fourth_min = third_min
    third_min = second_min
    second_min = arr[i]
    index = i

  if arr[i] >= second_min and arr[i] < third_min and index != i:
    fourth_min = third_min
    third_min = arr[i]
    index = i

  if arr[i] >= third_min and arr[i] < fourth_min and index != i:
    fourth_min = arr[i]

if first_min != 0.0001 and second_min != 0.0001\
 and first_max != -0.0001 and second_max != -0.0001:
  biggest_positive_pair = first_max*second_max
  biggest_negative_pair = first_min*second_min
  res.append(biggest_positive_pair*biggest_negative_pair)

if first_max != -0.0001 and first_min != 0.0001\
 and second_min != 0.0001 and third_min != 0.0001:
  biggest_negative_three = first_max*first_min*second_min*third_min
  res.append(biggest_negative_three)

if first_min != 0.0001 and first_max != -0.0001\
 and second_max != -0.0001 and third_max != -0.0001:
  biggest_positive_three = first_min*first_max*second_max*third_max
  res.append(biggest_positive_three)

if first_max != -0.0001 and second_max != -0.0001\
 and third_max != -0.0001 and fourth_max != -0.0001:
  biggest_positive_quarter = first_max*second_max*third_max*fourth_max
  res.append(biggest_positive_quarter)

if first_min != 0.0001 and second_min != 0.0001\
 and third_min != 0.0001 and fourth_min != 0.0001:
  biggest_positive_quarter = first_min*second_min*third_min*fourth_min
  res.append(biggest_positive_quarter)

print(max(res))
