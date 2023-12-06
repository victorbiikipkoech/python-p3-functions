def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    
    return number / 2

# Test the functions
greet_programmer()  # Outputs: "Hello, programmer!"
greet("Naureen")    # Outputs: "Hello, Naureen!"
greet_with_default()          # Outputs: "Hello, programmer!"
greet_with_default("Sunny")   # Outputs: "Hello, Sunny!"

sum_result = add(1, 2)
print(sum_result)  # Outputs: 3

halve_result = halve(4)
print(halve_result)  # Outputs: 2

invalid_result = halve("two")
print(invalid_result)  # Outputs: None
