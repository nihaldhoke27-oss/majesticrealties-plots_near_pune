import sys
from bs4 import BeautifulSoup

def swap_sidebar():
    with open('article.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    sidebar = soup.find('aside', class_='sidebar')
    
    if sidebar:
        widgets = sidebar.find('div', class_='sidebar-widgets')
        lead_form = sidebar.find('div', class_='lead-form-card')
        
        if widgets and lead_form:
            # We want the lead_form to be first
            lead_form.extract()
            sidebar.insert(0, lead_form)
            
            with open('article.html', 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print("Swapped successfully")
        else:
            print("Couldn't find both elements")

if __name__ == '__main__':
    swap_sidebar()
