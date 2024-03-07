import sys
import re
import util

allowed_options = {'i','n','c','l','w','H','o'}
command_options = set()
search_string   = ''
file_paths      = []


ERROR_TEXT = "\033[1;31mERROR: \033[0m"
READ_ONLY  = 'r'

# Error handling
if sys.argv.__len__() < 3:

    print(ERROR_TEXT + "You must specify the search string and the filename.\n")
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


MATCH_TYPE = util.get_pattern_matching_type(command_options,search_string)


grep_result_object = {}

matched_files = []

for eachfile in file_paths:

    line_count     = 0
    match_count    = 0

    with open(eachfile,READ_ONLY) as file:
        
        for line in file:

            line_count += 1
            matches     = MATCH_TYPE.findall(line)

            if len(matches):

                match_count += 1

                if 'l' in command_options:
                    matched_files.append(eachfile)
                    break

                if 'c' not in command_options:

                    output_string = ''

                    if 'H' in command_options or len(file_paths) > 1:

                        output_string += f'{eachfile}:'
                    
                    if 'n' in command_options:
                        output_string += f'{line_count}:'
                    
                    if 'o' in command_options:

                        for each_match in matches:

                            if output_string != '':
                                print(f'{output_string}:{each_match}')
                            else:
                                print(each_match)
                    
                    else:

                        output_string += f'{line}'

                        print(output_string.strip())
        
        if 'c' in command_options and 'l' not in command_options:
            
            if len(file_paths) > 1:

                print(f'{eachfile}:{match_count}')
            
            else:
                print(match_count)


if 'l' in command_options:
    
    for each_file in matched_files:
        output_string = ''

        if 'c' in command_options and len(matched_files) > 1:

            output_string = f'{each_file}:1'
            
            print(output_string)
        
        elif 'c' in command_options and len(matched_files) == 1:
            output_string = '1'

            if 'H' in command_options:
                output_string = f'{each_file}:1'
            
            print(output_string)
        
        print(each_file)
