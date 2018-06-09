# !/usr/bin/env python
# coding: utf-8
import re , sys , os 
import socket
from platform import system
from urllib2 import urlopen



if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')




host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
public_ip = urlopen('http://ip.42.pl/raw').read()   
                      
 

banner = ''' 
#================================================================#        
                                                                          
   ____            _ _     _                 _   _  ___    _  
 |  _ \          | | |   | |               | | | |/ / |  | | 
 | |_) | __ _  __| | |__ | | ___   ___   __| | | ' /| |__| | 
 |  _ < / _` |/ _` | '_ \| |/ _ \ / _ \ / _` | |  < |  __  | 
 | |_) | (_| | (_| | |_) | | (_) | (_) | (_| | | . \| |  | | 
 |____/ \__,_|\__,_|_.__/|_|\___/ \___/ \__,_| |_|\_\_|  |_| 
                                                             
                                                                  

	                Name : Venom X                                           
	                Coder By : Badblood KH                                    
	                Telegram :  https://t.me/mrspy17                         
                                                                                                                                                       
#================================================================#
       
\n'''


print banner

print "==================================================="
print"[!] Host Attacker :  ",host_name  
print"[!] LocalHost : ",host_ip            
print"[!] External IP : ",public_ip  
print "==================================================="
 


def ManingBing():
 try:
	lists = open(sys.argv[1], 'r').readlines()
	for ips in lists:
	 ip = ips.rstrip()	
	 page = 1
	 while page <= 101:
	  bing = "http://www.bing.com/search?q=ip%3A"+ip+"&count=50&first="+str(page)
	  openbing  = urllib2.urlopen(bing, timeout = 5)
	  readbing = openbing.read()
	  site =  re.findall('<h2><a href="((?:https://|http://)[a-zA-Z0-9-_]+\.*[a-zA-Z0-9][a-zA-Z0-9-_]+\.[a-zA-Z]{2,11})', readbing)
	  page += 101
	  print "[>] Grabbing IP Server ====> ", ip,"\n",  
	  print "\n".join(site)+"\n" 
	  open('Binged.txt', "a").write("\n".join(site)+"\n")
 except:
  pass

ManingBing()

