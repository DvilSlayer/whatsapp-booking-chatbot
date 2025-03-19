import requests
from datetime import datetime, timezone, timedelta
import json
current_time = datetime.now()
respons = requests.get(url=f"https://max-api.fusionintel.io/api/v1/Showtimes/get-showtimes?DateFrom={current_time.month}%2F{current_time.day}%2F{current_time.year}&DateTo={current_time.month}%2F{current_time.day + 1}%2F{current_time.year}",headers={'Content-type': 'application/json', 'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})
dat=respons.json()
y=dat['data']
import sqlite3
import json
time_str = "08:30 PM"
time_obj = datetime.strptime(time_str, "%I:%M %p")

# Combine the current date with the parsed time
combined_datetime = current_time.replace(hour=time_obj.hour, minute=time_obj.minute, second=0, microsecond=0)

# Format the combined datetime as a string in the desired format
# formatted_datetime = combined_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
formatted_datetime = combined_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
print(formatted_datetime)
timestamp_str = "2023-09-15T10:00:00Z"
timestamp_obj = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")

# Convert to 12-hour format with AM/PM
formatted_time = timestamp_obj.strftime("%I:%M %p")
print(formatted_time)
# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('my_dictionary_db2.db')
cursor = connection.cursor()
# cursor.execute('DROP TABLE IF EXISTS dictionaries')
# Create a table to store dictionaries (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS dictionaries2 (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  data JSON
               )''')
film_to_keep = 'Mission Impossible: Dead Reckoning I'
cursor.execute("INSERT INTO dictionaries2 (name, data) VALUES (?, ?)",
               ('example_dict', json.dumps(y)))

# Commit changes to the database
connection.commit()

# Retrieve the dictionary from the database
cursor.execute("SELECT * FROM dictionaries2 WHERE name=?", ('example_dict',))
row = cursor.fetchone()
_, _, serialized_data = row
retrieved_data = json.loads(serialized_data)
print(retrieved_data)
connection.close()
connection = sqlite3.connect('my_dictionary_db2.db')
cursor = connection.cursor()
# Create a new list to store the filtered screentimes
filtered_scree= []

# Loop through the screentimes and keep only the ones with the specified film name
for screentime in y:
    if screentime.get('film') == film_to_keep:
        filtered_scree.append(screentime)
# print(filtered_scree)
# print(y)
# Update the modified dictionary in the database
cursor.execute("UPDATE dictionaries2 SET data=? WHERE name=?",
                   (json.dumps(filtered_scree), 'example_dict'))

# Commit changes to the database
connection.commit()
print(filtered_scree)
target_time = '2023-09-15T10:00:00Z'
screen_id = ['']
for showing in filtered_scree:
    if showing['startTime'] == formatted_datetime:
        screen_id = showing['screenId']
        break
    else:
        screen_id = [""]
print(screen_id)
# Close the database connection
connection.close()
connection = sqlite3.connect('my_dictionary_db2.db')
cursor = connection.cursor()
# Update the modified dictionary in the database
cursor.execute("UPDATE dictionaries2 SET data=? WHERE name=?",
                   (json.dumps(y), 'example_dict'))

# Commit changes to the database
connection.commit()
print(y)
# Close the database connection
connection.close()
ids = []


# respons = requests.get(url="https://api.reachcinema.io/api/v1/Cinemas/ListAllByCircuit?circuitId=c7525c4a-d2b6-46e3-83cd-646402c62326",headers={'Content-type': 'application/json','Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})
# dat=respons.json()
# y=dat['data']
# print(y)
response = requests.get(url=f"https://max-api.fusionintel.io/api/v1/Showtimes/get-whatsapp-showtimes?DateFrom={current_time.month}%2F{current_time.day}%2F{current_time.year}&DateTo={current_time.month}%2F{current_time.day + 1}%2F{current_time.year}",headers={'Content-type': 'application/json', 'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})
data=response.json()
x=data['data']
times = ['10:00 AM', '10:30 AM', '12:30 PM', '12:40 PM', '12:50 PM', '02:50 PM', '03:50 PM', '04:00 PM', '05:10 PM', '06:10 PM', '07:10 PM', '08:10 PM', '10:20 PM', '10:30 PM', '12:00 PM', '12:30 PM', '02:00 PM', '02:20 PM', '03:00 PM', '05:20 PM', '05:30 PM', '06:00 PM', '06:20 PM', '07:20 PM', '07:30 PM', '08:30 PM', '08:40 PM', '10:00 PM', '10:20 PM', '10:40 PM', '10:50 PM', '11:10 PM',
         '11:20 PM', '11:30 PM', '11:40 PM', '11:50 PM', '12:10 PM', '12:20 PM', '12:40 PM', '12:50 PM', '01:00 PM', '01:10 PM', '02:00 PM', '02:10 PM', '02:30 PM', '02:40 PM', '02:50 PM', '03:00 PM', '03:10 PM', '03:20 PM', '03:30 PM', '03:40 PM', '03:50 PM', '04:00 PM', '04:10 PM', '04:20 PM', '04:30 PM', '04:40 PM', '04:50 PM', '05:00 PM', '05:10 PM', '05:20 PM', '05:30 PM', '05:40 PM',
         '05:50 PM', '06:10 PM', '06:20 PM', '06:30 PM', '06:40 PM', '06:50 PM', '07:00 PM', '07:10 PM', '07:20 PM', '07:30 PM', '07:40 PM', '07:50 PM', '08:00 PM',
         '08:10 PM', '08:20 PM', '08:30 PM', '08:40 PM', '08:50 PM', '09:00 PM', '09:10 PM', '09:20 PM', '09:30 PM', '09:40 PM', '09:50 PM', '10:00 PM', '10:10 PM', '11:00 PM', '11:00 PM', '11:20 PM', '11:50 PM', '12:00 PM', '12:20 PM', '12:40 PM', '12:50 PM', '01:10 PM', '01:20 PM', '01:30 PM', '01:40 PM', '01:50 PM', '02:00 PM', '02:10 PM', '02:20 PM', '02:30 PM', '02:40 PM', '02:50 PM']
from datetime import datetime

# Get the current date and time
current_datetime = datetime.utcnow()

# Format it as "YYYY-MM-DDTHH:MM:SS.sssZ"
formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
opp= current_datetime.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

print(formatted_datetime)
print(opp)
payload = {
  "cinemaId": "05c09ec8-9655-43ed-92e8-738f03a66e4b",
  "name": "tope",
  "email": "babatopeademodi@gmail.com",
  "phoneNumber": "2348089321091",
  "order": {
    "ticketSales": [
      {
        "showtimeId": "71614de7-176c-4e3c-904d-f7ab65a7ac28",
        "priceCardTicketId": "839e10d9-a17a-4588-94f8-154bc2291536",
        "ticketId": "254d79aa-7449-4795-bcd0-60c9fd4728d3",

        "ticketPrice": 4400,
        "quantity": 2,
        "amount": 30*4
      }
    ],
    "itemSales": [
      {
        "itemId": "8aa9f7ea-e20c-42c6-aa6c-2a3f7ef4c6af",
        "itemParentId": "d1b7289d-c6eb-4c73-bf5f-3108c27a235b",
        "packageTicketId": "254d79aa-7449-4795-bcd0-60c9fd4728d3",

        "quantity": 2,
        "price": 0,
        "amount": 10,
        "name": "string"
      }
    ],
    "amount": 0,
    "sourceId": "source-68fe65",
    "channelId": "channel-928a2b",

    "dateTimeReserved": "2023-09-07T17:38:38.550Z"
  },
  "screenId": "e7febec4-4e86-4966-a8be-86c1a4bef845",
  "seatNumber": 0
}
rr=payload["order"]["itemSales"][0]["quantity"]
payload["order"]["itemSales"][0]["quantity"] = payload["order"]["itemSales"][0]["quantity"] * 2
print(rr)
rp=payload["order"]["itemSales"][0]["quantity"]
print(rp)
#showtime data sample'c9a098d9-dbaf-4644-a2a1-12375dea2743'
# "priceCardId": "caf81b80-a58a-414a-97ac-3ef48b4077f6",
# "priceCard": {
#     "id": "caf81b80-a58a-414a-97ac-3ef48b4077f6",
#     "name": "Kolade Test",
#     "tickets": [
#         {
#             "id": "839e10d9-a17a-4588-94f8-154bc2291536",
#             "priceCardId": "caf81b80-a58a-414a-97ac-3ef48b4077f6",
#             "ticketId": "254d79aa-7449-4795-bcd0-60c9fd4728d3",
#             "ticketName": "Duo package",
#             "shortName": "duo pkg",
#             "price": 4400,
#             "ticketPackageId": "c9a098d9-dbaf-4644-a2a1-12375dea2743",
#             "ticketPackage": {
#                 "items": [
#                     {
#                         "id": "b2ce2918-1e66-43f7-903d-c64f7ee15756",
#                         "name": "Small Popcorn",
#                         "itemId": "8aa9f7ea-e20c-42c6-aa6c-2a3f7ef4c6af",
#                         "unit": 0,
#                         "price": 1000,
#                         "quantity": 2
#                     }
#                 ],
#                 "itemParents": [
#                     {
#                         "id": "d1b7289d-c6eb-4c73-bf5f-3108c27a235b",
#                         "name": "coke and fanta",
#                         "price": 200,
#                         "quantity": 2,
json_payload = json.dumps(payload)
try:
    # Make the POST request
    response = requests.post(url="https://max-api.fusionintel.io/api/v1/Bookings/create-whatsapp-booking", data=json_payload, headers={'Content-type': 'application/json', 'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        print('Response JSON:', response.json()['data']['paymentUrl'])
        # Assuming the response is in JSON format

    else:
        print(f"Request failed with status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
response = requests.get(url="https://api.reachcinema.io/api/v1/Cinemas/ListAllByCircuit?circuitId=c7525c4a-d2b6-46e3-83cd-646402c62326",headers={'Content-type': 'application/json', 'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})
data=response.json()
o=data['data']
id_=[]
for i in o:
    id_.append(i['id'])
print(id_[0])
print(o)
# r = requests.post(url="https://max-api.fusionintel.io/api/v1/Bookings/create-booking",headers={'Content-type': 'application/json', 'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'},data=da)
# pastebin_url = r.text
# print("The pastebin URL is:%s" % pastebin_url)
keys=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l_x = zip(keys,x)
dicct = dict(l_x)
# print(dicct)
# print(x)
movie_info_dict = {}
# ebony life
response = requests.get(url=f"https://max-api.fusionintel.io/api/v1/Showtimes/get-whatsapp-showtimes?DateFrom={current_time.month}%2F{current_time.day}%2F{current_time.year}&DateTo={current_time.month}%2F{current_time.day + 1}%2F{current_time.year}",headers={'Content-type': 'application/json', 'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiJlYm8tNTE1N2U1MTIiLCJuYmYiOjE2ODg0NzkxMjEsImV4cCI6MTcyMDEwMTUyMSwiaWF0IjoxNjg4NDc5MTIxLCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.rdLXhqTOPaE0e5mwJdoaANK7rEF23m53PN9ne_gUw0s'})
data=response.json()
p=data['data']
# print(p)
# https://max-api.fusionintel.io/api/v1/Showtimes/get-film-showtimes?todayDate=8%2F12%2F2023
response2 = requests.get(url="https://max-api.fusionintel.io/api/v1/Showtimes/get-film-showtimes?todayDate=8%2F12%2F2023",headers={'Content-type': 'application/json', 'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ2luZW1hQXBpIiwiQ2luZW1hSWQiOiIwNWMwOWVjOC05NjU1LTQzZWQtOTJlOC03MzhmMDNhNjZlNGIiLCJuYmYiOjE2OTEyNjc4NDcsImV4cCI6MTcyMjg5MDI0NywiaWF0IjoxNjkxMjY3ODQ3LCJpc3MiOiJodHRwczovL2Z1c2lvbmludGVsLmlvIiwiYXVkIjoiVXNlciJ9.8gNZ1kZSOqqErERX22ncxNHp1WLYFPmaV9BNx_wtVqc'})
data2 = response2.json()
w=data2['data']
name=[]
screen=[]
for movie in x:
    movie_name = movie["film"]
    if movie_name not in movie_info_dict:
        movie_info_dict[movie_name] = []
    try:
        start_time_utc = datetime.strptime(movie["startTime"], "%Y-%m-%dT%H:%M:%SZ")
        end_time_utc = datetime.strptime(movie["endTime"], "%Y-%m-%dT%H:%M:%SZ")
    except:
        start_time_utc = datetime.strptime(movie["startTime"], "%Y-%m-%dT%H:%M:%S.%fZ")
        end_time_utc = datetime.strptime(movie["endTime"], "%Y-%m-%dT%H:%M:%S.%fZ")
    local_timezone = timezone.utc
    start_time_local = start_time_utc.replace(tzinfo=local_timezone).astimezone(
        timezone(timedelta(hours=5)))  # Adjust the hours according to your timezone
    end_time_local = end_time_utc.replace(tzinfo=local_timezone).astimezone(
        timezone(timedelta(hours=5)))  # Adjust the hours according to your timezone
    movie_info_dict[movie_name].append("Screen: " + movie["screen"])
    screen.append(start_time_local.strftime("%I:%M %p"))
    movie_info_dict[movie_name].append("Start Time - " + start_time_local.strftime("%I:%M %p"))
    # movie_info_dict[movie_name].append("Start Time : " + start_time_local.strftime("%Y-%m-%d %I:%M %p"))
    movie_info_dict[movie_name].append("Date : " + start_time_local.strftime("%Y-%m-%d"))
    # movie_info_dict[movie_name].append("End Time : " + end_time_local.strftime("%I:%M %p"))
    movie_info_dict[movie_name].append("Total seats: " + str(movie["totalSeats"]))
    movie_info_dict[movie_name].append("Seats Sold: " + str(movie["seatsSold"]))
    # movie_info_dict[movie_name].append("Available seats: " + str(movie["totalSeats"] - movie["seatsSold"]))
    movie_info_dict[movie_name].append("=" * 34)
# print(screen)
# for i in movie_info_dict.items:
#     if i == ("=" * 50):
#         i= ("+" * 50)
# print(movie_info_dict.values())
for i in movie_info_dict.values():
    if len(i) > 6:
        for t in i[:-1]:
            dd = i.index(t)
            if t == ('=================================='):
                i[dd] = ('__________________________________')
# print(movie_info_dict.values())
all_movie_in = []
for movie_name, info_list in movie_info_dict.items():
    movie_info = ["Movie: " + movie_name]
    movie_info.extend(info_list)
    movie_string = '\n'.join(movie_info)
    # create a movie list
    all_movie_in.append(movie_string)
final_movie_info = '\n'.join(all_movie_in)
l_x = zip(keys,all_movie_in)
dicct = dict(l_x)
# print("Please Input a Screentime to book\nFor Example:\n03:00 PM\n\n"+dicct['b'])
# print(dicct['b'])
start_times = []
screens = []

lines = final_movie_info.split("\n")
i = 0
while i < len(lines):
    if "Start Time" in lines[i]:
        start_time = lines[i].split("-")[1].strip()
        start_times.append(start_time)
    elif "Screen" in lines[i]:
        screen = lines[i].split(":")[1].strip()
        screens.append(screen)
    i += 1

# print(str(start_times))
# print("Screens:", screens)
# print(final_movie_info)
movie_info_dict = {}
for movie in x:
    movie_name = movie["film"]
    if movie_name not in movie_info_dict:
        movie_info_dict[movie_name] = []

all_movie_info = []

for movie_name, info_list in movie_info_dict.items():
    all_movie_info.append(movie_name)
#     movie_info = ["Movie: " + movie_name]
#     # movie_info = [movie_name]
#     movie_info.extend(info_list)
#     movie_string = '\n'.join(movie_info)
#     all_movie_info.append(movie_string)
# final_movie_info2 = '\n'.join(all_movie_info)
# for i in all_movie_info:
#     p.append(i.values())

# print(all_movie_info)
movie_info=[]
for movie in y:
    movie_ = []
    price_card = movie["priceCard"]
    movie_info.append("Price Card Name:" + price_card["name"])

    for ticket in price_card["tickets"]:
        movie_.append("Ticket Name:" + ticket["ticketName"])
        # movie_.append("Ticket Name:" + str(ticket["ticketPackage"]))
        movie_.append("Price:" + str(ticket["price"]))
    movie_info_str = '\n'.join(movie_)
# print(movie_info_str)

# import sqlite3
#
# # Connect to the SQLite database (or create it if it doesn't exist)
# connection = sqlite3.connect('my_dictionary_db.db')
# cursor = connection.cursor()
#
# # Create a table to store dictionaries
# cursor.execute('''CREATE TABLE IF NOT EXISTS dictionaries (
#                   id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   name TEXT,
#                   data JSON
#                )''')
#
# # Insert a dictionary into the table
# data_to_insert = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': [1, 2, 3]
# }
#
# cursor.execute("INSERT INTO dictionaries (name, data) VALUES (?, ?)",
#                ('example_dict', json.dumps(data_to_insert)))
#
# # Commit changes and close the connection
# connection.commit()
# connection.close()
#
# # Reconnect to the database and retrieve the dictionary
# connection = sqlite3.connect('my_dictionary_db.db')
# cursor = connection.cursor()
#
# cursor.execute("SELECT * FROM dictionaries WHERE name=?", ('example_dict',))
# row = cursor.fetchone()
# cursor.execute('DROP TABLE IF EXISTS dictionaries')
#
# if row:
#     _, _, serialized_data = row
#     retrieved_data = json.loads(serialized_data)
#     print("Retrieved Dictionary:")
#     print(retrieved_data)
# else:
#     print("Dictionary not found")
# # print(retrieved_data['key1'])
# # Close the connection
# connection.close()
import sqlite3
import json

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('my_dictionary_db.db')
cursor = connection.cursor()
# cursor.execute('DROP TABLE IF EXISTS dictionaries')
# Create a table to store dictionaries (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS dictionaries (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  data JSON
               )''')

# Insert a dictionary into the table
data_to_insert = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': [1, 2, 3]
}

cursor.execute("INSERT INTO dictionaries (name, data) VALUES (?, ?)",
               ('example_dict', json.dumps(data_to_insert)))

# Commit changes to the database
connection.commit()

# Retrieve the dictionary from the database
cursor.execute("SELECT * FROM dictionaries WHERE name=?", ('example_dict',))
row = cursor.fetchone()
_, _, serialized_data = row
retrieved_data = json.loads(serialized_data)
print("Original Dictionary:")
print(retrieved_data)
# print(retrieved_data["key1"])
connection.close()
# connection = sqlite3.connect('my_dictionary_db.db')
# cursor = connection.cursor()
#
# cursor.execute("SELECT * FROM dictionaries WHERE name=?", ('example_dict',))
# row = cursor.fetchone()
# _, _, serialized_data = row
# retrieved_data = json.loads(serialized_data)
# print("Original Dictionary:")
# print(retrieved_data)

# Modify the dictionary
retrieved_data['key1'] = 'value1'
connection = sqlite3.connect('my_dictionary_db.db')
cursor = connection.cursor()

# cursor.execute("SELECT * FROM dictionaries WHERE name=?", ('example_dict',))
# row = cursor.fetchone()
# _, _, serialized_data = row
# retrieved_data = json.loads(serialized_data)
# print("Original Dictionary:")
# print(retrieved_data)

# Update the modified dictionary in the database
cursor.execute("UPDATE dictionaries SET data=? WHERE name=?",
                   (json.dumps(retrieved_data), 'example_dict'))

# Commit changes to the database
connection.commit()
print("Modified Dictionary:")
print(retrieved_data)
print("Dictionary not found")

# Close the database connection
connection.close()
# cursor.execute("INSERT INTO dictionaries (name, data) VALUES (?, ?)",
#                ('example_dict', json.dumps(data_to_insert)))
#
# # Commit changes to the database
# connection.commit()
#
# # Retrieve the dictionary from the database
# cursor.execute("SELECT * FROM dictionaries WHERE name=?", ('example_dict',))
# row = cursor.fetchone()
# if row:
#     _, _, serialized_data = row
#     retrieved_data = json.loads(serialized_data)
#     print("Original Dictionary:")
#     print(retrieved_data)
# print(retrieved_data["key1"])
# connection.close()
# connection = sqlite3.connect('my_dictionary_db.db')
# cursor = connection.cursor()
#
# cursor.execute("SELECT * FROM dictionaries WHERE name=?", ('example_dict',))
# row = cursor.fetchone()
# if row:
#     _, _, serialized_data = row
#     retrieved_data = json.loads(serialized_data)
#     print("Original Dictionary:")
#     print(retrieved_data)
#
#     # Modify the dictionary
#     retrieved_data['key1'] = 'value'
#
#     # Update the modified dictionary in the database
#     cursor.execute("UPDATE dictionaries SET data=? WHERE name=?",
#                    (json.dumps(retrieved_data), 'example_dict'))
#
#     # Commit changes to the database
#     connection.commit()
#     print("Modified Dictionary:")
#     print(retrieved_data)
# else:
#     print("Dictionary not found")
#
# # Close the database connection
# connection.close()

# if __name__ == "__main__":
#     import sender  # Import the sender module
#
#     # Call the function in sender.py to send the variable
#     sender.send_variable_to_receiver()
# cursor.execute("DELETE FROM dictionaries;")
# def get_dictionary():
#     connection = sqlite3.connect('my_dictionary_db.db')
#     cursor = connection.cursor()
#     # cursor.execute('DROP TABLE IF EXISTS dictionari')
#     cursor.execute("INSERT INTO dictionari (name, data) VALUES (?, ?)",
#                    ('example_dict', json.dumps(data_to_insert)))
#     cursor.execute("SELECT * FROM dictionari WHERE name=?", ('example_dict',))
#     row = cursor.fetchone()
#     if row:
#         _, _, serialized_data = row
#         retrieved_data = json.loads(serialized_data)
#         connection.close()
#         return retrieved_data
#     else:
#         connection.close()
#         return None
# dataaa=get_dictionary()
# print(dataaa)
# dataaa["key1"]="hey"
# connection = sqlite3.connect('my_dictionary_db.db')
# cursor = connection.cursor()
# cursor.execute("UPDATE dictionari SET data=? WHERE name=?",
#                             (json.dumps(dataaa), 'example_dict'))
# connection.commit()
# connection.close()
# print(dataaa)
# from datetime import datetime
#
# # Get the current date and time
# current_datetime = datetime.utcnow()
#
# # Format it as "YYYY-MM-DDTHH:MM:SS.sssZ"
# formatted_datetime = current_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
#
# print(formatted_datetime)