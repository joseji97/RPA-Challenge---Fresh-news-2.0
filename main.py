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
    #WebScrapperBot.close_browser()
#            
#            
#            
#            wi.add_work_item_file("./result.xlsx", "RESULT_EXCEL.xlsx")
#            files = get_all_files_from_folder()
#            wi.create_output_work_item(files=files, save=True)
#            wi.create_output_work_item(files="./result.xlsx", save=True)

#        finally:
#            