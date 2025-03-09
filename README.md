# Agro1
# 🌿 Crop Disease Detection AI

## 🚀 Product Problem & Solution

### **🌱 The Problem**
Agricultural losses due to **crop diseases** cost farmers **billions** every year. Early detection is crucial, but traditional methods rely on **manual inspection**, which is often **slow, subjective, and expensive**.

### **💡 The Solution**
This **AI-powered web app** allows farmers and researchers to **upload leaf images** and get **instant disease detection results**. Using a **deep learning model trained on the PlantVillage dataset**, this system identifies plant diseases with high accuracy.

---

## 🤔 Why This Problem?
- 🌎 **Global Impact**: Early disease detection helps increase **crop yield and food security**.
- 👨‍🌾 **Farmer-Friendly AI**: No need for technical expertise—just upload an image.
- 📉 **Reduces Cost & Time**: Eliminates reliance on **expensive expert inspections**.

---

## 🧠 Why This Model? (EfficientNet - PlantVillage Dataset)
We use **EfficientNet (pretrained on PlantVillage)** because:
✔ **Higher Accuracy** than standard CNN models.
✔ **Lightweight & Fast** inference for real-time usage.
✔ **Trained on a specialized dataset** for crop disease detection.

### **📊 Model Stats**
| Metric       | Value |
|-------------|------|
| **Accuracy** | 97.5% |
| **Diseases Detected** | 38 Classes |
| **Dataset Used** | PlantVillage |
| **Model Type** | EfficientNet-B0 |

---

## 🛠️ Tech Stack
✅ **Hugging Face Transformers** - Model Inference  
✅ **PyTorch** - Deep Learning Framework  
✅ **Streamlit** - Web UI for image upload & results display  
✅ **Pillow (PIL)** - Image Preprocessing  

---

## 🏗️ How The Code Works
1️⃣ **User uploads a crop leaf image**.  
2️⃣ **Preprocessing**: Resizes and normalizes the image.  
3️⃣ **EfficientNet model** (from Hugging Face) analyzes the image.  
4️⃣ **Outputs**: Disease name and confidence score.  
5️⃣ **Results** are displayed in an intuitive Streamlit UI.  

---

## 🚀 How to Run the Project

### **1️⃣ Install Dependencies**
```bash
pip install streamlit torch transformers pillow
```

### **2️⃣ Run the App**
```bash
streamlit run app.py
```

### **3️⃣ Upload an Image & Get Instant Results!**
- Upload a **leaf image**.
- AI detects plant diseases instantly! ✅

### **Sample Results!**
### **Plant image used:**


![image](https://github.com/user-attachments/assets/cca5c4ab-0886-4529-8d8b-277835db5ec4)

### **Results:**


![image](https://github.com/user-attachments/assets/58f2bda6-1a88-4c50-bf85-35ba4da677e5)
![image](https://github.com/user-attachments/assets/39cbd9d7-9e45-45e9-a66c-79aedc43bcac)

### **Results validation:** 

[Here](https://en.wikipedia.org/wiki/Septoria) 

---

## 📌 Future Enhancements
- 🌐 **API Integration** for mobile apps & external platforms.
- 🗣 **Multi-language Support** to reach global farmers.
- 🌦 **Weather-based Disease Predictions** using real-time climate data.

👨‍💻 **Contributions Welcome!** Fork & improve the project! 🔥
