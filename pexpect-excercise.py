import pexpect
import sys

# R1 Configuration
R1_ip = "172.31.108.3"
USERNAME = "admin" 
PASSWORD = "cisco" 
R1_command = 'ip address 172.16.1.1 255.255.255.255'

# Connect to R1
try:
    child = pexpect.spawn(f'telnet {R1_ip}')
    child.expect('Username:')
    child.sendline(USERNAME)  
    child.expect('Password:')
    child.sendline(PASSWORD)  
    child.expect('#')
except pexpect.ExceptionPexpect as e:
    print(f"Error connecting to router R1: {e}")
    sys.exit(1)

child.sendline('conf t')
child.expect(r'\(config\)#')
child.sendline('int loopback 0')
child.expect(r'\(config-if\)#')
child.sendline(R1_command)
child.expect(r'\(config-if\)#')
print(f"Loopback0 172.16.1.1 is created on {R1_ip}")

# R2 Configuration
R2_ip = "172.31.108.4"
R2_command = 'ip address 172.16.2.2 255.255.255.255'

# Connect to R2
try:
    child = pexpect.spawn(f'telnet {R2_ip}')
    child.expect('Username:')
    child.sendline(USERNAME)  
    child.expect('Password:')
    child.sendline(PASSWORD)  
    child.expect('#')
except pexpect.ExceptionPexpect as e:
    print(f"Error connecting to router R2: {e}")
    sys.exit(1)

child.sendline('conf t')
child.expect(r'\(config\)#')
child.sendline('int loopback 0')
child.expect(r'\(config-if\)#')
child.sendline(R2_command)
child.expect(r'\(config-if\)#')
print(f"Loopback0 172.16.2.2 is created on {R2_ip}")
