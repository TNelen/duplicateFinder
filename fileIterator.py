import os

path = 'E:\\Music'

def Diff(li1, li2):
    difference = []
    for i in li1:
        if i not in li2:
            difference.append(i)
        else:
            li2.remove(i)
    return difference


def main():
    filecount = 0
    songs = []
    songname = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for dirs in d:
            pathname =r + "\\"+ dirs
            #print(pathname)
            for r2, d2, f2 in os.walk(pathname):
                for file in f2:
                    filecount+=1
                    if '.mp3' in file or '.wav' in file or '.m4a' in file:
                        if ' - ' in file:
                            songname = file.split(" - ")
                            title = songname[1]
                        else:
                            title = file

                        if title.endswith('.mp3' or '.wav' or '.m4a'):
                            title = title[:-4]
                        songs.append(title)

    #print information
    print("number of scanned files")
    print(filecount)

    print("total number of songs")
    print(len(songs))
    
    uniques = set(songs)
    print("number of unique songs")
    print (len(uniques))

    duplicates = Diff(songs, uniques) 
    print("number of duplicates")  
    print (len(duplicates))

    #write duplicate titles to file
    f = open("duplicates.txt", "w")
    
    for title in sorted(duplicates):
        f.write(title + "\n")
    f.close()


    


if __name__ == "__main__":
    main()


        