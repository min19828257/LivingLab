import kalman_2

# Ba1:첫번째 천장비콘으로부터 신호세기
# Ba2:두번째 바닥비콘으로부터 신호세기
# Bb1:세번째 천장비콘으로부터 신호세기
# Bb2:네번째 바닥비콘으로부터 신호세기
# Bc1:다섯번째 천장비콘으로부터 신호세기
# Bc2:여섯번째 바닥비콘으로부터 신호세기

# l:바닥부터 천장까지의 길이
# a:바닥부터 모바일까지의 길이
# h:삼변측량하기위한 결과

#삼변측량하기 위한 원의 중심점으로 부터 모바일까지의 거리
def calculate(d1,d2):
    d1=4;d2=3;l=10
    a=((d1**2)-(d2**2)+l**2)/(2*l)
    result=d1**2-a**2
    return result

#각 비콘의 위치별 거리값 계
def in_data(data):
    rssi_list_2 = []
    rssi_result = []
    print(data)
    rssi_list = data.split(',')
    rssi_list_2.append(float(rssi_list[0]))
    rssi_list_2.append(float(rssi_list[1]))
    rssi_list_2.append(float(rssi_list[2]))
    rssi_list_2.append(float(rssi_list[3]))
    rssi_list_2.append(float(rssi_list[4]))
    rssi_list_2.append(float(rssi_list[5]))
    print(rssi_list_2)
    rssi_result = kalman_2.Kalman_3(rssi_list_2)
    Ba1=rssi_result[0]
    Ba2=rssi_result[1]
    Bb1=rssi_result[2]
    Bb2=rssi_result[3]
    Bc1=rssi_result[4]
    Bc2=rssi_result[5]
    distance1 = calculate(Ba1,Ba2)
    distance2 = calculate(Bb1,Bb2)
    distance3 = calculate(Bc1,Bc2)
    return str(distance1)+","+str(distance2)+","+str(distance3)
