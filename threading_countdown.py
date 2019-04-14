#!/usr/bin/env python
# coding: utf-8

# In[55]:


__author__ = "Ganesh Chandrasekaran"
__license__ = "Open Source GPL"
__version__ = "1.0"
__status__ = "Development"
__description__ = "Code to demonstrate Threading concept"

import threading
import datetime

th_lst = []
def fn_countdown(thread,count):
    while count > 0:
        currentts = datetime.datetime.now()
        addtolist(str(currentts),thread,count)
        print ("timestamp : {} -> {} - {} | ".format(currentts,thread, count))
        count -= 2
        time.sleep(2)
    return

def main():
    #threading t1 and t2

    thread1 = threading.Thread(target=fn_countdown,args=('Even Thread',20))
    thread1.start()

    thread2 = threading.Thread(target=fn_countdown,args=('Odd Thread',19))
    thread2.start()

def addtolist(ts,thread,count):
    th_lst.append((ts,thread,count))
    
    
if __name__ == '__main__':
    main()   


# In[ ]:




