import os
import re

def slugify(title):
    s = title.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')

print("=== New Writeup Article ===\n")

title = input("Article title: ").strip()
slug = input(f"URL slug (or press Enter for '{slugify(title)}'): ").strip()
if not slug:
    slug = slugify(title)

tags = []
print("\nEnter tags (one per line, press Enter with empty line to finish):")
while True:
    tag = input("  Tag: ").strip()
    if not tag:
        break
    tags.append(tag)

month = input("\nMonth (e.g. June): ").strip()
year = input("Year: ").strip()
read_time = input("Read time (minutes): ").strip()

dir_path = os.path.join(os.path.dirname(__file__), slug)
os.makedirs(dir_path, exist_ok=True)

tag_html = "\n      ".join(f'<span class="article-tag">{t}</span>' for t in tags)

article_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - Danny Wang</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpath d='M8 10 L4 16 L8 22' stroke='%232563eb' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3Cline x1='18' y1='9' x2='14' y2='23' stroke='%232563eb' stroke-width='3' stroke-linecap='round'/%3E%3Cpath d='M24 10 L28 16 L24 22' stroke='%232563eb' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<meta property="og:title" content="{title} - Danny Wang">
<meta property="og:description" content="">
<meta property="og:url" content="https://dannywang.dev/writeups/{slug}/">
<meta property="og:type" content="article">
<link rel="canonical" href="https://dannywang.dev/writeups/{slug}/">
<style>
*, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
:root {{
  --bg: #ffffff; --bg-subtle: #f8f9fa; --text-primary: #111827; --text-secondary: #4b5563;
  --text-tertiary: #6b7280; --accent: #2563eb; --accent-hover: #1d4ed8; --accent-light: #eef2ff;
  --border: #e5e7eb; --shadow: 0 1px 2px rgba(0,0,0,0.04); --shadow-card: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.03);
  --radius: 0.5rem; --radius-sm: 0.375rem; --radius-full: 9999px; --sidebar-width: 350px;
  --font-body: Georgia, 'Times New Roman', serif;
  --font-heading: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'SF Mono', Menlo, Monaco, 'Cascadia Code', 'Courier New', monospace;
  --transition: 0.2s ease;
}}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: var(--font-body); background: var(--bg); color: var(--text-primary);
  line-height: 1.7; font-size: 15px; display: flex; min-height: 100vh; animation: fadeIn 0.6s ease;
}}
@keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
h1, h2, h3, .sidebar h1 {{ font-family: var(--font-heading); }}
a {{ color: var(--accent); text-decoration: none; transition: color var(--transition); }}
a:hover {{ color: var(--accent-hover); }}
img {{ max-width: 100%; display: block; }}
ul {{ list-style: none; }}
.sidebar {{
  width: var(--sidebar-width); min-height: 100vh; position: fixed; top: 0; left: 0;
  background: var(--bg); border-right: 1px solid var(--border); display: flex;
  flex-direction: column; padding: 2rem 1.5rem; z-index: 100; overflow-y: auto;
}}
.sidebar-inner {{ display: flex; flex-direction: column; align-items: flex-start; gap: 0.5rem; width: 100%; }}
.avatar {{
  width: 128px; height: 128px; border-radius: 50%; background: var(--accent-light); color: var(--accent);
  display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 600;
  font-family: var(--font-mono); flex-shrink: 0; margin-bottom: 0.5rem;
}}
.sidebar h1 {{ font-size: 1.2rem; font-weight: 600; color: var(--text-primary); line-height: 1.3; letter-spacing: -0.01em; }}
.tagline {{ font-size: 0.88rem; color: var(--text-secondary); line-height: 1.5; font-family: var(--font-body); margin-bottom: 0.125rem; }}
.info-line {{ display: flex; align-items: center; gap: 0.45rem; font-size: 0.88rem; color: var(--text-tertiary); font-family: var(--font-body); }}
.email-row {{ display: flex; align-items: center; gap: 0.4rem; margin-top: 0.25rem; width: 100%; }}
.email-row a {{ font-size: 0.88rem; color: var(--text-secondary); word-break: break-all; font-family: var(--font-body); }}
.social-links {{ display: flex; align-items: center; flex-wrap: nowrap; gap: 0.15rem; margin-top: 0.5rem; }}
.social-link {{
  display: inline-flex; align-items: center; gap: 0.3rem; font-size: 0.72rem;
  font-family: var(--font-heading); color: var(--text-tertiary);
  padding: 0.2rem 0.35rem; border-radius: var(--radius-sm); transition: all var(--transition);
}}
.social-link:hover {{ color: var(--accent); background: var(--accent-light); }}
.hamburger {{ display: none; }}
.main {{ margin-left: var(--sidebar-width); flex: 1; padding: 3rem 3rem 0; max-width: 820px; }}

