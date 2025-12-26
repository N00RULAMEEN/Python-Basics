import sys



if len(sys.argv) < 2:
    sys.exit("Too Few Arguments")

for arg in sys.argv[1:] :

    print("Hi Welcome To Mega World ", arg)      

"""

if len(sys.argv) < 2:
    sys.exit("Too Few Arguments")
elif len(sys.argv) >2 :
    sys.exit("Too Many Arguments")

else:
    print("Hi Welcome To Mega World ",sys.argv[1] )        

"""
"""
print("Hi Welcome To Mega World ",sys.argv[1] )   

if len(sys.argv) < 2:
    print("Too Few Arguments")
elif len(sys.argv) >2 :
    print("Too Many Arguments")

else:
    print("Hi Welcome To Mega World ",sys.argv[1] )        """