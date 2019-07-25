from getdata_firebase import get_data
from getdata_firebase import make_DB


def set_data(data):

    rssi_list =[x for x in range(len(data))]

    for i in range(len(data)):
        rssi_list[i] = data[i].split(", ")

    return rssi_list

# 후보정하기 - 타입맞추기
def transform(enterData):
    for i in range(len(enterData)):
        enterData[i] = abs(int(float(enterData[i])))

    return enterData


#후보정하기
def set_Subdata(mobile_data,rssi_list, location_list):
    errorRange = 5;bestIndex = 0     # 오차허용범위, 큰값 인덱
    
    #x = [77,63,72]
    x = mobile_data
    data = rssi_list
    subData = []    #후보리스트
    sublocationData = []    #후보좌표리스트

    #큰값 인덱스 정하기
    for i in range(len(x)):
        if x[i] == max(x):
            bestIndex = i

    #후보정하기
    for i in range(len(data)):
        enterData_1 = data[i]
        location_Data = location_list[i]
        if max(x) - errorRange < abs(int(float(enterData_1[bestIndex]))) and max(x) + errorRange > abs(int(float(enterData_1[bestIndex]))):
            enterData = transform(enterData_1)
            subData.append(enterData)
            sublocationData.append(location_Data)


    return x,subData,sublocationData

# 유사도 계산하기
def check_similar(mobile_data,subData,subLocation):

    similar_number = []
    
    for i in range(len(subData)):
        Distance=0
        for j in range(3):
            Distance += abs(mobile_data[j] - subData[i][j])
        if(Distance < 30):
            similar_number.append(i)
        
    return similar_number

#좌표 출력하기
def print_location(similar_num,subLocation):

    X=0;Y=0
    
    for i in similar_num:
        X += float(subLocation[i][0])
        Y += float(subLocation[i][2])

    X = X/len(similar_num)
    Y = Y/len(similar_num)

    return X,Y

#모바일과 소켓 연결
def Setting(ip,port):
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind((ip, port))
    serverSock.listen(1)

    connectionSock, addr = serverSock.accept()

    print(str(addr),'에서 접속이 확인되었습니다.')

    data = connectionSock.recv(1024).decode()

    return data # 모바일이 측정한 신호세기값 (3개)

#필터
def Weight(Rssi):
    Rssi_result = []
    Rssi_Weight = [1/7,1/7,1/7,1/7,3/7]
    for i in range(len(Rssi)):
        Rssi_result.append(Rssi[i] * Rssi_Weight[i])
    return Rssi_result

if __name__ == "__main__":    
    data = get_data() #data가져오기
    rssi_data, location_data = make_DB(data) # 파이어베이스로부터 받아온 데이터를 신호세기와 위치좌표DB로 만들기

    while(1):    
        data = set_data(rssi_data)  # 신호세기를 구현을 위해 2차원 배열로 만들기
        #mobile_data = Setting(ip,prot) # 소켓으로 모바일 데이터 가져오기
        #mobile_data = Weight(mobile_data) #필터
        
        mobile_data,subData,subLocation = set_Subdata(mobile_data ,data, location_data)    #후보 데이터 선정(모바일 측정데이터,신호세기, 위치좌표)

        similar_number=check_similar(mobile_data,subData,subLocation) #유사도 계산하기
        X,Y = print_location(similar_number,subLocation) #유사도결과 기반으로 X,Y출
        print("x,y : ", X, Y)
