import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('192.168.35.9',12000))
server_socket.listen(0)
client_socket,addr = server_socket.accept()
data = client_socket.recv(65535)
result = data.decode()

print("recieve Data : ",data.decode())

cred = credentials.Certificate('living-lab-5aff5-firebase-adminsdk-20qye-f8994a93dc.json')

firebase_admin.initialize_app(cred, {
    'databaseURL':'https://living-lab-5aff5.firebaseio.com/'
})

result = 1

ref = db.reference('data')
##users_ref = ref.child('Omega')
##users_ref.set({
##    'Omega_all' : result
##   # 'Omega_beacon ':2
##})

users_ref = ref.child('Omega')
users_ref.set({
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
    'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
})
