import feedparser
import json
import requests
from bs4 import BeautifulSoup
import time

def get_full_article(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # חיפוש הטקסט המרכזי (מתאים לרוב אתרי החדשות בישראל)
        paragraphs = soup.find_all(['p', 'div'], class_=['entry-content', 'article-content', 'content'])
        if not paragraphs:
            paragraphs = soup.find_all('p')
            
        full_text = "\n".join([p.get_text() for p in paragraphs if len(p.get_text()) > 50])
        return full_text[:2000] # לוקח עד 2000 תווים כדי לא להכביד
    except:
        return ""

def scrape():
    feeds = ["https://www.now14.co.il/feed/", "https://www.jdn.co.il/feed/"]
    all_news = []
    
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            print(f"מושך כתבה מלאה: {entry.title}")
            full_content = get_full_article(entry.link)
            
            all_news.append({
                "title": entry.title,
                "time": time.strftime("%H:%M"),
                "source": feed.feed.get('title', 'חדשות'),
                "body": full_content if full_content else entry.get('summary', '')
            })
            time.sleep(1) # הפסקה קצרה כדי לא להיחסם

    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(all_news, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    scrape()
