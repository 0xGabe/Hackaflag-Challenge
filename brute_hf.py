import sys
import requests

def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

prLightPurple(""""                                                         
 @@@@@@   @@@  @@@@@@@@@@   @@@@@@@   @@@       @@@@@@@@  
@@@@@@@   @@@  @@@@@@@@@@@  @@@@@@@@  @@@       @@@@@@@@  
!@@       @@!  @@! @@! @@!  @@!  @@@  @@!       @@!       
!@!       !@!  !@! !@! !@!  !@!  @!@  !@!       !@!       
!!@@!!    !!@  @!! !!@ @!@  @!@@!@!   @!!       @!!!:!    
 !!@!!!   !!!  !@!   ! !@!  !!@!!!    !!!       !!!!!:    
     !:!  !!:  !!:     !!:  !!:       !!:       !!:       
    !:!   :!:  :!:     :!:  :!:        :!:      :!:       
:::: ::    ::  :::     ::    ::        :: ::::   :: ::::  
:: : :    :     :      :     :        : :: : :  : :: ::   
                                                          
                                                          
@@@@@@@   @@@@@@@   @@@  @@@  @@@@@@@  @@@@@@@@           
@@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@  @@@@@@@@           
@@!  @@@  @@!  @@@  @@!  @@@    @@!    @@!                
!@   @!@  !@!  @!@  !@!  @!@    !@!    !@!                
@!@!@!@   @!@!!@!   @!@  !@!    @!!    @!!!:!             
!!!@!!!!  !!@!@!    !@!  !!!    !!!    !!!!!:             
!!:  !!!  !!: :!!   !!:  !!!    !!:    !!:                
:!:  !:!  :!:  !:!  :!:  !:!    :!:    :!:                
 :: ::::  ::   :::  ::::: ::     ::     :: ::::           
:: : ::    :   : :   : :  :      :     : :: ::            
""")

if len(sys.argv) <= 3 | len(sys.argv) >= 3:
    prRed("[-] How to use -> python3 http://site.com user.txt password.txt")
else:
    url = sys.argv[1]
    data = {"login": sys.argv[2], "Password": sys.argv[3], "Submit": "Login"}
    res = requests.post(url, data)
    print(res.text)

#TO DO:

#file01 = open('user.txt', 'r')
#fileUser = file.readlines()

#file02 = open('password.txt', 'r')
#filePassword = file02.readlines()
