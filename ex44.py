"""
class Parent(object):
	
	def implicit(self):
		print "PATENT implicit()"


class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
"""
"""
class Parent(object):
	
	def override(self):
		print "PARENT override()"

class Child(Parent):
		
	def override(self):
		print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
"""
"""
class Parent(object):

	def altered(self):
		print "PARENT altered()"
class Child(Parent):
 	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child,self).altered()
		print "CHILD, AFTER PARENT altered()"
class Child(Parent):
	
	def __init__(self,stuff):
		self.stuff = stuff
		super(Child,self).__init__()


dad = Parent()
son = Child()

dad.altered()
son.altered()
"""
print "Composition:"

class Other(object):

	def override(self):
		print "OTHER override()"
	
	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Child(object):
	
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()
	
	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()

