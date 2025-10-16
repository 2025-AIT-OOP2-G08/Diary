from diaries.AbstractDiary import AbstractDiary

class KaiseiDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"

    def get_summary(self):
        return "オブ演習疲れた"

    def get_author(self):
        return "Kaisei"