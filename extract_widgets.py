import sys
from bs4 import BeautifulSoup

def extract_widgets():
    raw = open('new_article_raw.html', encoding='utf-8').read()
    soup = BeautifulSoup(raw, 'html.parser')
    
    # Comments usually have a specific class or id
    comments_section = soup.find(id='comments') or soup.find(class_='wp-block-comments') or soup.find(id='respond')
    
    # Sidebar widgets (Latest posts, category, archive, follow us)
    # usually in an aside or sidebar div
    sidebar = soup.find('aside') or soup.find(class_='sidebar') or soup.find(class_='widget-area')
    if not sidebar:
        # maybe look for specific blocks
        sidebar = soup.find(class_='wp-block-group sidebar-blog')
        
    out = "=== COMMENTS ===\n"
    if comments_section:
        out += str(comments_section)
    else:
        out += "No comments found\n"
        
    out += "\n=== SIDEBAR ===\n"
    if sidebar:
        out += str(sidebar)
    else:
        out += "No sidebar found\n"
        
    with open('extracted_widgets.html', 'w', encoding='utf-8') as f:
        f.write(out)

if __name__ == '__main__':
    extract_widgets()
