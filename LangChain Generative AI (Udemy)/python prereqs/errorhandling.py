## Exception try, except block
try:
    a = b
except NameError as ex:
    print (ex)

try:
    result = 1 / 0
except ZeroDivisionError as ex:
    print(ex)
    print('Please enter a denom greater than 0')
    
try:
    result = 1 / 2
    a=b
except ZeroDivisionError as ex:
    print(ex)
    print('Please enter a denom greater than 0')
except Exception as ex1:
    print(ex1)
    print('Main exception got caught')

try: 
    num = int(input("Enter num: "))
    result = 10/num
except ValueError:
    print('This is not a valid number')
except ZeroDivisionError:
    print('Zero is not valid')
except Exception as ex: #main exception class always goes last
    print(ex)
    
#try except else

try:
    num = int(input("Enter a number"))
    result = 10/num
except ValueError:
    print('This is not a valid number')
except ZeroDivisionError:
    print('Zero is not valid')
except Exception as ex: #main exception class always goes last
    print(ex)
else:
    print(f"the result is {result}")
    
#try except else finally
try:
    num = int(input("Enter a number: "))
    result = 10/num
except ValueError:
    print('This is not a valid number')
except ZeroDivisionError:
    print('Zero is not valid')
except Exception as ex: #main exception class always goes last
    print(ex)
else:
    print(f"the result is {result}")
    
finally:
    print("Execution complete.")
    
### File handling and exception handling
try:
    file=open('AI/LangChain Generative AI (Udemy)/example1.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist")
finally:
    if 'file' in locals() and not file.closed():
        file.close()
        print('file close')
    