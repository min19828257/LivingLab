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
def set_Subdata(rssi_list, location_list):
    errorRange = 5;bestIndex = 0     # 오차허용범위, 큰값 인덱
    
    x = [77,63,72]     
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

if __name__ == "__main__":    
    data = get_data() #data가져오기
    rssi_data, location_data = make_DB(data)
    data = set_data(rssi_data)
    mobile_data,subData,subLocation = set_Subdata(data, location_data)    #후보 데이터 선정(모바일 측정데이터,신호세기, 위치좌표)
    similar_number=check_similar(mobile_data,subData,subLocation)
    X,Y = print_location(similar_number,subLocation)
    print("x,y : ", X, Y)
