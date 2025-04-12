import os

def parse_content(file):
    file_path_1 = os.path.join(file,'sample.txt')
    with open(file_path_1,'r') as f:

        content_1 = f.readlines()

        

    file_path_2 = os.path.join(file,'new_file_1.txt')
    try:

        with open(file_path_2,'w') as f:
            content_write = f.writelines(content_1)
    except Exception as e:
        print(e)

    with open(file_path_2,'r') as f:

        content_2 = f.readlines()

    line_count = len(content_1)
 # word_count = sum(len(line.split()) for line in content_1)
    word_count =0
    sum=0
    for line in content_1:
        sum +=len(line.split())

    word_count = sum


        



    return content_2,line_count,word_count


print(parse_content('/workspaces/Python_Projects/file_operations/'))