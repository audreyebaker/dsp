date_start = '01-02-2013'    
date_stop = '07-28-2015'

from datetime import datetime

def days_between(d1, d2):
     d1 = datetime.strptime(d1, '%m-%d-%Y')
     d2 = datetime.strptime(d2, '%m-%d-%Y')
     answer = abs((d2-d1).days)
     print(str(answer)+ ' days')
     return answer
    

date_start2 = '12312013'  
date_stop2 = '05282015'  

def days_between2(d1, d2):
     d1 = datetime.strptime(d1, '%m%d%Y')
     d2 = datetime.strptime(d2, '%m%d%Y')
     answer = (abs((d2-d1).days))
     print(str(answer)+ ' days')
     return answer
 
date_start3 = '15-Jan-1994'      
date_stop3 = '14-Jul-2015'  

def days_between3(d1, d2):
     d1 = datetime.strptime(d1, '%d-%b-%Y')
     d2 = datetime.strptime(d2, '%d-%b-%Y')
     answer = abs((d2-d1).days)
     print(str(answer)+ ' days')
     return answer

days_between(date_start, date_stop)
days_between2(date_start2, date_stop2)
days_between3(date_start3, date_stop3)
