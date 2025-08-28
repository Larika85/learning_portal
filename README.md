# 📚 AI-Powered Learning Path Generator  

An interactive web app built with **Streamlit** and **Gemini API (via LangChain)** that generates a structured, day-wise learning path based on your goal. 🚀  

---

## ✨ Features  
- Enter any **learning goal** (e.g., *“Learn Python basics in 3 days”*).  
- Automatically generates a **day-wise roadmap** with topics, explanations, and YouTube search keywords.  
- Built with **Streamlit** for a simple, interactive UI.  
- Uses **Google’s Gemini API** through `langchain-google-genai`.  

---

## 🛠️ Installation & Setup  

### 1. Clone the Repository  
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Create Virtual Environment (Recommended)  
```bash
python -m venv venv
```
Activate it:  
- **Windows (PowerShell):**  
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**  
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key  
This app requires a **Google API Key** for Gemini.  

1. Get your API key from [Google AI Studio](https://aistudio.google.com/).  
2. Launch the app and enter the key in the sidebar.  

---

## ▶️ Run the App  
```bash
streamlit run app.py
```

The app will open in your browser (usually at `http://localhost:8501`).  

---

## 📂 Project Structure  
```
├── app.py              # Streamlit UI
├── utils.py            # Helper functions to call Gemini API
├── prompt.py           # Prompt template for generating learning paths
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📸 Example Usage  
- Input: *“I want to learn Python basics in 3 days”*  
- Output:  
  ```
  Day 1:
  Topic: Python Syntax & Basics
  Explanation: Introduction to variables, data types, and operators.
  YouTube: Python basics for beginners
  ...
  ```  

---

## 🤝 Contributing  
Pull requests are welcome! Feel free to fork the repo and open issues for bugs/features.  

---

## 📜 License  
This project is licensed under the MIT License.  
