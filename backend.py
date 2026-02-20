from flask import Flask, redirect, render_template_string
import webbrowser
import threading
import time

app = Flask(__name__)

# HEDEF LİNK - BUNU DEĞİŞTİR
HEDEF_LINK = "https://grabify.link/0I5H2O"

# Ana sayfa - direkt yönlendirme
@app.route('/')
def index():
    # HTML ile yönlendirme
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Yönlendiriliyor...</title>
        <!-- Meta refresh ile anında yönlendirme -->
        <meta http-equiv="refresh" content="0; url={HEDEF_LINK}">
        <style>
            body {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }}
            .message {{
                font-size: 24px;
                animation: pulse 1.5s infinite;
            }}
            @keyframes pulse {{
                0% {{ opacity: 0.5; }}
                50% {{ opacity: 1; }}
                100% {{ opacity: 0.5; }}
            }}
        </style>
    </head>
    <body>
        <div class="message">
            ⚡ Yönlendiriliyorsunuz...<br>
            <small style="font-size: 14px;">{HEDEF_LINK}</small>
        </div>
        
        <!-- JavaScript ile anında yönlendirme (yedek) -->
        <script>
            // Hemen yönlendir
            window.location.replace("{HEDEF_LINK}");
            
            // Eğer çalışmazsa 1 saniye sonra tekrar dene
            setTimeout(function() {{
                window.location.href = "{HEDEF_LINK}";
            }}, 1000);
        </script>
    </body>
    </html>
    '''
    return html

# Direkt yönlendirme endpoint'i
@app.route('/go')
def go():
    return redirect(HEDEF_LINK, code=302)

# İkinci yönlendirme yöntemi
@app.route('/redirect')
def redirect_page():
    return redirect(HEDEF_LINK, code=301)

# Bilgi sayfası (opsiyonel)
@app.route('/info')
def info():
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Link Yönlendirici</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f0f0f0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 500px;
            }}
            h1 {{ color: #333; }}
            .link {{ 
                background: #667eea;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                text-decoration: none;
                display: inline-block;
                margin: 10px;
            }}
            .link:hover {{ background: #764ba2; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔗 Link Yönlendirici</h1>
            <p>Hedef link:</p>
            <code>{HEDEF_LINK}</code>
            <br><br>
            <a href="/" class="link">Ana Sayfa (Yönlendir)</a>
            <a href="/go" class="link">Direkt Git</a>
        </div>
    </body>
    </html>
    '''

# Tarayıcıyı otomatik aç
def open_browser():
    """Sunucu başladıktan 1 saniye sonra tarayıcıyı aç"""
    time.sleep(1)
    webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
    print('='*60)
    print('🚀 FLASK LİNK YÖNLENDİRİCİ BAŞLATILDI!')
    print('='*60)
    print(f'🎯 Hedef Link: {HEDEF_LINK}')
    print(f'🌐 Adres: http://localhost:5000')
    print(f'📌 Ana sayfa: http://localhost:5000/')
    print(f'📌 Direkt git: http://localhost:5000/go')
    print(f'📌 Bilgi: http://localhost:5000/info')
    print('='*60)
    print('✅ Siteye giren direkt hedefe yönlenecek!')
    print('❌ Durdurmak için Ctrl+C basın')
    print('='*60)
    
    # Tarayıcıyı otomatik aç (opsiyonel)
    # threading.Thread(target=open_browser).start()
    
    # Uygulamayı başlat
    app.run(host='0.0.0.0', port=5000, debug=False)
