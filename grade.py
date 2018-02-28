def converttoGrade(mark):
    if mark>=0 and mark<=49:
        gr='F'
    elif mark<=59:
        gr='D'
    elif mark<=69:
        gr='C'
    elif mark<=79:
        gr='B'
    elif mark<=100:
        gr='A'
    else:
        gr='X'
    return gr
print(converttoGrade(76))
