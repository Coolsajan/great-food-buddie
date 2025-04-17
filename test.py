from scripts.run_scraper import ScrapReviews


foodPlace=str(input("Enter the name of the cafe :"))

scraper=ScrapReviews(foodPlace=foodPlace)

resultpath=scraper.initiate_data_scraper()
print(resultpath)