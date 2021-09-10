
import os
def toplamsay():

   say= os.system('dpkg -l | wc -l')
   print(str(say)"adet kurulu ")

toplamsay()