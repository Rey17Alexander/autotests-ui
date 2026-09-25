from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = Text(page, f"{identifier}-widget-title-text", "Title")
        self.chart = Image(page, f"{identifier}-{chart_type}-chart", "Chart")

    def check_visible(self, title: str):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)
        expect(self.chart).to_be_visible()
