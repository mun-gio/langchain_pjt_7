# crawler.py
import bs4
from langchain_community.document_loaders import WebBaseLoader


class Crawler:
    def __init__(self) -> None:
        pass

    def crwaler(self, vitamin):
        loader = WebBaseLoader(
            web_paths=(f"https://examine.com/supplements/{vitamin}/",),
            bs_kwargs=dict(
                parse_only=bs4.SoupStrainer(
                    "div",
                    attrs={"class": ["summary"]},
                )
            ),
        )

        docs = loader.load()
        print(f"문서의 수: {len(docs)}")
        print(docs)

crawler = Crawler()
crawler.crwaler()
