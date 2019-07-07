# Import database module.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('living-lab-5aff5-firebase-adminsdk-20qye-f8994a93dc.json')

firebase_admin.initialize_app(cred, {
    'databaseURL':'https://living-lab-5aff5.firebaseio.com/'
})


# Get a database reference to our posts
ref = db.reference('data')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())
