from utils import Utils

class WebScrapper(Utils):
    def _init_(self):
        super().__init__()

if __name__ == '__main__':
    WebScrapperBot = WebScrapper()
    WebScrapperBot.open_website()
    WebScrapperBot.begin_search()
    WebScrapperBot.select_topic()
    WebScrapperBot.sort_newest_news()
    WebScrapperBot.set_month_range()
    WebScrapperBot.extract_website_data()
    WebScrapperBot.close_browser()