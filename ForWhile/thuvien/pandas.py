import pandas as pd
print(pd.__version__)
num=pd.Series(["Bưởi","Táo","Cam","Chanh"])
nums=pd.Series([1,2,3,4])
list=pd.Series(['Nguyễn Bùi Quang Huy','64130854'],index=['Full Name','DD'])
print(nums.values)
print(nums.index)
print(list.index)
print(list.values)
print(num)

pData={'Nghệ An':16000,'Khánh Hòa':7000}
plist=['Nghệ An','Khánh Hòa','Phú Yên','Gia Lai']
province=pd.Series(pData,index=plist)
print(province)

print(pd.isnull(province))

            
