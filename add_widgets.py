import sys
from bs4 import BeautifulSoup

def modify_article():
    with open('article.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Update comments
    comments_div = soup.find('div', class_='wp-block-comments')
    if comments_div:
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
        comments_div.clear()
        comments_div.append(BeautifulSoup(comments_html, 'html.parser'))
        
    # 2. Add Sidebar Widgets
    sidebar = soup.find('aside', class_='sidebar')
    if sidebar:
        widgets_html = """
        <div class="sidebar-widgets">
            <div class="widget">
                <h4>Latest Posts</h4>
                <ul class="widget-list">
                    <li><a href="#">Real Estate vs. Stock Market: The Ultimate Investment Showdown</a></li>
                    <li><a href="#">Retirement Dreams: Why Senior Citizens Are Investing in NA Plots Near Pune</a></li>
                    <li><a href="#">Top 5 Emerging Areas for Plot Investments in Pune</a></li>
                </ul>
            </div>
            
            <div class="widget">
                <h4>Categories</h4>
                <ul class="widget-list">
                    <li><a href="#">Investment Tips</a></li>
                    <li><a href="#">Market Trends</a></li>
                    <li><a href="#">Pune Real Estate</a></li>
                    <li><a href="#">Retirement Planning</a></li>
                </ul>
            </div>
            
            <div class="widget">
                <h4>Archive</h4>
                <ul class="widget-list">
                    <li><a href="#">October 2025</a></li>
                    <li><a href="#">November 2025</a></li>
                    <li><a href="#">December 2025</a></li>
                </ul>
            </div>
            
            <div class="widget">
                <h4>Follow Us</h4>
                <div class="social-icons">
                    <a href="#" class="social-icon" aria-label="Facebook">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                    </a>
                    <a href="#" class="social-icon" aria-label="Twitter">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
                    </a>
                    <a href="#" class="social-icon" aria-label="Instagram">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                    </a>
                    <a href="#" class="social-icon" aria-label="LinkedIn">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                    </a>
                </div>
            </div>
        </div>
        """
        # Insert the widgets before the lead form
        widgets_soup = BeautifulSoup(widgets_html, 'html.parser')
        sidebar.insert(0, widgets_soup)
        
    with open('article.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Injected widgets and comments into article.html")

if __name__ == '__main__':
    modify_article()
