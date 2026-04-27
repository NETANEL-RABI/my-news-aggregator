import feedparser
import json
import requests
import os

def scrape():
    # רשימת אתרים אמינים
    feeds = [
        "https://www.now14.co.il/feed/",
        "https://www.jdn.co.il/feed/",
        "https://www.inn.co.il/rss.xml"
    ]
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    all_news = []

    for url in feeds:
        try:
            print(f"מנסה למשוך מ: {url}")
            resp = requests.get(url, headers=headers, timeout=10)
            feed = feedparser.parse(resp.content)
            
            for entry in feed.entries[:3]:
                all_news.append({
                    "title": entry.title,
                    "time": "עכשיו",
                    "source": feed.feed.get('title', 'חדשות'),
                    "link": entry.link
                })
        except Exception as e:
            print(f"שגיאה באתר {url}: {e}")

    # שמירה - אם הרשימה ריקה, הוא לא ימחק את הקובץ
    if all_news:
        with open('news.json', 'w', encoding='utf-8') as f:
            json.dump(all_news, f, ensure_ascii=False, indent=4)
        print(f"הצלחתי! נשמרו {len(all_news)} מבזקים.")
    else:
        print("לא נמצאו מבזקים חדשים, הקובץ לא עודכן.")

if __name__ == "__main__":
    scrape()
