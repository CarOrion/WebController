from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')  # Tarayıcıdan direkt girildiğinde burası çalışacak
def home():
    return render_template('index.html')  # "templates/index.html" dosyasını döndür

@app.route('/keypress', methods=['POST'])
def keypress():
    data = request.json
    key = data.get('key')
    print(f"Tuşa basıldı: {key}")  # Terminalde göster
    return {"status": "success", "key": key}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
