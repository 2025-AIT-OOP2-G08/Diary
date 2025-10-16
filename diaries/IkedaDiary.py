from diaries.AbstractDiary import AbstractDiary

class IkedaDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"

    def get_summary(self):
        return "眠い"

    def get_author(self):
        return "Ikeda"