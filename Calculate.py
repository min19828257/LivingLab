# d1:첫번째 비콘으로부터 신호세기
# d2:두번째 비콘으로부터 신호세기
# l:바닥부터 천장까지의 길이
# a:바닥부터 모바일까지의 길이
# h:삼변측량하기위한 결과

#삼변측량하기 위한 원의 중심점으로 부터 모바일까지의 거리
def calculate(d1,d2):
    d1=4;d2=3;l=10
    a=((d1**2)-(d2**2)+l**2)/(2*l)
    result=d1**2-a**2
    return result



