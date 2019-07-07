from socket import *
import Calculate                     #
import Trilateration
def Setting(ip,port):
    serverSock = socket(AF_INET, SOCK_STREAM)
    print("소켓시작")
    serverSock.bind((ip, port))
    print("bind")
    serverSock.listen(1)
    print("listen")

    while(1):
        connectionSock, addr = serverSock.accept()

        print(str(addr),'에서 접속이 확인되었습니다.')
    
        data = connectionSock.recv(1024).decode()
        data_2 = Calculate.in_data(data)
        data_2 = data_2.split(",")
        data_3 = Trilateration.Trilateration(data_2) # 삼변측량알고리즘 적용
        return data_3 #위치좌표 X,Y반

