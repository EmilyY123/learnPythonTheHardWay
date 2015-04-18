## while loop
i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers  ## print a list:
	print "At the bottom i is %d" % i

print "The numbers:"

for num in numbers:
	print num


def num_print(num):
	new_numbers = []
	j = 0
	while j < num:	
		print "At the top j is %d" % j
		new_numbers.append(j)

		j = j + 1
		print "Numbers now:", new_numbers
		print "At the bottom j is %d" % j

num_print(8)

## increments by as arguments
def num_print_new(num,increment):
	new_numbers = []
	j = 0
	while j < num:
		print "At the top j is %d" % j
		new_numbers.append(j)

		j = j + increment
		print "Numbers now:", new_numbers
		print "At the bottom j is %d" % j

num_print_new(8,1)
num_print_new(8,3)

## use for 
numbers = []
for i in range(8):
	numbers.append(i)

print "Numbers are:", numbers
