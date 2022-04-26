# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
sys.path.append(r'/firsttest.py')
import firsttest

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi('hi OUYANG Mingxuan')
    oymx = firsttest.People('OUYANG Mingxuan')
    oymx.work()
    oymx.sleep()
    print("good job")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
