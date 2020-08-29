import os
from glob import glob


def zip(copyFrom, copyTo):
    import zipfile

    if copyFrom[-1] != os.sep:
        copyFrom += os.sep

    # recupero la lista file e cartelle da zippare
    dirlist = glob(copyFrom + "**", recursive=True)

    # creo il file zip
    zip_name = zipfile.ZipFile(file=copyTo, mode='w', compression=14)

    # aggiungo i file e cartelle al file zip
    for file in dirlist:
        if file != copyTo:
            zipfile = file.replace(copyFrom, "")

            try:
                zip_name.write(file, zipfile)
            except Exception:
                pass