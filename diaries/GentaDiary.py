from diaries.AbstractDiary import AbstractDiary

class GentaDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-01"

    def get_summary(self):
        return "大学からの電話怖い"

    def get_author(self):
        return "Genta"