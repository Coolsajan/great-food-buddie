from scripts.run_scraper import ScrapReviews
from src.preprocessing.cleaning_chromradb import CleanAndSaveToChromaDBC
from src.rag_pipeline.retriever import load_retriver

foodPlace=str(input("Enter the name of the cafe :"))

scraper=ScrapReviews(foodPlace=foodPlace)

resultpath=scraper.initiate_data_scraper()

clean_store=CleanAndSaveToChromaDBC()

clean_store.initiate_clean_chromadb(foodPlace=foodPlace,filepath=resultpath)

if __name__ == "__main__":
    retriever = load_retriver(foodPlace=foodPlace)
    results = retriever.invoke("good food ?")
    for r in results:
        print(r.page_content)
