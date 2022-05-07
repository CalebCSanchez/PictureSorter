import os
import PictureSorter

directory = 'D:\VSCode\Projects\PictureSorter\Images'

def fileParser(directory):
    for filename1 in os.listdir(directory):
        file1 = os.path.join(directory, filename1)
        if os.path.isfile(file1):
            filetype = file1.split('.')[-1]
            if (filetype == 'jpeg' or filetype == 'png' or filetype == 'jpg'):
                for filename2 in os.listdir(directory)[os.listdir(directory).index(filename1) + 1:len(os.listdir(directory))]:
                    file2 = os.path.join(directory, filename2)
                    if (file1 == file2):
                        pass
                    filetype2 = file2.split('.')[-1]
                    if (filetype2 == 'jpeg' or filetype2 == 'png' or filetype2 == 'jpg'):
                        result = PictureSorter.pictureSorter(file1,file2)
                        if (result >= 95):
                            df = input("Would you like to delete "+file2+ ": (y/n)")
                            if df == 'y':
                                os.remove(file2)
                                break

                        if (result >= 85):
                            print (filename1)
                            print (filename2)
                            print(result)

                pass
            else:
                print('File ' + file1 + ' is not compatible')
            

fileParser(directory)


