#!usr/bin/python
import webbrowser
import codecs
import time
import os

with open ("urls_hentai.txt") as fp:
    num =1
    for ebayno in fp:
        with open ("urls_hentai.txt" , "r") as r:
            url = ''+ ebayno.strip()
            lines = r.readlines()
            time.sleep(20)
            webbrowser.open(url)
            num += 1
            print(num)
            if num == 10:
                os.system('taskkill /F /IM MicrosoftEdge.exe')
                print('close browser')
                with open('urls_hentai.txt', 'w') as w:
                    for l in lines:
                        if url not in l:
                            w.write(l)