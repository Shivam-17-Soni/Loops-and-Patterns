import os

def createIfNotExist(folder):
    if not os.path.exists(folder):   #if folder doesnot exist it wil make it.
        os.makedirs(folder)

def move(folderName,files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

if __name__=="__main__":
    
    files = os.listdir()
    files.remove("folder_clutter.py")

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')

    imgExts=[".png",".jpg","jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]
    move("Images",images)

    docExts=[".txt",".docx","doc",".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts ]
    move("Docs",docs)

    mediaExts=[".mp4",".mp3",".flv"]
    medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaExts ]
    move("Media",medias)

    others = []
    for file in files:
        ext=os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and os.path.isfile(file):
            others.append(file)

    move("Others",others)