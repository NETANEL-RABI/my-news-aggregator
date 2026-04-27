import feedparser
import json
import os
from datetime import datetime
import requests

# רשימת האתרים המעודכנת
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

def scrape_news():
    news_items = []
    
    # הגדרות שגורמות לאתרים לחשוב שאנחנו דפדפן אמיתי (מונע חסימות)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for url in rss_feeds:
        try:
            # משיכת התוכן עם Headers
            response = requests.get(url, headers=headers, timeout=10)
            feed = feedparser.parse(response.content)
            
            source_name = feed.feed.get('title', url.split('.')[1])
            
            for entry in feed.entries[:5]:  # לוקחים את 5 המבזקים האחרונים מכל אתר
                news_items.append({
                    "title": entry.title,
                    "link": entry.link,
                    "time": datetime.now().strftime("%H:%M"),
                    "source": source_name,
                    "body": entry.get('summary', '')[:100] + "..."
                })
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    # שמירה לקובץ news.json
    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(news_items, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    scrape_news()