.sidebar-section-title {{
  font-size: 0.65rem; font-weight: 600; font-family: var(--font-heading);
  color: var(--text-tertiary); text-transform: uppercase; letter-spacing: 0.06em;
  margin-top: 0.5rem; margin-bottom: 0.2rem;
}}
.sidebar-experience {{ display: flex; flex-direction: column; gap: 0.25rem; width: 100%; }}
.sidebar-experience-item {{ font-size: 0.78rem; color: var(--text-secondary); font-family: var(--font-body); line-height: 1.4; }}
.sidebar-experience-item .role {{ font-weight: 600; color: var(--text-primary); }}
.sidebar-experience-item .date {{ font-size: 0.68rem; font-family: var(--font-mono); color: var(--text-tertiary); }}
.sidebar-experience-item a, .sidebar-experience-item a:visited {{ color: inherit; text-decoration: none; cursor: default; }}
.sidebar-experience-item a:hover {{ text-decoration: underline; cursor: pointer; }}

.sidebar-link,
.sidebar-link:visited {{
  display: inline-block; font-size: 0.78rem; font-family: var(--font-heading);
  color: var(--text-tertiary); text-decoration: none; margin-top: 0.6rem; transition: color var(--transition);
}}
.sidebar-link:hover {{ color: var(--accent); }}

.section {{ margin-bottom: 3rem; }}
.footer {{ padding: 1.25rem 0 2.5rem; border-top: 1px solid var(--border); margin-top: 1.5rem; font-size: 0.75rem; color: var(--text-tertiary); font-family: var(--font-body); }}

