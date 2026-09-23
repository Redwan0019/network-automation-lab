from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

devices = [{

    "device_type":"cisco_ios",
    "host":"devnetsandboxiosxec8k.cisco.com",
    "username":"redwanabdurhmanlilay",
    "password":"Q-poJ27vh2_WR",


},

]

commands =["show version", "show ip interface brief" , " show vlan brief"]

success_count = 0
fail_count= 0

for device in devices:
    try:
        connection = ConnectHandler(**device)
        filename =f"{device['host']}.txt"
        with open(filename,"w")as f:
            for command in commands:
                output = connection.send_command(command)
                f.write(f"====={command}=====\n")
                f.write(output+"\n\n")

        connection.disconnect()
        success_count = success_count+1
        print(f"SUCESS:{device['host']}")  
    except NetmikoAuthenticationException:
        fail_count=fail_count+1
        print(f"Faild (bad cridanntials):{device['host']}")
    except NetmikoTimeoutException:
        fail_count=fail_count+1
        print(f"FAILD (unrechable):{device['host']}")

    print(f"\n{success_count} succeeded, {fail_count} faild")