## more variables and printing
my_name = "Zed A. Shaw"
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 #lbs
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print "Let's talk about %s." % my_name
print "He is %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usualy %s depending on the coffee." % my_teeth

## this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age,my_height,my_weight,my_age+my_height + my_weight)

print "If I add %d, %d, and %s." %(my_age,my_height,my_name)

height_in_cm = my_height * 2.54
weight_in_kg = my_weight / 2.2

print "He's %d pounds heavy that is %f kg." %(my_weight,weight_in_kg)
## print out as 2 digital round(f,2)
print "He's %d pounds heavy that is %.2f kg." %(my_weight,weight_in_kg)
print "He is %d inches tall that is %f cm." %(my_height,height_in_cm)
