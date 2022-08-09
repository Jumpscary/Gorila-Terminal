# Importes:
import os, time
from datetime import datetime
import colorama as c



# Colores:
red = c.Fore.RED
blue = c.Fore.BLUE
green = c.Fore.GREEN
reset = c.Fore.RESET


# Clear Console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


# Banner
def banner():
    clearConsole()
    print(f"""
{red}  
  _______   ______   .______       __   __          ___      
 /  _____| /  __  \  |   _  \     |  | |  |        /   \     
|  |  __  |  |  |  | |  |_)  |    |  | |  |       /  ^  \    
|  | |_ | |  |  |  | |      /     |  | |  |      /  /_\  \   
|  |__| | |  `--'  | |  |\  \----.|  | |  `----./  _____  \  
 \______|  \______/  | _| `._____||__| |_______/__/     \__\ 
                                                  """)



# Command
def command():
    day = datetime.today()
    banner()
    execute = input(f"""
    {red}

╔═══════════[{green} G O R I L A - T E R M I N A L {red}]
| ~ {blue} {day}  {red}
╚═══════════════> {reset}""")
    print(f"{red}╚═══════════════> ", f"|{reset}",os.system(execute))
    time.sleep(2)


    
# Loop
for x in range(9999999999):
    command()

