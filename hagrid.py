#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:47:55 2021

@author: Fatima
"""

import matplotlib.pyplot as plt
##import speedtest library
import speedtest
##import time library
import time 


##create an array to store download speed, keep it empty
list_download_speed =[]
##create an array to store upload speed, keep it empty
list_upload_speed =[]


#create a for loop which iterates 5 times
for i in range(5):
    
    ####access the class Speedtest() using the object speedtest, and assign it to a variable st
    st = speedtest.Speedtest()
    
    ##access the function st.download(), divide it by 1000000 to convert to Mb, reduce it to 2 decimal places using round() function
    download_speed = round( st.download()/1000000,2)
    

    ##show the calculated download speed appended with "mbps" in the list_download_speed
    list_download_speed.append(download_speed)
    
    ##repeat the same for upload_speed
    upload_speed = round( st.upload()/1000000,2)
    
    ##show the calculated upload_speed appended with "mbps" in the list_upload_speed
    list_upload_speed.append(upload_speed)
    ##run the loop for every 60 seconds interval using time.sleep(n)
    time.sleep(60)
    
    print(list_download_speed)
    print(list_upload_speed)

##Create a list named x, store the values 1 to 5 inside it    
x = [1,2,3,4,5]   

## plot the download speed on the x axis of the graph using plt.plot()
plt.plot(x, list_download_speed, label = "Download speed") 

##give the title for the graph as 'Speed' 
plt.title('speed') 

##plot the upload speed on the x axis of the graph using plt.plot()
plt.plot(x, list_upload_speed,label="Upload Speed") 

##Add a legend to the plot using 'plt. '
plt.legend()
##The legend will tell you which line graph represents download speed 
##and which line graph represents upload speed 


plt.show() 
