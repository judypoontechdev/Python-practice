# **Task description**
# Reads a file name input and maps its extension to the corresponding HTTP 
# media type (MIME type, e.g., `image/jpeg`, `application/pdf`), defaulting 
# to `application/octet-stream` for unknown extensions.

def main():
    # Prompt user for file name and convert to lowercase for case-insensitive match
    file_name = input('What is the name of file? ').lower().strip()
    extensions(file_name)

# Check file extension and output the corresponding media type
def extensions(f):
    if f.endswith('.gif'):
        print('image/gif')
    elif f.endswith(('.jpg', '.jpeg')):
        print('image/jpeg')
    elif f.endswith('.png'):
        print('image/png')
    elif f.endswith('.pdf'):
        print('application/pdf')
    elif f.endswith('.txt'):
        print('text/plain')
    elif f.endswith('.zip'):
            print('application/zip')
    else:
        print('application/octet-stream')

main()
