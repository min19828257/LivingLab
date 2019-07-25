import Simple_server   #TCP Socket

data = Simple_server.Setting('127.0.0.1',8888) #신호세기를 위치좌표(X,Y)로 변환
data = data.split(",") 
print(data) #(X,Y)좌표값으로 결과 도출




