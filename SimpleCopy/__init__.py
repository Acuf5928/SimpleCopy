from SimpleCopy import code_copy, code_move


def copy(copyFrom: str, copyTo: str, copyType: bool):
    code_copy.copy(copyFrom, copyTo, copyType)


def move(moveFrom: str, moveTo: str, moveType: bool):
    code_move.move(moveFrom, moveTo, moveType)
