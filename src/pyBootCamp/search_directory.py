import os


'''
Function to search for files in specified path.
It stores the files in a list returning it to client.
'''
def find_files(search_path):
    result = []
    # lists all files in given search path.
    for _,_,files in os.walk(search_path):
        result = files
    return result

# Searches files in the current working directory.
print(find_files(os.getcwd()))