from src.utils.logging import logging
from src.utils.exceptions import CustomException

from src.utils.utils import save_reviews
from src.data_scraper.google_reviews import GoogleMapsDataPull
from src.data_scraper.tripadvisor_reviews import TripAdviserDataPull
import os,sys


class ScrapReviews:
    """
    : Scrap data from web for inputed resturant/cafe....
    
    : it will used the google maps and tripadivers scraper data to scrap the data...
    """
    def __init__(self,foodPlace:str):
        self.foodPlace = foodPlace

    def initiate_data_scraper(self):
        """
        Initiate Data Scraper
        """
        try:
            logging.info("Entering intot data scraper..")
            google_map_data_puller=GoogleMapsDataPull(foodPlace=self.foodPlace)
            google_data_path=google_map_data_puller.initiate_google_maps_data_pull()
            logging.info("Review pulled form googlemap sucessfull..")

            tripadviser_data_puller=TripAdviserDataPull(foodPlace=self.foodPlace)
            tripadviser_data_path=tripadviser_data_puller.initiate_tripadviser_data_pull()
            logging.info("Review pulled form tripadviser sucessfull..")

            data_path=[google_data_path,tripadviser_data_path]
            logging.info(f"Data saved in..{data_path}")
            return data_path

        except Exception as e:
            raise CustomException(e,sys)



