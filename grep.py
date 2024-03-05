import sys
import re
import util

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


util.validate_input_arguments(search_string,command_options,file_paths)