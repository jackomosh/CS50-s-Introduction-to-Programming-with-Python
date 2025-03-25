def greet(input):
    if "Hello" in input:
        return "Hello, There!"
    else:
        return "I'm not sure what you mean"
    
greeting = greet("Hello")
print(greeting + ' ' + "Jack")