print("SINH VIEN : DINH XUAN ANH")
print("MSV : 235752021610055")
print("#############################")
######################################​
import datetime as dt
format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2005-08-16T14:45:52', format)
print('Day ' + str(t1.day))
print('Month ' + str(t1.month))
print('Minute ' + str(t1.minute))
print('Second ' + str(t1.second))
# Define todays date and time
t2 = dt.datetime.now()
diff = t2 - t1
print('How many days difference? ' + str(diff.days))
