# Import database module.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#데이터 가져오기
def get_data():

    cred = credentials.Certificate('living-lab-5aff5-firebase-adminsdk-20qye-d135bd46ca.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL':'https://living-lab-5aff5.firebaseio.com/'
    })
    
    # Get a database reference to our posts
    ref = db.reference('Position coordinates/4Floor Lab')
    # Read the data at the posts reference (this is a blocking operation)
    data = ref.get()
    return data


# RSSI DB & 좌표 DB 만들기
def make_DB(data):
    rssi_db = []; location_db = []

    data = str(data)

    data = data.replace(": {'location': 1, 'location(", " ")
    for i in range(4):
        text = ""
        for j in range(4):
            text = "'("+str(i)+","+str(j)+")'"
            data = data.replace(text, "")
    data = data.replace(")", "")
    data = data.replace("{", "")
    data = data.replace("}", "")
    data = data.replace(":", "")
    data = data.replace("\n", "")
    data = data.replace("{", "")
    data = data.replace("'", "")
    data = data.replace("\\n", "")

    data = data.split(",  ")

   
    for i in range(len(data)):
        newdata = data[i].split(" [")
        location_db.append(newdata[0].strip())  #좌표 설정하기

        rssi = newdata[1][0:-1]
        rssi_db.append(rssi)    #신호세기 설정하기

    return rssi_db, location_db

#    print(data)
    

#if __name__ == "__main__":
#     data = get_data() #data가져오기
#     rssi_data, location_data = make_DB(data)
