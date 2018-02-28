def hanoi(frm,to,via,n):
    if n==1:
        print(frm,to)
    else:
        hanoi(frm,via,to,n-1)
        hanoi(frm,to,via,1)
        hanoi(via,to,frm,n-1)
#def ls_curse(l,n):
 #   if n==1:
                
#ls_curse([1,2,3,4,5],2)
class movie(object):
    def __init__(self,title,dir_name,genre,rating):
        self.title=title
        self.dir_name=dir_name
        self.genre=genre
        self.rating=rating
    def getttl(self):
        return self.title
    def getnm(self):
        return self.dir_name
    def getgn(self):
        return self.genre
    def getrating(self):
        return self.rating
    def setttl(self,tt):
        self.title=tt
    def setnm(self,dname):
        self.dir_name=dname
    def setgn(self,gen):
        self.genre=gen
    def setrating(self,rating):
        self.rating=rating
m1=movie("abc","def","a",1)
m2=movie("abd","deg","b",2)
m3=movie("abe","deh","d",4)
m4=movie("abf","dei","c",3)
l1=[m1,m2,m3,m4]
l1.sort(key=l1[0].getrating())
print(l1)
