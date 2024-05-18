from cutecharts.charts import Pie
from cutecharts.components import Page
from playwright.sync_api import sync_playwright


def pie(day_of_year: int):
    chart = Pie(width="200px", height="200px")

    WHITE = "#00000000"
    GREEN = "#AFE1AF"

    chart.set_options(
        labels=["done", "remaining"],
        colors=[GREEN, WHITE],
        inner_radius=0
    )
    days_in_year = 365
    days_remaining = days_in_year - day_of_year

    chart.add_series(data=[day_of_year, days_remaining])
    return chart


def make_page(day_of_year: int):
    page = Page()
    page.add(pie(day_of_year=day_of_year))
    page.render()


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for i in range(1, 365 + 1):
            print(i)
            make_page(i)

            page.goto("file:///home/chowder/code/countdown/render.html")
            page.evaluate("document.body.style.zoom=5.0")
            page.screenshot(
                path=f"bars/{i}.png",
                omit_background=True,
                clip={
                    "x": 450,
                    "y": 283,
                    "width": 180,
                    "height": 180,
                }
            )
