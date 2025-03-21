### Read a whole file

with open('AI/LangChain Generative AI (Udemy)/example.txt', 'r') as file:
    content = file.read()
    print(content)
        
with open('AI/LangChain Generative AI (Udemy)/example.txt', 'r') as file:
    for line in file:
        print(line.strip()) ## .strip removes newline char
        
## Writing a file (overwriting)
with open('AI/LangChain Generative AI (Udemy)/example.txt', 'w') as file:
    file.write('Hello World!\n')
    file.write('this is a new line.\n')
    
## Write without overwriting
with open('AI/LangChain Generative AI (Udemy)/example.txt', 'a') as file:
    file.write("append operation!\n")
    
## writing a list of lines
lines = ['First line\n','Second line \n', 'Third line\n']
with open('AI/LangChain Generative AI (Udemy)/example.txt', 'a') as file:
    file.writelines(lines)

### Binary Files

#writing to a binary file
data = b'\x00\x01\x02\x03\x04'
with open('example.bin', 'wb') as file:
    file.write(data)
    
### read content from file, write to destination text file
with open('AI/LangChain Generative AI (Udemy)/example.txt', 'r') as source:
    content  = source.read()
with open('destination.txt', 'w') as destination:
    destination.write(content)
    
# read text file and count number of lines words and char
with open('AI/LangChain Generative AI (Udemy)/example.txt', 'r') as file:
    lines = file.readlines() 
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line)for line in lines)

## Writing and then Reading 
with open('AI/LangChain Generative AI (Udemy)/example.txt', 'w+') as file:
    file.write("Hello World\n")
    file.write("This is a new line\n")
    
    ## Move file cursor to the beginning
    file.seek(0)
    
    ## Read content
    print(content)