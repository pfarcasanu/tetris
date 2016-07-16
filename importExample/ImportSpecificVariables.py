'''
	import all components from other module
	In this way, specific global components from "module1.py" are defined in this Python script
	You can specify what global components you want to import

	You can use * to say that you want to import everything:
		from module1 import *
		This is equivalent to copy the whole file of module1 over to this python script

	Run the script to see if it makes sense.
'''
## This is equivalent to just copy and past all the content of GraphicsLib over here
from module1 import global_variable_in_module1, global_function_in_module1, global_class_in_module1
# from module1 import *

print(global_variable_in_module1)
global_function_in_module1("Fred")
x = global_class_in_module1()
print(x)
