from utils import Utils

class WebScraper(Utils):
    def _init_(self):
        super().__init__()

if __name__ == '__main__':
    WebScraperBot = WebScraper()
    WebScraperBot.open_website()
    WebScraperBot.begin_search()
    WebScraperBot.select_topic()
    WebScraperBot.sort_newest_news()
    WebScraperBot.set_month_range()
    WebScraperBot.extract_website_data()
    WebScraperBot.close_browser()
    WebScraperBot.print_and_log("info","Bot execution finished")