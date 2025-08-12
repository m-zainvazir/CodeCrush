# 👨‍💻 CodeCrush 
### 🚀 Your AI-Powered FAANG Interview Coach

[![Streamlit](https://img.shields.io/badge/Deployed_on-Streamlit_Cloud-FF4B4B?logo=streamlit)](https://your-app-url.streamlit.app)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python)](https://www.python.org/)

> Real-time FAANG interview simulator powered by **Groq's LPU** (1,000+ tokens/sec) and **Llama3-70B**, with near-zero latency responses.


<img src="src/Code Crush without side.jpg" alt="Code-Crush-without-side" border="0">
<img src="src/Code Crush how.jpg" alt="Code Crush how" border="0">


## 🔥 Key Features
| Feature | Description |
|---------|-------------|
| **⚡ Instant Responses** | 800-1000 tokens/sec via Groq LPU (vs. 20-30/sec on local LLMs) |
| **🎯 Premium Model** | Meta's Llama3-70B (outperforms 7B/8B parameter models) |
| **📊 Adaptive Interviews** | Scales difficulty based on user performance |
| **💻 Multi-format Input** | Handles code snippets, system diagrams, and theory questions |
| **🔍 Code Analysis** | Explains errors and suggests optimizations |

## 🛠️ Tech Stack
| Component     | Stack                                   |
| ------------- | --------------------------------------- |
| **AI Engine** | Groq API + LLaMA3-70B                   |
| **Framework** | LangChain (prompt + memory)             |
| **Interface** | Streamlit (Community Cloud)             |
| **Security**  | `.env` / `secrets.toml` for key storage |
 

## 📈 Impact  

- **Solved key pain points** in interview prep:  
  - Slow response times in local/offline models  
  - Static, non-adaptive questions  
  - Lack of real-time feedback  
- **Created a realistic simulation** of FAANG interview experience without GPU setup.  



## 🔧 Installation  

```bash
# Clone the repository
git clone https://github.com/m-zainvazir/codecrush.git
cd codecrush

# Create virtual environment
conda create -n codecrush python=3.10
conda activate codecrush

# Install dependencies
pip install -r requirements.txt
```


## ▶️ Usage  

```bash
streamlit run app.py
```

Make sure to set your **Groq API key** in `.streamlit/secrets.toml`:  

```toml
GROQ_API_KEY = "your_api_key_here"
```



## 🤝 Contributing  

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.  


## 📜 License  

This project is licensed under the MIT License.  
