with open('config.txt', 'w') as file:
    file.write("Hello, World!")

try:
    with open('config.txt', 'r') as file:
        content = file.read()
        print(content)

except :
    with open('config.txt', 'w') as file:
        content= file.write("Guest")
        print(content)