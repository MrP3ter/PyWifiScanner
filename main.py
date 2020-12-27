from wifi import Cell,Scheme
import os
def function_program():
    cell = Cell.all('wlan0')[0]
    scheme = Scheme.for_cell('wlan0', 'home', cell)
    scheme.save()
    scheme.activate()
    scheme = Scheme.find('wlan0', 'home')
    scheme.activate()

def main():
    print("Welcome To PyWifi")
    print("This is my first Script Created In Python")
    InputUser = input("Run the Script?:")
    if InputUser == 1:
        function_program()
    elif InputUser == 2:
        os.kill()
main()
