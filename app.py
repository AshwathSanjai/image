from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send-message", methods=["POST"])
def handle_message():
    message = request.json["message"]

    try:
        response = openai.Image.create(
            prompt=message,
            n=1,
            size="256x256"
        )
        image_url = response['data'][0]['url']
        return {"image_url": image_url}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(debug=True)