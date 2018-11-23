import os

# get all file names in dir "./"
#fnames = os.listdir("./")

def get_filefoldnames(dir00):

    fnames = os.listdir(dir00)
    filenames = []
    foldnames = []

    for fname in fnames:
        if os.path.isfile(dir00+fname):
            filenames.append(fname)
        elif os.path.isdir(dir00+fname):
            foldnames.append(fname)
    
#    print filenames
#    print foldnames

    return foldnames, filenames

def get_pvtuNames(filenames):
    pvtu_names = []
    for filename in filenames:
        if ".pvtu" in filename:
            pvtu_names.append(filename)

    return pvtu_names

