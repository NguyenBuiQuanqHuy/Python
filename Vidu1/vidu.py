# Nhập năm dương lịch. Đổi sang năm âm lịch
# 1991->Tân Mùi
# 2004->Giáp Thân

# canfull="Canh Tân Nhâm Quý Giáp Ất Bính Đinh Mậu Kỷ"
# can=[s for s in canfull.split()]
# chifull="Thân Dậu Tuất Hợi Tý Sửu Dần Mão Thìn Tỵ Ngọ Mùi "
# chi=[s.strip() for s in chifull.split()]
# dob=int(input("Nhập năm sinh:"))
# ca=can[dob%10]
# ch=chi[dob%12]
# print(f"Năm {dob} là năm {ca} {ch}")
#
#
# import datetime
# name= input("Nhập tên:")
# nam=int(input("Nhập năm sinh"))
# nam_hientai=datetime.datetime.now().year
# age=nam_hientai-nam
# print(f"{name} năm nay {age} tuổi")
# h=float(input())
# w=float(input())


# bmi=round(w / (h ** 2), 1)
# print(bmi)
# if bmi<18.5:
#     print("Gầy")
# elif 18.5<=bmi<25:
#     print("Bình thường")
# elif 25<=bmi<30:
#     print("Thừa cân")
# else: print("Béo phì")

canfull="Canh Tân Nhâm Quý Giáp Ất Bính Đinh Mậu Kỷ"
can=[s for s in canfull.split()]
chifull="Thân Dậu Tuất Hợi Tý Sửu Dần Mão Thìn Tỵ Ngọ Mùi"
chi=[s for s in chifull.split()]
try:
    nam=int(input())
except(ValueError):
   nam=int(input())
ca=can[nam%10]
ch=chi[nam%12]
print(f"{ca} {ch}")