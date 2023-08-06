"""这是nester.py模块，提供了一个print_lol（）的函数，这个函数的作用是打印列表，
其中又可能包含（也可能不包含）嵌套列表。"""
def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item)
		else:
			print(each_item)
