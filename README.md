# 🌾 Plant Disease Detection using CNN & OpenCV  

A deep learning project to **detect rice plant diseases** using **Convolutional Neural Networks (CNNs)** and **OpenCV**.  
It includes an interactive **Streamlit web app** where users can upload images of rice leaves and get instant predictions.  

---

## 🚀 Features
- 📷 Upload rice plant leaf images for disease prediction  
- 🤖 Trained **CNN model** for classification  
- 🖼️ Image preprocessing with **OpenCV & NumPy**  
- 🌐 User-friendly **Streamlit interface**  
- 🔬 Built on **TensorFlow/Keras** for deep learning  

---

## 🛠️ Tech Stack
- **Python 3.8+**  
- **TensorFlow / Keras**  
- **OpenCV**  
- **NumPy, Pandas, Matplotlib, Seaborn**  
- **Streamlit** (for web app UI)  

---

## 📦 Installation & Setup  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YourUsername/plant-disease-detection.git
   cd plant-disease-detection
Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies
pip install -r requirements.txt
Run the app
streamlit run app.py

📊 Model Training
Preprocessing done with OpenCV (resizing, normalization, augmentation).
CNN trained on Rice Disease Dataset (can be swapped with other plant disease datasets).
Evaluation metrics: Accuracy, Confusion Matrix, Precision/Recall.

📌 Future Improvements
Extend dataset for more plant species
Add mobile app integration
Deploy model with FastAPI / Docker
