# KalaYatra 🎨🌿

**KalaYatra** is a Streamlit-based web application designed to showcase India's traditional art forms, rich cultural experiences, and promote responsible tourism. It offers users an engaging way to explore India's heritage through a modern digital platform.

## 🚀 Features

- 🔐 **Secure Login System** – Only authenticated users can access the main content.
- 🏠 **Home Page** – Highlights major Indian arts, dance forms, and eco-tourism.
- 🎨 **Art Forms Section** – Showcases traditional arts like Madhubani, Warli, and Tanjore with images and descriptions.
- 🎉 **Cultural Experiences** – Provides insights into Indian festivals, folk music, cuisine, and handicrafts.
- 📬 **Contact Form** – Users can get in touch via a simple form.
- 🌐 **Responsive UI** – Clean and user-friendly interface using Streamlit's components and custom HTML/CSS.

## 🛠️ Technologies Used

| Technology     | Description                            |
|----------------|----------------------------------------|
| Python         | Core programming language              |
| Streamlit      | Frontend framework for web UI          |
| HTML & CSS     | Custom styles via `st.markdown()`      |


## 📂 Project Structure

KalaYatra/
│
├── app.py # Main Streamlit application
├── requirements.txt # List of Python dependencies
└── README.md # Project documentation (this file)


## Architecture Diagram

+-------------------------+
|      User Browser       |
| (Desktop / Mobile View) |
+-----------+-------------+
            |
            v
+----------------------------+
|      Streamlit Frontend   |
|  - Header & Navigation     |
|  - Home Page               |
|  - Art Forms Page          |
|  - Responsible Tourism     |
|  - Kathak Page             |
|  - Contact Page (Form)     |
|  - Login Page              |
+----------------------------+
            |
            v
+----------------------------+
|    Session State Manager  |
|  - Tracks current page     |
|  - Login button state      |
+----------------------------+
            |
            v
+-----------------------------+
|       Backend Resources     |
|  - JSON File: art_forms.json|
|  - kathak_info.py (details) |
|  - Future: User DB/Auth API |
+-----------------------------+

Optional (Future Enhancements):
+-----------------------------+
|   Cloud Deployment (e.g.,   |
|     Streamlit Community,   |
|     Streamlit Sharing,     |
|     or AWS/GCP)            |
+-----------------------------+

dd
## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/KalaYatra.git
cd KalaYatra
