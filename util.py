import os

allowed_options = {'i','n','c','l','w'}
error_text = "\033[1;31mERROR: \033[0m"

def validate_input_arguments( search_string,command_options,file_paths ):
    
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

    for filespec in file_paths:
        
        if not os.path.exists(filespec):
            print(error_text + filespec + " - File path does not exist.\n")
            exit(2)

        elif os.path.isdir(filespec):
            print(error_text + filespec + " - is a directory.")
            exit(2)
    