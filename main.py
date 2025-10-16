from diaries.DiarySample import DiarySample
from diaries.KaiseiDiary import KaiseiDiary
from diaries.IkedaDiary import IkedaDiary
from diaries.GentaDiary import GentaDiary
from diaries.nakashimaDiary import NakashimaDiary



# ↓のリストには、メンバーの各自気が格納されます。
diaries = [DiarySample(), 
           KaiseiDiary(),
           IkedaDiary(),
           GentaDiary(),
           NakashimaDiary(),
           ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()