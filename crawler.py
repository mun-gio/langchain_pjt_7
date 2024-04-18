# crawler.py
import bs4
from langchain_community.document_loaders import WebBaseLoader


class Crawler:
    def __init__(self) -> None:
        pass
    def crawler(self):
        nutrients = ['vitamin-c', 'vitamin-d', 'vitamin-a', 'vitamin-e', 'vitamin-k', 'biotin', 'vitamin-b12', 'vitamin-b3', 'vitamin-b6', 'vitamin-b2', 'vitamin-b1', 'folic-acid', 'vitamin-b5', 'prenatal-vitamins','calcium', 'zinc', 'biotic-supplement', 'taurine', 'theanine', 'creatine', 'curcumin', 'boron', 'copper', 'iron', 'coenzyme-q10','citric-acid', 'glucosamine', 'glutamine', 'gluten', 'glycine', 'iodine', 'lutein', 'nicotine', 'potassium']
        docs = []
        for i in nutrients:
            loader = WebBaseLoader(
                web_paths=(f"https://examine.com/supplements/{i}/",),
                bs_kwargs=dict(
                    parse_only=bs4.SoupStrainer(
                        "div",
                        attrs={"class": ["summary"]},
                    )
                ),
            )
            docs += loader.load()
        return docs
