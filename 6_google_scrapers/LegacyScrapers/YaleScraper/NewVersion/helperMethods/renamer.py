
import os

SAVE_TO_DIRECTORY = "/home/myanime/Desktop/0/"
for x in range (0, 2000):
    try:
        docName = str(x)
        os.chdir(SAVE_TO_DIRECTORY)
        files = filter(os.path.isfile, os.listdir(SAVE_TO_DIRECTORY))
        files = [os.path.join(SAVE_TO_DIRECTORY, f) for f in files] # add path to each file
        files.sort(key=lambda x: os.path.getmtime(x))
        newest_file = files[x]
        os.rename(newest_file, docName+".csv")
    except:
        pass
print "Done"
