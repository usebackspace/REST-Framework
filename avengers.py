import requests

URL= 'http://127.0.0.1:8000/avengers/'

# def get_avengers():
#     response = requests.get(URL)
#     avengers = response.json()
#     for avenger in avengers:
#             print(avenger['name'],avenger['heroic_name'])

# # get_avengers()

# def add_avenger(name,heroic_name):
#       data ={'name':name,'heroic_name':heroic_name}
#       response = requests.post(URL,json=data)

#       if response.status_code == 201:
#           print('Avenger added Successfully')
#       else:
#             print('Failed to Add Avenger')
        
# # add_avenger('Thor Odin','Thor')


# def get_avenger_by_id(id):
#       response = requests.get(URL+str(id)+'/')
#       avenger = response.json()
#       print(avenger['name'],avenger['heroic_name'])

# # get_avenger_by_id(2)

# def update_avenger(id,name,heroic_name):
#       data={'name':name,'heroic_name':heroic_name}
#       response = requests.put(URL+f'{id}/',json=data)
#       if response.status_code == 200:
#             print('updated Successfully')
#       else:
#             print('Data not Found')

# # update_avenger(2,'Bruce Banner','Hulk')

# def delete_avenger(id):
#       response =requests.delete(URL+f"{id}/")

# delete_avenger(4)



def get_avengers():
    response = requests.get(URL)
    avengers = response.json()
    for avenger in avengers:
        print(avenger['name'],avenger['heroic_name'])

# get_avengers()

def add_avenger():
    data = {'name':'Natasha RomanOff','heroic_name':'Black Widow'}
    response = requests.post(URL,json=data)

# add_avenger()

def get_avenger_id(id):
    response = requests.get(URL+f'{id}/')
    avenger = response.json()
    print(avenger['name'],avenger['heroic_name'])

# get_avenger_id(2)

def update_avenger(id,name,heroic_name):
    data={'name':name,'heroic_name':heroic_name}
    response = requests.put(URL+f'{id}/',json=data)
    print(response)

# update_avenger(2,'Bruce Banner','Hulk')

def delete_avenger(id):
    response = requests.delete(URL+f'{id}/')

delete_avenger(5)