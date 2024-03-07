import os
import re

allowed_options = {'i','n','c','l','w','H','o'}
ERROR_TEXT = "\033[1;31mERROR: \033[0m"

def validate_input_arguments( search_string,command_options,file_paths ):
    
    for option in command_options:

        if option not in allowed_options:
            
            print(ERROR_TEXT + "Invalid option " + option + "\n")
            exit(1)

    if not search_string:

        print(ERROR_TEXT + "You must specify the search string.\n")
        exit(1)

    if not file_paths:

        print(ERROR_TEXT + "You must specify atleast one file.\n")
        exit(1)

    for filespec in file_paths:
        
        if not os.path.exists(filespec):
            print(ERROR_TEXT + filespec + " - File path does not exist.\n")
            exit(2)

        elif os.path.isdir(filespec):
            print(ERROR_TEXT + filespec + " - is a directory.")
            exit(2)


def get_pattern_matching_type(command_options,search_string):

    # Pattern Matches
    CASE_SENSITIVE        = re.compile(search_string)
    CASE_INSENSITIVE      = re.compile(search_string,re.IGNORECASE)
    CASE_SENSITIVE_WORD   = re.compile(f'\\b{search_string}\\b')
    CASE_INSENSITIVE_WORD = re.compile(f'\\b{search_string}\\b',re.IGNORECASE)

    MATCH_TYPE = CASE_SENSITIVE

    if 'w' in command_options:

        MATCH_TYPE = CASE_SENSITIVE_WORD

        if 'i' in command_options:

            MATCH_TYPE = CASE_INSENSITIVE_WORD
    
    elif 'i' in command_options:

        MATCH_TYPE = CASE_INSENSITIVE
    
    return MATCH_TYPE
