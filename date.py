class Date(object):
    def setdate(self,date):
        self.date=date
    def setmonth(self,month):
        self.month=month
    def setyear(self,year):
        self.year=year
    def getdate(self):
        return self.date
    def getmonth(self):
        return self.month
    def getyear(self):
        return self.year
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
    month_arr=['None','Jan','Feb','March','Apr','May','Jun','Jul','Aug','Sep']
    def __str__(self):
        date=str(self.date)
        year=str(self.year)
        month=self.month_arr[self.month]
        st=date+' '+month+' '+year
        return st
D=Date(20,1,2017)
print(D)
print(D.getmonth())        
