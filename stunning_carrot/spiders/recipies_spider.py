from pathlib import Path
from typing import Iterable

import scrapy
from scrapy import Request


class RecipiesSpider(scrapy.Spider):
    name = "recipies"

    def start_requests(self) -> Iterable[Request]:
        urls = [
            ""
        ]