def hanoi(frm,to,via,n):
    if n==1:
        print(frm,to)
    else:
        hanoi(frm,via,to,n-1)
        hanoi(frm,to,via,1)
        hanoi(via,to,frm,n-1)
hanoi('A','B','C',3)
