from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/enhance', methods=['POST'])
def enhance_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    image.save('input.png')

    # Run Real-ESRGAN to enhance the image
    subprocess.run(['python3', 'inference_realesrgan.py', '-n', 'RealESRGAN_x4plus', '--input', 'input.png', '--output', 'results'], check=True)

    with open('results/input_out.png', 'rb') as f:
        enhanced_image = f.read()

    return enhanced_image, 200, {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

