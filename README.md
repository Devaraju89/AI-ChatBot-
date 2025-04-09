# AI-ChatBot-
ChatBot for VIRTUAL THERAPY ASSISTANT
# 💬 Virtual Therapy Assistant

A user-friendly virtual chatbot designed to simulate a Cognitive Behavioral Therapy (CBT)-based conversation. This assistant helps users explore their emotions, manage stress, and engage in self-reflection using AI-powered interactions.

## 🧠 About the Project

The Virtual Therapy Assistant is a mental health chatbot built with a focus on enhancing emotional well-being. It provides interactive, point-wise responses to users based on cognitive behavioral therapy principles. This project is ideal for users seeking a gentle guide through feelings of anxiety, stress, or self-doubt.

## 🚀 Features

- 🧘 Real-time AI-based therapy support via chat  
- 🎯 Point-wise, easy-to-understand responses  
- 💬 Send messages by pressing **Enter** or clicking Send  
- 🌐 Responsive and clean UI using **Tailwind CSS**  
- 🔐 Environment-based configuration using `.env`  
- 🔄 Error handling and fallback messages (e.g., API quota errors)  
- ✅ Fully tested for usability and smooth user experience  

## 🧩 Tech Stack

### Frontend:
- HTML5
- Tailwind CSS
- JavaScript

### Backend:
- Python (Flask)
- Flask-CORS
- Google Gemini 1.5 Pro API (via `google.generativeai`)
- `dotenv` for secure API key management

---

## 👥 Team Responsibilities

### 👤 Person 1: Frontend & UI/UX
- Designed an intuitive and minimal user interface using Tailwind CSS
- Integrated input handling (e.g., **message send on Enter key**)  
- Managed visual components and responsiveness across devices

### 👤 Person 2: Backend & API Integration
- Built Flask backend to handle chat interactions  
- Integrated the Gemini API to generate context-aware responses  
- Secured API access with `.env` configuration  
- Handled JSON communication between frontend and backend

### 👤 Person 3: Debugging, Error Handling, and Testing
- Solved critical errors like:
  - API rate limiting (HTTP 429)
  - CORS issues
  - Invalid/missing `.env` configurations
- Improved bot response structure (point-wise format)
- Handled edge cases and fallback messaging
- Conducted final testing and live demo walkthrough

---

## 🧪 How to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/virtual-therapy-assistant.git
   cd virtual-therapy-assistant
