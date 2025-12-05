from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("private/database.db")
        cursor = conn.cursor()

        # INTENTIONALLY UNSAFE QUERY FOR CTF PURPOSES
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        try:
            result = cursor.execute(query).fetchone()
        except Exception as e:
            return f"SQL Error: {str(e)}"

        if result:
            flag = cursor.execute("SELECT value FROM flag").fetchone()[0]
            message = flag
        else:
            message = "Login failed."

        conn.close()

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)