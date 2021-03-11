import os
import requests
import time

os.system("clear||cls")

print("""
########################
   [++] 7OSINT [++]
[!] By sir1usbl4ck [!]
##### SÉTIMA ORDEM #####

[1] Encontrar zonas de DNS.
[2] Encontrar subdominios.
[3] Reverse DNS.
[4] Reverse IP Lookup.
[5] Extrair LINKS de uma pagina web.

""")
op = input("~>")
if op == "2":
	t = input("alvo ~> ")
	req = requests.get("https://api.hackertarget.com/hostsearch/?q={}".format(t))
	resposta = req.text
	print("")
	print(resposta)
	print("")
	print("[+] Subdominios verificados com sucesso! [+]\r\n")

if op == "1":
        t2 = input("alvo ~> ")
        req = requests.get("https://api.hackertarget.com/findshareddns/?q={}".format(t2))
        resposta = req.text
        print("")
        print(resposta)
        print("")
        print("[+] DNS's verificados com sucesso! [+]\r\n")

if op == "3":
        t2 = input("alvo ~> ")
        req = requests.get("https://api.hackertarget.com/reversedns/?q={}".format(t2))
        resposta = req.text
        print("")
        print(resposta)
        print("")
        print("[+] Reversed DNS! [+]\r\n")

if op == "4":
        t2 = input("alvo ~> ")
        req = requests.get("https://api.hackertarget.com/reverseiplookup/?q={}".format(t2))
        resposta = req.text
        print("")
        print(resposta)
        print("")
        print("[+] Reversed IP! [+]\r\n")

if op == "5":
        t2 = input("alvo ~> ")
        req = requests.get("https://api.hackertarget.com/pagelinks/?q={}".format(t2))
        resposta = req.text
        print("")
        print(resposta)
        print("")
        print("[+] LINKS EXTRAIDOS!! [+]\r\n")

