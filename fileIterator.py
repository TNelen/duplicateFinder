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
    songs = []
    songname = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        #print(d)
        print(len(songs))
        for dirs in d:
            pathname =r + "\\"+ dirs
            print(pathname)
            for r2, d2, f2 in os.walk(pathname):
                for file in f2:
                    if '.mp3' in file:
                        if ' - ' in file:
                            songname = file.split(" - ")
                            title = songname[1]
                        else:
                            title = file

                        if title.endswith('.mp3'):
                            title = title[:-4]
                        songs.append(title)



    for f in songs:
        print(f)
    print("total number of songs")
    print(len(songs))
    
    uniques = set(songs)
    print("number of unique songs")
    print (len(uniques))

    duplicates = Diff(songs, uniques) 
    print("number of duplicates")  
    print (len(duplicates))
    print("duplicates:")
    f = open("duplicates.txt", "a")
    for song in duplicates:
        f.write(song + "\n")
    f.close()


    


if __name__ == "__main__":
    main()


        