css = """
/* Custom Widgets */
.sidebar-widgets { display: flex; flex-direction: column; gap: 2rem; margin-bottom: 2rem; }
.widget { background: var(--surface); padding: 1.5rem; border-radius: var(--radius-lg); border: 1px solid var(--border); box-shadow: var(--shadow-sm); }
.widget h4 { margin-top: 0; margin-bottom: 1rem; color: var(--text-dark); font-family: var(--font-heading); }
.widget-list { list-style: none; padding: 0; margin: 0; }
.widget-list li { margin-bottom: 0.75rem; border-bottom: 1px solid var(--border); padding-bottom: 0.75rem; }
.widget-list li:last-child { margin-bottom: 0; border-bottom: none; padding-bottom: 0; }
.widget-list a { color: var(--text); text-decoration: none; transition: var(--transition); }
.widget-list a:hover { color: var(--primary); }
.social-icons { display: flex; gap: 1rem; }
.social-icon { display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 50%; background: var(--bg-color); color: var(--text); transition: var(--transition); border: 1px solid var(--border); }
.social-icon:hover { background: var(--primary); color: white; border-color: var(--primary); transform: translateY(-3px); }

/* Comments Section */
.comments-section { margin-top: 4rem; padding-top: 2rem; border-top: 2px solid var(--border); }
.comments-section h3 { font-family: var(--font-heading); margin-bottom: 0.5rem; }
.comment-notes { font-size: 0.9rem; color: var(--text-light); margin-bottom: 2rem; }
.custom-comment-form .form-group { margin-bottom: 1.5rem; }
.custom-comment-form label { display: block; margin-bottom: 0.5rem; font-weight: 500; font-size: 0.9rem; }
.custom-comment-form textarea, .custom-comment-form input[type="text"], .custom-comment-form input[type="email"], .custom-comment-form input[type="url"] { width: 100%; padding: 0.75rem 1rem; border: 1px solid var(--border); border-radius: var(--radius-sm); font-family: inherit; transition: var(--transition); background: var(--surface); }
.custom-comment-form textarea:focus, .custom-comment-form input:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(255, 81, 1, 0.1); }
.form-group-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; }
.form-checkbox { display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 1.5rem; }
.form-checkbox input { margin-top: 0.3rem; }
.form-checkbox label { font-size: 0.9rem; color: var(--text); line-height: 1.5; }
"""

with open("style.css", "a", encoding="utf-8") as f:
    f.write(css)
