import sys

if len(sys.argv) > 1 :
	i = len(sys.argv)
	while i > 1 :
		str = sys.argv[i-1][::-1].swapcase()
		print(f"{str}", end="")
		i = i - 1
print("")

