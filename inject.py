import sys
import re
from bs4 import BeautifulSoup

def inject():
    # Load original scraped index page
    idx_raw = open(r'C:\Users\Utkar\.gemini\antigravity\brain\d8ca229d-d885-4451-88e0-753f54da6f81\.system_generated\steps\70\content.md', encoding='utf-8').read()
    idx_soup = BeautifulSoup(idx_raw, 'html.parser')
    
    # In WordPress Gutenberg blocks, posts might be list items in a wp-block-post-template
    titles_elems = idx_soup.find_all('h3', class_=re.compile(r'wp-block-post-title'))
    if not titles_elems:
        titles_elems = [h3 for h3 in idx_soup.find_all('h3') if h3.find('a')]
    
    print(f"Found {len(titles_elems)} post titles")

    blog_cards_html = ""
    count = 0
    for title_elem in titles_elems:
        title = title_elem.get_text(strip=True)
        link_elem = title_elem.find('a')
        link = "article.html" # we are using the single article.html template
        
        # We need to find the parent li or block that contains this post
        # Typically wp-block-post-title is a sibling of the excerpt and image within the post template
        # Let's search near this element by looking at its parent chain
        parent = title_elem.parent
        if parent and parent.name == 'div' and not parent.has_attr('class'):
            parent = parent.parent
            
        # The image might be inside a preceding figure
        img_elem = None
        current = title_elem
        # Search backwards or in parent for figure
        while current.previous_sibling:
            current = current.previous_sibling
            if current.name == 'figure':
                img_elem = current.find('img')
                break
        
        # If not found, look globally in the parent's parent (assuming they are wrapped)
        if not img_elem and title_elem.find_previous('img'):
             img_elem = title_elem.find_previous('img')
             
        img_src = img_elem['src'] if img_elem and img_elem.has_attr('src') else 'https://images.unsplash.com/photo-1582407947304-fd86f028f716?q=80&w=1000'
        
        # Excerpt
        excerpt_elem = title_elem.find_next_sibling('div', class_=re.compile(r'wp-block-post-excerpt'))
        if not excerpt_elem and title_elem.parent:
            excerpt_elem = title_elem.parent.find('div', class_=re.compile(r'wp-block-post-excerpt'))
            
        excerpt = excerpt_elem.get_text(strip=True) if excerpt_elem else 'Read more about this exciting investment opportunity in Pune.'
        excerpt = excerpt.replace('Read more', '')
        
        card = f"""
        <a href="{link}" class="blog-card">
            <div class="card-image">
                <img src="{img_src}" alt="Plot">
                <div class="card-badge">Article</div>
            </div>
            <div class="card-content">
                <div class="card-meta">
                    <span>Recent</span> • <span>Read Article</span>
                </div>
                <h3 class="card-title">{title}</h3>
                <p class="card-excerpt">{excerpt}</p>
                <span class="read-more">Read Article <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
            </div>
        </a>
        """
        blog_cards_html += card
        count += 1
        if count >= 6:
            break

    print(f"Generated HTML for {count} cards.")

    # Now load local index.html and update
    local_idx_path = 'index.html'
    local_idx_raw = open(local_idx_path, encoding='utf-8').read()
    local_idx_soup = BeautifulSoup(local_idx_raw, 'html.parser')
    
    grid = local_idx_soup.find('div', class_='blog-grid')
    if grid and blog_cards_html:
        grid.clear()
        grid.append(BeautifulSoup(blog_cards_html, 'html.parser'))
        with open(local_idx_path, 'w', encoding='utf-8') as f:
            f.write(str(local_idx_soup))
            print("Updated index.html")
    else:
        print("Failed to find grid or generated 0 cards")

if __name__ == '__main__':
    inject()
