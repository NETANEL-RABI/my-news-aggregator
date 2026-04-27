import feedparser, json, requests, time
from bs4 import BeautifulSoup
from datetime import datetime

def get_full(url):
    try:
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        soup = BeautifulSoup(resp.content, 'html.parser')
        paragraphs = soup.find_all('p')
        return "\n\n".join([p.get_text() for p in paragraphs if len(p.get_text()) > 50])[:2500]
    except: return ""

def scrape():
    feeds = ["https://www.now14.co.il/feed/", "https://www.jdn.co.il/feed/", "https://www.inn.co.il/rss.xml"]
    results = []
    for url in feeds:
        f = feedparser.parse(url)
        for e in f.entries[:5]:
            print(f"Scraping: {e.title}")
            results.append({
                "title": e.title,
                "body": get_full(e.link) or e.get('summary', ''),
                "time": datetime.now().strftime("%H:%M"),
                "source": f.feed.get('title', 'חדשות'),
                "link": e.link
            })
            time.sleep(1)
    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    scrape()
