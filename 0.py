check = check_key_api(key)
check = check_key_vip(key)

import os
def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b != 0:
        return a / b
    else:
        return "Không thể chia cho 0!"
os.system("cls" if os.name == "nt" else "clear")
def main():
    # Banner
    print("\033[1;33m██████╗░██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░")
    print("\033[1;35m██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░")
    print("\033[1;36m██████╔╝╚██╗░██╔╝░░░██║░░░██║░░██║██║░░██║██║░░░░░")
    print("\033[1;37m██╔══██╗░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░")
    print("\033[1;32m██║░░██║░░╚██╔╝░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗")
    print("\033[1;31m╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝\n")
    print("\033[1;97mTool By: \033[1;32mDUY KHÁNH            \033[1;97mPhiên Bản: \033[1;32mV4")
    print("\033[97m════════════════════════════════════════════════")
    print("\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;95m BOX ZALO\033[1;31m : \033[1;36mhttps://zalo.me/g/nguadz335")
    print("\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;93m YOUTUBE\033[1;31m : \033[1;32mREVIEWTOOL247NK")
    print("\033[1;97m[\033[1;91m<>\033[1;97m]\033[1;32m ADMIN\033[1;31m : \033[1;33mDUYKHANH")
    print("\033[97m════════════════════════════════════════════════\n")

    # Menu
    print("\033[1;34mChọn phép tính:")
    print("\033[1;36m1. Cộng")
    print("\033[1;36m2. Trừ")
    print("\033[1;36m3. Nhân")
    print("\033[1;36m4. Chia")
    print("\033[1;36m5. Thoát")

    while True:
        choice = input("\033[1;33mNhập số (1-5): \033[0m")
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("\033[1;32mNhập số thứ nhất: \033[0m"))
            num2 = float(input("\033[1;32mNhập số thứ hai: \033[0m"))

            if choice == '1':
                print(f"\033[1;97m{num1} + {num2} = \033[1;32m{cong(num1, num2)}\033[0m")
            elif choice == '2':
                print(f"\033[1;97m{num1} - {num2} = \033[1;32m{tru(num1, num2)}\033[0m")
            elif choice == '3':
                print(f"\033[1;97m{num1} * {num2} = \033[1;32m{nhan(num1, num2)}\033[0m")
            elif choice == '4':
                print(f"\033[1;97m{num1} / {num2} = \033[1;32m{chia(num1, num2)}\033[0m")
        
        elif choice == '5':
            print("\033[1;31mThoát chương trình. Tạm biệt!\033[0m")
            break
        
        else:
            print("\033[1;31mLựa chọn không hợp lệ! Vui lòng thử lại.\033[0m")

if __name__ == "__main__":
    main()
