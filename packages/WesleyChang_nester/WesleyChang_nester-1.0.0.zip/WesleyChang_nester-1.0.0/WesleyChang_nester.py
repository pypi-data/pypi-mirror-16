"""This is theh "nester.py" module and it provides one function called print_lol()
    which prints lists that may or may not includee nested lists."""
def print_lol(the_list):
        """This function takes one postional argument called "the list" , which
            is any Python list (of - possibly - nested lists). Each data item in the 
            provided list is (recursively) printed to the scren on it's own line."""
        for each_item in the_list:
                if isinstance(each_item, list):
                        print_lol(each_item)
                else:
                        print(each_item)
                
