import os
def Spoof_extension(from_file,to_ext):
    pth  = from_file.replace(from_file.split(os.path.sep)[-1],"")
    name = from_file.split(os.path.sep)[-1].split(".")[0]
    ex   = from_file.split(os.path.sep)[-1].split(".")[1]
    new = name+u"\u202E"+to_ext+"."+ex
    new_with_path = pth + os.path.sep + new
    try:
        os.rename( from_file, new_with_path )
        if os.path.isfile(new_with_path):
            return True
    except Exception as e:
        return False