.article {{ max-width: 680px; }}
.article h1 {{ font-size: 1.6rem; font-weight: 700; margin-bottom: 0.3rem; line-height: 1.3; }}
.article .byline {{ font-size: 0.82rem; color: var(--text-tertiary); font-family: var(--font-mono); margin-bottom: 1.5rem; }}
.article h2 {{ font-size: 1.2rem; font-weight: 600; margin-top: 2rem; margin-bottom: 0.6rem; color: var(--text-primary); }}
.article h3 {{ font-size: 1.05rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.4rem; }}
.article p {{ margin-bottom: 1rem; color: var(--text-secondary); line-height: 1.8; }}
.article ul, .article ol {{ margin-bottom: 1rem; padding-left: 1.5rem; color: var(--text-secondary); line-height: 1.8; }}
.article li {{ margin-bottom: 0.3rem; }}
.article code {{
  font-family: var(--font-mono); font-size: 0.82rem; background: var(--bg-subtle);
  padding: 0.15rem 0.4rem; border-radius: var(--radius-sm); border: 1px solid var(--border);
}}
.article pre {{
  background: var(--bg-subtle); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 1rem; overflow-x: auto; margin-bottom: 1rem; font-size: 0.82rem; line-height: 1.5;
}}
.article pre code {{ background: none; border: none; padding: 0; }}
.article-back {{ display: inline-block; margin-bottom: 1.5rem; font-size: 0.85rem; font-family: var(--font-heading); font-weight: 500; }}
.article-tags {{ display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.5rem; margin-bottom: 1.5rem; }}
.article-tag {{
  font-size: 0.65rem; font-family: var(--font-mono); background: var(--accent-light);
  color: var(--accent); padding: 0.15rem 0.45rem; border-radius: var(--radius-full); font-weight: 500;
}}
@media (max-width: 1023px) {{
  body {{ flex-direction: column; }}
  .sidebar {{ position: relative; width: 100%; min-height: auto; border-right: none; border-bottom: 1px solid var(--border); padding: 1rem 1.25rem; flex-direction: row; align-items: center; flex-wrap: wrap; }}
  .sidebar-inner {{ flex-direction: row; align-items: center; width: 100%; gap: 0.75rem; flex-wrap: wrap; }}
  .avatar {{ width: 44px; height: 44px; font-size: 0.9rem; margin-bottom: 0; flex-shrink: 0; }}
  .sidebar h1 {{ font-size: 1rem; }}
  .sidebar .tagline, .sidebar .info-line, .sidebar .sidebar-section-title, .sidebar .sidebar-experience, .sidebar .email-row, .sidebar .social-links, .sidebar .resume-btn, .sidebar .sidebar-link {{ display: none; }}
  .sidebar-mobile-content {{ display: flex; align-items: center; gap: 0.6rem; width: 100%; }}
  .hamburger {{ display: inline-flex; align-items: center; justify-content: center; background: none; border: none; cursor: pointer; color: var(--text-secondary); padding: 0.3rem; border-radius: var(--radius-sm); transition: all var(--transition); flex-shrink: 0; margin-left: auto; }}
  .hamburger:hover {{ color: var(--accent); background: var(--accent-light); }}
  .sidebar.expanded {{ flex-direction: column; align-items: stretch; }}
  .sidebar.expanded .sidebar-inner {{ flex-direction: column; align-items: flex-start; width: 100%; gap: 0.5rem; }}
  .sidebar.expanded .tagline, .sidebar.expanded .info-line, .sidebar.expanded .sidebar-section-title, .sidebar.expanded .sidebar-experience, .sidebar.expanded .email-row, .sidebar.expanded .social-links, .sidebar.expanded .resume-btn, .sidebar.expanded .sidebar-link {{ display: flex; }}
  .sidebar.expanded .sidebar-mobile-content {{ width: 100%; }}
  .main {{ margin-left: 0; padding: 1.5rem 1.5rem 0; }}
}}
@media (max-width: 767px) {{
  .sidebar {{ padding: 0.75rem 1rem; }}
  .main {{ padding: 1.25rem 1rem 0; }}
  .article h1 {{ font-size: 1.3rem; }}
  .article h2 {{ font-size: 1.05rem; }}
}}
@media (min-width: 1024px) {{
  .sidebar-mobile-content {{ display: flex; flex-direction: column; width: 100%; }}
  .hamburger {{ display: none; }}
}}
</style>
</head>
<body>

