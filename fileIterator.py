import os

path = 'E:\\Music\\FAVS'

def main():
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.mp3' in file:
                files.append(os.path.join(r, file))

    for f in files:
        print(f)
    



if __name__ == "__main__":
    main()


        