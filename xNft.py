import os
import requests
import colorama

colorama.init(convert=True)

R = colorama.Fore.RED
G = colorama.Fore.GREEN
B = colorama.Fore.BLUE
C = colorama.Fore.CYAN
X = colorama.Fore.RESET

def main():
    print(f'''{C}
              _   _  __ _   
             | \ | |/ _| |  
        __  _|  \| | |_| |_ 
        \ \/ / . ` |  _| __|
         >  <| |\  | | | |_ 
        /_/\_\_| \_|_|  \__|

        Author: Lexxrt
        Github: https://github.com/Lexxrt
    {X}''')

    for code in range(0, 10000):
        filename = f'cryptopunk{str(code).zfill(4)}.png'
        with open(f'./output/{filename}', 'wb') as out:
            try:
                data = requests.get(f'https://www.larvalabs.com/cryptopunks/cryptopunk{str(code).zfill(4)}.png').content
                out.write(data)
                print(f'{B}[+] Getting: https://www.larvalabs.com/cryptopunks/cryptopunk{str(code).zfill(4)}.png{X}')
            except Exception as ex:
                print(f'{R}[!] Exception: {str(ex)}{X}')
                print(f'{R}[!] Failed: https://www.larvalabs.com/cryptopunks/cryptopunk{str(code).zfill(4)}.png{X}')

if __name__ == '__main__':
    try:
        if os.path.exists('./output'):
            pass
        else:
            os.mkdir('output')

        main()
    except:
        pass
