# printing, printing
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
#print formatter % (1,2,3) ## have to put for argument here since formatter has 4 argument 
## %r-> can put everything: numercial value, logic value,string,sentence
print formatter %("one", "two", "three", "four")
print formatter %(True, False, False, True)
print formatter %(formatter, formatter, formatter,formatter)
print formatter %(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print "-----"
print formatter %('one','two','False',1)
