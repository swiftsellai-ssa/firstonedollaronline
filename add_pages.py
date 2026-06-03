import os

pages = ['index.html', '1-idea.html', '1-idea-unlocked.html', 'the-dollar-game.html', 'secret-box.html']

speculation_script = '''
  <script type="speculationrules">
  {
    "prerender": [{
      "where": {
        "href_matches": "/*"
      },
      "eagerness": "moderate"
    }]
  }
  </script>
'''

for page in pages:
    if not os.path.exists(page): continue
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<script type="speculationrules">' not in content:
        content = content.replace('</head>', speculation_script + '</head>')
    
    content = content.replace('<a href="#">Terms</a>', '<a href="terms.html">Terms</a>')
    content = content.replace('<a href="#">Privacy</a>', '<a href="privacy.html">Privacy</a>')
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)

terms_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Terms of Service - First$1Online</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
  <style>
    :root { --primary: #3b82f6; --text: #e0f7ff; --text-light: #9ca3af; --bg: #0a0e1f; --white: #111827; --accent: #10b981; }
    * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', system-ui, sans-serif; }
    body { background: var(--bg); color: var(--text); line-height: 1.6; padding: 2rem 5%; }
    .container { max-width: 800px; margin: 0 auto; background: var(--white); padding: 3rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.5); border: 1px solid #1e293b; }
    h1 { color: var(--accent); margin-bottom: 2rem; }
    h2 { color: var(--primary); margin-top: 2rem; margin-bottom: 1rem; }
    p { margin-bottom: 1rem; color: var(--text-light); }
    a { color: var(--primary); text-decoration: none; }
    a:hover { text-decoration: underline; }
    .back { display: inline-block; margin-bottom: 2rem; font-weight: bold; }
  </style>
</head>
<body>
  <div class="container">
    <a href="index.html" class="back">← Back to Home</a>
    <h1>Terms of Service</h1>
    <p>Last updated: May 2026</p>
    
    <h2>1. Acceptance of Terms</h2>
    <p>By accessing and using First$1Online ("the Website"), you agree to be bound by these Terms of Service.</p>
    
    <h2>2. Digital Products</h2>
    <p>All sales of digital products (including the $1 Idea Vault and Notion Blueprint) are final. Upon payment, you receive instant access to the digital content. Due to the nature of digital goods, we do not offer refunds once access has been granted.</p>
    
    <h2>3. Intellectual Property</h2>
    <p>The content, organization, graphics, design, and other matters related to the Website are protected under applicable copyrights and intellectual property rights. The copying, redistribution, or publication by you of any such matters or any part of the Website is strictly prohibited without our express written permission.</p>
    
    <h2>4. Limitation of Liability</h2>
    <p>First$1Online and its content are provided "as is" and without warranties of any kind. We do not guarantee that the ideas or blueprints provided will result in specific financial outcomes or business success. Your results will depend entirely on your own effort and execution.</p>

    <h2>5. Contact</h2>
    <p>If you have any questions about these Terms, please reach out via <a href="https://x.com/gabriel_raiseos" target="_blank">Twitter/X (@gabriel_raiseos)</a>.</p>
  </div>
</body>
</html>'''

with open('terms.html', 'w', encoding='utf-8') as f:
    f.write(terms_content)

privacy_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Privacy Policy - First$1Online</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
  <style>
    :root { --primary: #3b82f6; --text: #e0f7ff; --text-light: #9ca3af; --bg: #0a0e1f; --white: #111827; --accent: #10b981; }
    * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', system-ui, sans-serif; }
    body { background: var(--bg); color: var(--text); line-height: 1.6; padding: 2rem 5%; }
    .container { max-width: 800px; margin: 0 auto; background: var(--white); padding: 3rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.5); border: 1px solid #1e293b; }
    h1 { color: var(--accent); margin-bottom: 2rem; }
    h2 { color: var(--primary); margin-top: 2rem; margin-bottom: 1rem; }
    p { margin-bottom: 1rem; color: var(--text-light); }
    a { color: var(--primary); text-decoration: none; }
    a:hover { text-decoration: underline; }
    .back { display: inline-block; margin-bottom: 2rem; font-weight: bold; }
  </style>
</head>
<body>
  <div class="container">
    <a href="index.html" class="back">← Back to Home</a>
    <h1>Privacy Policy</h1>
    <p>Last updated: May 2026</p>
    
    <h2>1. Information We Collect</h2>
    <p>When you visit First$1Online, we collect basic analytics data to understand how our site is used. When you make a purchase, payment processing is securely handled by Stripe. We do not store or process your credit card information directly.</p>
    
    <h2>2. How We Use Your Information</h2>
    <p>We use your information solely to provide access to our digital products, communicate with you regarding your purchase, and improve our website's user experience.</p>
    
    <h2>3. Third-Party Services</h2>
    <p>We use third-party services like Stripe for payment processing and Notion for content delivery. These services have their own privacy policies governing how they handle your data.</p>
    
    <h2>4. Data Protection</h2>
    <p>We implement standard security measures to protect against unauthorized access or alteration of your personal information. However, no internet transmission is entirely secure, and we cannot guarantee absolute data security.</p>
    
    <h2>5. Contact Us</h2>
    <p>For any privacy-related concerns, please contact us via <a href="https://x.com/gabriel_raiseos" target="_blank">Twitter/X (@gabriel_raiseos)</a>.</p>
  </div>
</body>
</html>'''

with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(privacy_content)

print("done")
