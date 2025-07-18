import pandas as pd
from langchain_core.documents import Document




class DataConverter:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def converter(self):
        df = pd.read_csv(self.file_path, encoding="utf-8", on_bad_lines="skip")[["product_title","review"]]
        docs= [
            Document(page_content=row["review"], metadata = {"product_name": row["product_title"]})
            for _,row in df.iterrows()
        ]
        return docs


if __name__ == "__main__":
    data = DataConverter(file_path="/home/deependera/LLMOps/flipkart_product_recommender/data/flipkart_product_review.csv")
    final = data.converter()
    print(final[0])
