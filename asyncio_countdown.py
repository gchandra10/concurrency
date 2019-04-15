
__author__ = "Ganesh Chandrasekaran"
__license__ = "Open Source GPL"
__version__ = "1.0"
__status__ = "Development"
__description__ = "Code to demonstrate AsyncIO concept"

import datetime
import time
import asyncio

# definition of a coroutine for odd counter 
async def fn_coroutine_1(oddcounter):
    while oddcounter > 0:
        currentts = datetime.datetime.now()
        print ("timestamp : {} -> {} - {} | ".format(currentts,'odd',oddcounter))
        oddcounter -= 2
        await asyncio.sleep(2)
    return

# definition of a coroutine for even counter 
async def fn_coroutine_2(evencounter):
    while evencounter > 0:
        currentts = datetime.datetime.now()
        print ("timestamp : {} -> {} - {} | ".format(currentts,'even',evencounter))
        evencounter -= 2
        await asyncio.sleep(2)
    return
     

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # schedule both the coroutines to run on the event loop
    loop.run_until_complete(asyncio.gather(fn_coroutine_1(19), fn_coroutine_2(20)))