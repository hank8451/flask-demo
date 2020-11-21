from flask import Flask
app = Flask(
    __name__,
    # static_folder= "static",   # 靜態檔案的資料夾名稱（預設）
    # static_url_path= "/static" # 靜態檔案對應的（預設
    static_folder = "public",
    static_url_path = "/"
)

@app.route("/")
def home():
    return "Hello Flask"

@app.route("/test")
def test():
    return "I am a test"

@app.route("/user/<user_name>")
def log_in(user_name):
    return "Hello " + user_name

if __name__ == "__main__":
    app.run()