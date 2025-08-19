from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB_NAME = "database.db"

# Veritabanı bağlantısı
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# Ana sayfa
@app.route("/")
def index():
    return render_template("index.html")

# Kullanıcı ekleme
@app.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()
        return redirect("/users")

    return render_template("add.html")

# Kullanıcıları listeleme
@app.route("/users")
def list_users():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    conn.close()
    return render_template("users.html", users=users)

# ✅ Admin paneli - tüm tabloları listele
@app.route("/admin")
def admin_panel():
    conn = get_db()
    cur = conn.cursor()

    # Tabloları al
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row["name"] for row in cur.fetchall()]

    db_data = {}
    for table in tables:
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        db_data[table] = rows

    conn.close()
    return render_template("admin.html", data=db_data)
    

if __name__ == "__main__":
    conn = sqlite3.connect(DB_NAME)
    with open("schema.sql") as f:
        conn.executescript(f.read())
    conn.close()

    app.run(debug=True)
