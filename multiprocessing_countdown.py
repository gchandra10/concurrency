#!/usr/bin/env python
# coding: utf-8

# In[15]:


__author__ = "Ganesh Chandrasekaran"
__license__ = "Open Source GPL"
__version__ = "1.0"
__status__ = "Development"
__description__ = "Code to demonstrate MultiProcessing concept"

import datetime
import multiprocessing

class fn_Countdown(multiprocessing.Process):
    def __init__(self,processname,count):
        multiprocessing.Process.__init__(self)
        self.count = count
        self.processname = processname
        
    def run(self):
        while self.count > 0:
            currentts = datetime.datetime.now()
            print ("timestamp : {} -> {} - {} | ".format(currentts,self.processname,self.count))
            self.count -= 2
            time.sleep(2)
        return

if __name__ == '__main__':
   process1 = fn_Countdown('Even Process ', 20)
   process1.start()                

   process2 = fn_Countdown('Odd Process ',19)
   process2.start()


# In[ ]:





# In[ ]:




