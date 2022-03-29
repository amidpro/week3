import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')



# TODO: Use the glob.glob() function to obtain the list of filenames
file_name = "/Users/getintotech/"
file_list = glob.glob("/Users/getintotech/Desktop/*")
# print(file_list)

for file_name in file_list:
    if os.path.getsize(file_name)>0:
        print(os.path.getsize(file_name), file_name)


# basename having difficulties

# TODO: use os.path.getsize to find each file's size

# for path in file_list:
#     print(os.path.getsize(path))

# for name in pattern:
# print (os. path)
# changed because of variables


# TODO: Add a test to only display files that are not zero length

# if os.stat(path).st_size == 0:
#     print('File is empty')
# else:
#     print('File is not empty')

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

