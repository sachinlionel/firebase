from firebase import firebase

firebase = firebase.FirebaseApplication('https://resumei-9410d.firebaseio.com/')
print(firebase.get('/utm',None))
