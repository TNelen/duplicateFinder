import os


def Diff(li1, li2):
    difference = []
    for i in li1:
        if i not in li2:
            difference.append(i)
        else:
            li2.remove(i)
    return difference


def main():

    path = 'E:\\Music'
    filecount = 0
    songs = []
    songname = []
    info = {}
    dup_info = {}
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
                for file in f:
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
                        path = os.path.join(r,file)
                        info[path] = title


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

    unique_duplicates = set(duplicates)
    for song in sorted(unique_duplicates):
        for i,j in info.items():
            if j ==song:
                dup_info[i] = j 

    #write duplicate titles to file
    f = open("duplicates.txt", "w")
    for i,j in dup_info.items():
        length = len(j)
        j=j.ljust(60)
        f.write(j + i + "\n")
    f.close()



if __name__ == "__main__":
    main()


        