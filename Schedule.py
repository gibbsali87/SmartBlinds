import pymongo
from pip._vendor.distlib.compat import raw_input

myclient = pymongo.MongoClient("mongodb+srv://SB_Admin:RainyDay10@mongoa-ewvkf.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["SmartBlinds"]
mycol = mydb["SB"]

print("Enter Schedule for your Blinds in Format: yyyy-mm-dd HH:mm")
year = raw_input("Year: ")
month = raw_input("Month: ")
day = raw_input("Day: ")
hour = raw_input("Hour: ")
minute = raw_input("Minute: ")

mySch = {"Object": "Smart Blinds", "Year": year, "Month": month, "Day": day, "Hour": hour, "Minute": minute}

x = mycol.insert_one(mySch)


print("Your Enter Below Schedule.")
print(year, month, day, hour, minute)