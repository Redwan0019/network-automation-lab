from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException,NetmikoAuthenticationException
from datetime import datetime

def get_devices():
    return [{
            "device_type":"cisco_ios",
            "host":"devnetsandboxiosxec8k.cisco.com",
            "username":"redwanabdurhmanlilay",
            "password":"Q-poJ27vh2_WR",
    },
       
           
]

def get_commands():
    return ["show running-config"]


def buckup_devices():
    devices =get_devices()
    commands =get_commands()
    success_count =0
    fail_count =0

    for device in devices:
        try:
            connection=ConnectHandler(**device)
            timestamp = datetime.now().strftime("%y-%m-%d_%h-%m")
            filename = f"{device['host']}_{timestamp}.txt"

            with open(filename,"w")as f:
                for command in commands:
                    output = connection.send_command(command)
                    f.write(output)

            connection.disconnect()
            success_count =success_count +1
            print(f"BACKUP SUCCESS:{device['host']}")
        except NetmikoAuthenticationException:
            fail_count =fail_count+1
            print(f"FAILD (bad credentials): {device['host']}")
        except NetmikoTimeoutException:
            fail_count = fail_count+1
            print(f"FAILD (unrechable):{device['host']}")

    print(f"\n{success_count} suceeded,{fail_count} failed")




if __name__ == "__main__":
        buckup_devices()