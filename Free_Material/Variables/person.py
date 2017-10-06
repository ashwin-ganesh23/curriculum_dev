class Person:

	def __init__(self, name, age, height, hadDinner):
		self.name = name			#string type
		self.age = age				#int type
		self.height = height		#float type (in feet)
		self.hadDinner = hadDinner	#boolean type

	def display_height(self):
		print("{} is {} feet tall!".format(self.name, self.height))

	def greet_person(self):
		print("Welcome to Peerbuds Innovation Lab, {}".format(self.name))

	def want_dinner(self):
		if self.hadDinner:
			print("Lucky!!! What did you have?")
		else:
			print("Uhoh, time to wrap up soon!")

	def drink(self):
		if not(self.age >= 21):
			print("Please help yourself!")
		else:
			print("Water and coffee only :)")

me = Person('Ashwin', 24, 6.0, False)

me.display_height()
me.greet_person()
me.want_dinner()