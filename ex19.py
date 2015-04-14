# functions and variabels 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

## Note: function has to be put into a new line. It can not just following print syntax!!!  
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from out script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers
 + 1000)

print "How many cheese do you have?"
num_cheese = int(raw_input(">"))

print "How many crackers do you have?"
num_cracker = int(raw_input(">"))

print "There is total cheese and crackers you have now:"
cheese_and_crackers(num_cheese, num_cracker)
