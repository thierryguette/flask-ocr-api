from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import os

# Spécifie le chemin vers tesseract.exe si nécessaire (adapté à Windows)
# Change le chemin ci-dessous si ton installation est différente
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr_process():
    if 'image' not in request.files:
        return jsonify({'status': 'error', 'message': 'Aucune image fournie'}), 400

    image_file = request.files['image']

    try:
        image = Image.open(image_file)
        text = pytesseract.image_to_string(image)

        response = {
            'status': 'success',
            'text': text
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Point d'entrée pour le lancement local
if __name__ == '__main__':
    app.run(debug=True)
