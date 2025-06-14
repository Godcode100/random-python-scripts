import os
extensions =[".py",".txt",".jpg"]
for extension in extensions:
    print("here are the extensions for: ",extension)
    for path,folder,files in os.walk('.'):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(path,file))