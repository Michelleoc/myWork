# x = float(input("Please enter a positive number: "))

# def mySqrt(x): r = x

# precision = 10 ** (-10)
    
# while abs(x - r * r) > precision:
    # r = (r + x / r) / 2
        
# return r

# print (r)


# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo


# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

# Python3 implementation of the approach

# Function to return the square root of
# a number using Newtons method

n = float(input("Please enter a positive number: "))
l = 0.00001

def squareRoot(n, l) :

	# Assuming the sqrt of n as n only
	x = n

	# To count the number of iterations
	count = 0

	while (1) :
		count += 1

		# Calculate more closed x
		root = 0.5 * (x + (n / x))

		# Check for closeness
		if (abs(root - x) < l) :
			break

		# Update root
		x = root

	return root

# Driver code
# if __name__ == "__main__" :

# n = 14.5
# l = 0.00001

print (squareRoot(n, l))

# This code is contributed by AnkitRai01
