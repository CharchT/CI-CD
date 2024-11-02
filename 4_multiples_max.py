import heapq

arr = [-3, -3, -3, -3, 4, 4, 4, 5]

# Edge case: if the array has fewer than 4 elements
if len(arr) < 4:
    print("Array must have at least 4 elements.")
else:
    # Get the four largest and four smallest values
    largest = heapq.nlargest(4, arr)
    smallest = heapq.nsmallest(4, arr)

    # Calculate the products
    products = []

    # Product of the two largest positive numbers
    if len(largest) >= 2 and largest[1] > 0:
        products.append(largest[0] * largest[1])

    # Product of the two smallest negative numbers
    if len(smallest) >= 2 and smallest[1] < 0:
        products.append(smallest[0] * smallest[1])

    # Product of the three largest numbers
    if len(largest) >= 3:
        products.append(largest[0] * largest[1] * largest[2])

    # Product of the four largest numbers
    if len(largest) >= 4:
        products.append(largest[0] * largest[1] * largest[2] * largest[3])

    # Product of the three smallest numbers
    if len(smallest) >= 3:
        products.append(smallest[0] * smallest[1] * smallest[2])

    # Product of the four smallest numbers
    if len(smallest) >= 4:
        products.append(smallest[0] * smallest[1] * smallest[2] * smallest[3])

    # Get the maximum product
    if products:
        print(max(products))
    else:
        print("No valid products found.")
