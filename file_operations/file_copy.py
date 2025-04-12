import os
import shutil

# def copy_files(file_path):
#     source_file = os.path.join(file_path,'new_file_1.txt')
#     destination_file = os.path.join(file_path,'copy_text.txt')
#     try:
#         with open(source_file,'r') as f:
#             content = f.readlines()
#         with open(destination_file,'w') as f:
#             f.writelines(content)

#     except Exception as e:
#         print(e)

#     with open(destination_file,'r') as f:
#         new_content = f.readlines()

#     return new_content

def copy_file_operation(file_path):

    source_file = os.path.join(file_path,'sample.txt')
    destination_file = os.path.join(file_path,'new_copy_file.txt')

    try:
        shutil.copy(source_file,destination_file)

    except Exception as e:
        print(e)
        return None
    
    with open (destination_file,'r') as f:
        content = f.readlines()

    return content

print(copy_file_operation('/workspaces/Python_Projects/file_operations/'))