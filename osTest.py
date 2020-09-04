import os

print(os.system("dir"))

cmd = input("화면을 지우시겠습니까? ")
if cmd == "Y" or "y":
    os.system("cls")