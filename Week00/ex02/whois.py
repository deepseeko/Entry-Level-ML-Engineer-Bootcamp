import sys

if len(sys.argv) != 2:
	print("more than one arg !")
	sys.exit(1)

try:
	number = int(sys.argv[1])
	if number == 0:
		print("I'm Zero.")
	elif number % 2 == 0 :
		print("I'm Even.")
	elif number % 2 != 0:
		print("I'm Odd.")
except:
	print("{{argument is not an integer}}")
