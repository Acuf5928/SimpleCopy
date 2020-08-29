import os
import shutil

from SimpleCopy import code_zip


def move(moveFrom: str, moveTo: str, moveType: bool):
    if not os.path.exists(moveFrom):
        raise Exception

    if os.path.isdir(moveTo):
        moveTo = moveTo + os.sep + moveFrom.split(os.sep)[-1]

    if os.path.exists(moveTo):
        if moveType is True:
            pass
        if moveType is None:
            raise Exception
        if moveType is False:
            name = moveTo.split(os.sep)[-1]
            destinationPath = moveTo.replace(name, "")

            if len(moveTo.split(os.sep)[-1].split(".")) != 1:
                nameExt = "." + name.split(".")[-1]
            else:
                nameExt = ""

            namePrefix = name.split(".")[0]

            n = 0

            while os.path.exists(moveTo):
                n += 1
                moveTo = destinationPath + namePrefix + " (" + str(n) + ")" + nameExt

    if os.path.isdir(moveFrom) and len(moveTo.split(os.sep)[-1].split(".")) != 1:
        code_zip.zip(moveFrom, moveTo)
        shutil.rmtree(moveFrom)

    else:
        shutil.move(moveFrom, moveTo)
