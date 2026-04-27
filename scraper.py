import feedparser
import json

# רשימת מקורות RSS
rss_feeds = [
   rss_feeds = [
   rss_feeds = [
    "https://www.now14.co.il/feed/",              # ערוץ 14
    "https://www.kol-barama.co.il/feed/",        # קול ברמה
    "https://www.93fm.co.il/feed/",              # קול חי
    "https://hm-news.co.il/feed/",               # המחדש
    "https://www.a7.org/rss.xml",                # ערוץ 7
    "https://www.israelhayom.co.il/rss.xml",     # ישראל היום
    "https://www.kikar.co.il/rss",               # כיכר השבת
    "https://www.bhol.co.il/rss",                # בחדרי חרדים
    "https://www.jdn.co.il/feed/",               # JDN
    "https://www.0404.co.il/?feed=rss2"          # 0404
]
]
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
