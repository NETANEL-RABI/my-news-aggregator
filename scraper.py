import feedparser
import json

# רשימת מקורות RSS (תוכל להוסיף עוד בהמשך)
rss_feeds = [
    "https://rss.walla.co.il/feed/1", # מבזקי וואלה
    ""https://www.ynet.co.il/Integration/StoryRss2.xml",
"https://www.emess.co.il/feed/"
    
]

all_news = []

for url in rss_feeds:
    feed = feedparser.parse(url)
    for entry in feed.entries[:10]: # 10 כתבות מכל מקור
        all_news.append({
            "title": entry.title,
            "link": entry.link,
            "source": feed.feed.title if hasattr(feed.feed, 'title') else "חדשות"
        })

# שמירה לקובץ news.json
with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=4)
