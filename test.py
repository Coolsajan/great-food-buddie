from scripts.run_scraper import ScrapReviews
from src.preprocessing.cleaning_chromradb import CleanAndSaveToChromaDBC


foodPlace=str(input("Enter the name of the cafe :"))

scraper=ScrapReviews(foodPlace=foodPlace)

resultpath=scraper.initiate_data_scraper()

clean_store=CleanAndSaveToChromaDBC()

clean_store.initiate_clean_chromadb(foodPlace=foodPlace,filepath=resultpath)