# max weight of knapsack is 8kg

# wt = (3, 4, 6, 5)
# val = (2, 3, 1, 4)
# n = len(val)


# result: max capacity is 6 (weights 3 + 5), result in largest value of 6

W = int(input("What is the maximum capacity of the knapsack? "))
n = int(input("How many items are in your knapsack? "))

# initiate these two arrays (or lists)
wt = []
val = []

# 1. print(), not print = "something"  2. printing this prompt once should be okay, no need to put it into a loop
print("Please enter your values one by one.")

while n > 0:
    wt.append(int(input("Enter the weight: ")))
    val.append(int(input("Enter your value: ")))
    n = n - 1

# print out the two arrays
#print(wt)
#print(val)

n = len(val)

# W is capacity of knapsack
# n is amount of items
# wt is weight
# val is value

def knapsack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        return knapsack(W, wt, val, (n - 1))
    else:
        return max(
            val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1),
            knapsack(W, wt, val, n - 1),
        )

print(knapsack(W, wt, val, n))
input('Press ENTER to exit')