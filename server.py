from flask import Flask, send_from_directory
import logging
from datetime import datetime

app = Flask(__name__)

# ログの設定
logging.basicConfig(filename="access.log", level=logging.INFO, format="%(message)s")

@app.route("/beacon")
def beacon():
    # アクセス情報を取得
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    referrer = request.referrer if request.referrer else "No Referrer"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ログに記録
    log_entry = f"{timestamp} | IP: {ip} | Referrer: {referrer} | User-Agent: {user_agent}"
    logging.info(log_entry)
    print(log_entry)  # コンソールにも表示

    # 透明な1x1ピクセルの画像を返す
    return send_from_directory('static', 'beacon.png')


@app.route("/")
def index():
    return send_from_directory('', 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
