greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "John"

intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name)

print(intrupution, formatted)

text = "My favorite color is Purple!"

name = "Quana"

intrupution = f"Hello, my name is {name}."

greet_format = "Hello my name is {}"

formatted = greet_format.format(name)

print(intrupution, formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace("Quana", "Auna"))
print(text)
print(text.replace("Purple", "Green"))
print(text.upper().replace("color", "food"))