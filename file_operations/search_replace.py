import os
import re

def search_replace(file_path,search_text,replace_text):

    source_file = os.path.join(file_path,'sample.txt')
    destination_file = os.path.join(file_path,'replace_1.txt')
    try:
        with open(source_file,'r') as f:
            content = f.read()

        # updated_content = content.replace(search_text,replace_text)
        updated_content = re.sub(search_text,replace_text,content)

        with open(destination_file,'w') as f:
            f.writelines(updated_content)
    except Exception as e:
        print(e)

    return destination_file


print(search_replace('/workspaces/Python_Projects/file_operations/','and','or'))

    



