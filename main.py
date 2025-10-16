from diaries.DiarySample import DiarySample
from diaries.KaiseiDiary import KaiseiDiary

# ↓のリストには、メンバーの各自気が格納されます。
diaries = [DiarySample(), 
           KaiseiDiary(),
           ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()