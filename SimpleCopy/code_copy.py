import os
import shutil

from SimpleCopy import code_zip


def copy(copyFrom: str, copyTo: str, copyType: bool):
    if not os.path.exists(copyFrom):
        raise Exception

    if os.path.isdir(copyTo):
        copyTo = copyTo + os.sep + copyFrom.split(os.sep)[-1]

    if os.path.exists(copyTo):
        if copyType is True:
            pass
        if copyType is None:
            raise Exception
        if copyType is False:
            name = copyTo.split(os.sep)[-1]
            destinationPath = copyTo.replace(name, "")

            if len(copyTo.split(os.sep)[-1].split(".")) != 1:
                nameExt = "." + name.split(".")[-1]
            else:
                nameExt = ""

            namePrefix = name.split(".")[0]

            n = 0

            while os.path.exists(copyTo):
                n += 1
                copyTo = destinationPath + namePrefix + " (" + str(n) + ")" + nameExt

    if os.path.isdir(copyFrom) and len(copyTo.split(os.sep)[-1].split(".")) != 1:
        code_zip.zip(copyFrom, copyTo)

    elif os.path.isfile(copyFrom):
        shutil.copy2(copyFrom, copyTo)

    elif os.path.isdir(copyFrom):
        shutil.copytree(copyFrom, copyTo)
