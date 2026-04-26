import feedparser
import json

# רשימת מקורות RSS
rss_feeds = [
    "https://rss.walla.co.il/feed/1",
    "https://www.ynet.co.il/Integration/StoryRss2.xml"
]

all_news = []

for url in rss_feeds:
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]:
            all_news.append({
                "title": entry.title,
                "link": entry.link,
                "source": feed.feed.title if hasattr(feed.feed, 'title') else "חדשות"
            })
    except Exception as e:
        print(f"Error parsing {url}: {e}")

# שמירה לקובץ news.json
with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=4)
