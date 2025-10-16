from diaries.AbstractDiary import AbstractDiary

class NakashimaDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"

    def get_summary(self):
        return "今日はGitHubについてのグループワークをした。"

    def get_author(self):
        return "Nakashima"
