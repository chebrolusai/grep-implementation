import sys
import re

allowed_options = {'i','n','c','l','w'}
command_options = set()
search_string   = ''
file_paths      = []
error_text = "\033[1;31mERROR: \033[0m"


# Error handling
if sys.argv.__len__() < 3:

    print(error_text + "You must specify the search string and the filename.\n")
    exit(1)



# Parse input arguments
for argument in sys.argv[1:]:

    if re.match("^-[a-zA-Z]+",argument):

        for each_char in argument[1:]:

            command_options.add(each_char)

    elif search_string == '':

        search_string = argument

    else :

        file_paths.append(argument)



# Error handling
for option in command_options:

    if option not in allowed_options:
        
        print(error_text + "Invalid option " + option + "\n")
        exit(1)

if not search_string:

    print(error_text + "You must specify the search string.\n")
    exit(1)

if not file_paths:

    print(error_text + "You must specify atleast one file.\n")
    exit(1)