<aside class="sidebar" id="sidebar">
  <div class="sidebar-mobile-content">
    <div class="avatar" aria-label="Danny Wang avatar">DW</div>
    <div style="flex-grow:1;min-width:0;overflow:hidden;"><h1>Danny Wang</h1></div>
    <button class="hamburger" id="hamburger" aria-label="Toggle menu">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
  </div>
  <div class="sidebar-inner" id="sidebarInner">
    <p class="tagline">Student &amp; Software Developer | Competitive Programmer | ML Enthusiast</p>
    <span class="info-line">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
      Calgary, Alberta, Canada
    </span>
    <span class="info-line">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
      Sir Winston Churchill HS - Grade 10 IB
    </span>
    <span class="info-line">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
      4.0 GPA | 97% Average
    </span>
    <div class="sidebar-section-title">Experience</div>
    <div class="sidebar-experience">
      <div class="sidebar-experience-item"><span class="role">Executive</span> &middot; <a href="https://www.mathattacksociety.org" target="_blank">Math Attack Society</a> <span class="date">2025-Present</span></div>
      <div class="sidebar-experience-item"><span class="role">Executive</span> &middot; <a href="https://archallenge.org" target="_blank">Alpine Reasoning Challenge</a> <span class="date">2025-Present</span></div>
      <div class="sidebar-experience-item"><span class="role">Entrepreneur</span> &middot; eBay Business <span class="date">2024-2026</span></div>
      <div class="sidebar-experience-item"><span class="role">Co-President</span> &middot; Chess Club <span class="date">2023-2025</span></div>
    </div>
    <div class="email-row">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
      <a href="mailto:dannywang930@gmail.com">dannywang930@gmail.com</a>
      <button class="copy-btn" data-email="dannywang930@gmail.com" aria-label="Copy email">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
        <span class="copy-tooltip">Copied!</span>
      </button>
    </div>
    <div class="social-links">
      <a href="https://github.com/ThePeeps191" target="_blank" rel="noopener" class="social-link">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.438 9.8 8.205 11.387.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.756-1.333-1.756-1.089-.744.083-.729.083-.729 1.205.085 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 21.795 24 17.295 24 12 24 5.37 18.63 0 12 0z"/></svg>
        GitHub
      </a>
      <a href="https://www.linkedin.com/in/dannywangdev/" target="_blank" rel="noopener" class="social-link">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        LinkedIn
      </a>
      <a href="https://codeforces.com/profile/danny.wang" target="_blank" rel="noopener" class="social-link">
        <svg width="15" height="15" viewBox="0 0 156 117.6" fill="currentColor"><path d="M30.3,32.7H9c-5,0-9,4.1-9,9v64.7c0,5,4.1,9,9,9h21.3c5,0,9-4.1,9-9V41.7C39.4,36.7,35.3,32.7,30.3,32.7z"/><path d="M84.6,0H63.3c-5,0-9,4.1-9,9v97.4c0,5,4.1,9,9,9h21.3c5,0,9-4.1,9-9V9C93.6,4.1,89.6,0,84.6,0z"/><path d="M138.7,45.1h-21.3c-5,0-9,4.1-9,9v52.3c0,5,4.1,9,9,9h21.3c5,0,9-4.1,9-9V54.1C147.7,49.1,143.7,45.1,138.7,45.1z"/></svg>
        Codeforces
      </a>
    </div>
    <a href="../../dannywang_resume.pdf" target="_blank" class="resume-btn">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
      Download Resume
    </a>
    <a href="../../index.html" class="sidebar-link">&larr; Portfolio</a>
  </div>
</aside>

<main class="main">
  <section class="section article">

    <a href="../index.html" class="article-back">&larr; Back to Writeups</a>

    <h1>{title}</h1>
    <div class="article-tags">
{tag_html}
    </div>
    <p class="byline">{month} {year} &middot; {read_time} min read</p>

    <p>Write description here</p>

    <h2>Section Title</h2>
    <p>Content goes here. Write in full paragraphs with <code>inline code</code> and code blocks as needed.</p>

    <pre><code>// Code block placeholder
int main() {{
    return 0;
}}</code></pre>

  </section>

  <footer class="footer">
    &copy; 2026 Danny Wang &middot; <a href="../../index.html">Portfolio</a>
  </footer>
</main>

<script>
(function() {{
  const sidebar = document.getElementById('sidebar');
  const hamburger = document.getElementById('hamburger');
  if (hamburger && sidebar) {{
    hamburger.addEventListener('click', function(e) {{
      e.stopPropagation();
      sidebar.classList.toggle('expanded');
    }});
    document.addEventListener('click', function(e) {{
      if (!sidebar.contains(e.target) && sidebar.classList.contains('expanded')) {{
        sidebar.classList.remove('expanded');
      }}
    }});
  }}
}})();
</script>
</body>
</html>"""

filepath = os.path.join(dir_path, "index.html")
with open(filepath, "w", encoding="utf-8") as f:
    f.write(article_html)

print(f"\nArticle created at writeups/{slug}/index.html")
print(f"URL: https://dannywang.dev/writeups/{slug}/")
