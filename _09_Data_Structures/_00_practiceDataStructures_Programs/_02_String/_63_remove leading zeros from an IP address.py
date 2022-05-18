'''
remove leading zeros from an IP address
Topics
CRUD - delete
Type - string
State - input string
behaviour - remove leading zeros

# mathematical approach
step1 - get the input string
step2 - check the leading zeros and remove
step3 - return the output in console
'''
print("1.using the Builtin approach")
print("2.using the algorithm approach")
ip = "123.003.0154"
for i in ip:
    new_ip = ".".join([str(int(i)) for i in ip.split(".")])
    print("After removing lead zeros:", new_ip)
print("3.using the functions approach")


def removezeros(ip):

    new_ip = ".".join([str(int(i)) for i in ip.split(".")])
    return new_ip


ip = "100.020.003.400"
print("input ip address:", ip)
print("After removing leading zeros in ip address:", removezeros(ip))
print("4.using the OOPS approach")


class Remove:
    def __init__(self, ip):
        self.ip = ip

    def get_inputip(self):
        print("input ip:", self.ip)

    def get_removeleadzero(self):
        print("After removing zeros:", removezeros(self.ip))


ip = Remove("001.002.0054.003154")
ip.get_inputip()
ip.get_removeleadzero()
