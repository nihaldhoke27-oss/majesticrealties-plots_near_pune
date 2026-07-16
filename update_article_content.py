import sys
from bs4 import BeautifulSoup

def update_article():
    with open('new_article_raw.html', 'r', encoding='utf-8') as f:
        new_raw = f.read()
    new_soup = BeautifulSoup(new_raw, 'html.parser')
    
    art_content = new_soup.find('div', class_='entry-content')
    art_title = new_soup.find('h1')
    title_text = art_title.get_text(strip=True) if art_title else "Real Estate Growth: Importance of Capital Asset, Title Deed, and Registry"
    
    if art_content:
        # Also remove the wp-block-comments from art_content if it's there
        # because we added our own custom comments section below it.
        # Actually in our previous script we just appended to it.
        # Let's clean the extracted content
        wp_comments = art_content.find('div', class_='wp-block-comments')
        if wp_comments:
            wp_comments.decompose()
            
        with open('article.html', 'r', encoding='utf-8') as f:
            local_raw = f.read()
            
        local_soup = BeautifulSoup(local_raw, 'html.parser')
        
        # update title
        h1 = local_soup.find('h1', class_='article-title')
        if h1:
            h1.string = title_text
            
        # update title tag
        title_tag = local_soup.find('title')
        if title_tag:
            title_tag.string = f"{title_text} - Majestic Realties"
            
        # update body
        body = local_soup.find('div', class_='article-body')
        if body:
            # We want to replace the content but KEEP our custom comments section which is now inside article.html ?
            # Wait, in article.html the comments section is currently appended INSIDE 'div.wp-block-comments' which was inside article-body originally.
            # But we are clearing article-body.
            # So we should save our custom comments section first.
            custom_comments = body.find('div', class_='comments-section')
            
            body.clear()
            body.append(BeautifulSoup(art_content.decode_contents(), 'html.parser'))
            
            if custom_comments:
                body.append(custom_comments)
            else:
                # Re-add it if we lost it
                comments_html = """
                <div class="comments-section">
                    <h3>Leave a Reply</h3>
                    <p class="comment-notes">Your email address will not be published. Required fields are marked *</p>
                    <form class="custom-comment-form" action="#" method="post">
                        <div class="form-group">
                            <label>Comment *</label>
                            <textarea rows="5" required></textarea>
                        </div>
                        <div class="form-group-row">
                            <div class="form-group">
                                <label>Name *</label>
                                <input type="text" required>
                            </div>
                            <div class="form-group">
                                <label>Email *</label>
                                <input type="email" required>
                            </div>
                            <div class="form-group">
                                <label>Website</label>
                                <input type="url">
                            </div>
                        </div>
                        <div class="form-checkbox">
                            <input type="checkbox" id="save-info">
                            <label for="save-info">Save my name, email, and website in this browser for the next time I comment.</label>
                        </div>
                        <button type="submit" class="btn-primary" style="margin-top: 1rem;">Post Comment</button>
                    </form>
                </div>
                """
                body.append(BeautifulSoup(comments_html, 'html.parser'))
                
            with open('article.html', 'w', encoding='utf-8') as f:
                f.write(str(local_soup))
            print("Updated article content successfully.")
    else:
        print("Could not find entry-content in new_article_raw.html")

if __name__ == '__main__':
    update_article()
