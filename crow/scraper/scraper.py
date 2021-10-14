from crow.scraper.bot import Bot
from crow.scraper.sites import Site

if __name__ == "__main__":
  coindesk = Site(
    name="coindesk",
    urls=[
      "https://www.coindesk.com/markets/",
    ]
  )