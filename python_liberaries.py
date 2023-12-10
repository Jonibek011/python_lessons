

# Datetime
import datetime as dt
now = dt.datetime.now()
# print(now)
#bugun = dt.date.today()
# print(bugun)
# ertaga = dt.date(2023, 12, 11)
# print(f"Ertangi sana {ertaga}")

# hozir = dt.datetime.now()
# hozirVaqt = hozir.time()
# print(hozirVaqt)
# print(f"Hozir vaqt {hozirVaqt}")
# keyinVaqt = dt.time(20, 23, 34)
# print(keyinVaqt)

# ramazon = dt.date(2024, 4, 12)
# days = (ramazon - bugun)
# t_kun = dt.date(2024, 2, 12)
# farq = (t_kun - bugun)
# # print(farq.days)
# Nilu = dt.date(2024, 4, 21)
# farq1 = (Nilu - bugun)
# print(f"Tug'ilgan kunimga {farq.days} kun qoldi")

bugun = dt.datetime.now()
fudbol = dt.datetime(2023, 12, 11, 23, 45, 00)
farq = fudbol-bugun
print(farq)


