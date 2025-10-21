# here we are knowing return values how will work im not expalining waht is return value 


def greet(input):
    if "Hello " in input:
        return "Hello there"
    else: 
        return "Im Not Sure What You Mean"

greeting = greet("where is my phone ")
print(greeting)