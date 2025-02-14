import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# מקבל את ה-API Key מהסביבה
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "ברוך הבא לבוט תכנון הטיול בתאילנד!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    if not user_input:
        return jsonify({"error": "נא לספק הודעה"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "אתה עוזר אישי שמתכנן טיולים בתאילנד"},
                  {"role": "user", "content": user_input}]
    )

    bot_reply = response["choices"][0]["message"]["content"]

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # הגדרת הפורט לפי מה ש-Render מחפש
    app.run(host="0.0.0.0", port=port)
