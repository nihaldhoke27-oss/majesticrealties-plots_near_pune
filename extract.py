import sys
from bs4 import BeautifulSoup

def extract():
    f1 = open(r'C:\Users\Utkar\.gemini\antigravity\brain\d8ca229d-d885-4451-88e0-753f54da6f81\.system_generated\steps\70\content.md', encoding='utf-8').read()
    soup1 = BeautifulSoup(f1, 'html.parser')
    
    print('--- INDEX ---')
    articles = soup1.find_all('article')
    for a in articles:
        title = a.find('h2').text.strip() if a.find('h2') else 'None'
        content_div = a.find('div', class_='entry-content')
        excerpt = content_div.text.strip() if content_div else 'None'
        img = a.find('img')['src'] if a.find('img') else 'None'
        link = a.find('a')['href'] if a.find('a') else 'None'
        print(f"TITLE: {title}")
        print(f"EXCERPT: {excerpt}")
        print(f"IMG: {img}")
        print(f"LINK: {link}")
        print('---')
        
    f2 = open(r'C:\Users\Utkar\.gemini\antigravity\brain\d8ca229d-d885-4451-88e0-753f54da6f81\.system_generated\steps\71\content.md', encoding='utf-8').read()
    soup2 = BeautifulSoup(f2, 'html.parser')
    
    print('--- ARTICLE ---')
    article_title = soup2.find('h1')
    print("H1:", article_title.text.strip() if article_title else "None")
    content = soup2.find('div', class_='entry-content')
    if content:
        # Instead of just text, let's grab the HTML inside to keep paragraphs and lists
        print(content.decode_contents())
    else:
        print('Not found')

if __name__ == '__main__':
    extract()
