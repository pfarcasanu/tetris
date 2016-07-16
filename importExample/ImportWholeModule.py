'''
	import as a whole module
	In this way, a varible named module1 is defined in this function.
	module1 contains all the global components from "module1.py"
	To access those components in the module, you need to say module1.name_of_the_global_var

	Run the script to see if it makes sense.
'''
import module1

print(module1.global_variable_in_module1)
module1.global_function_in_module1("Fred")
y = module1.global_class_in_module1()
print(y)
