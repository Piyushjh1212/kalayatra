# KalaYatra 

**KalaYatra** is a Streamlit-based web application designed to showcase India's traditional art forms, rich cultural experiences, and promote responsible tourism. It offers users an engaging way to explore India's heritage through a modern digital platform.

##  Features

-  **Secure Login System** – Only authenticated users can access the main content.
-  **Home Page** – Highlights major Indian arts, dance forms, and eco-tourism.
-  **Art Forms Section** – Showcases traditional arts like Madhubani, Warli, and Tanjore with images and descriptions.
-  **Cultural Experiences** – Provides insights into Indian festivals, folk music, cuisine, and handicrafts.
-  **Contact Form** – Users can get in touch via a simple form.
-  **Responsive UI** – Clean and user-friendly interface using Streamlit's components and custom HTML/CSS.

##  Technologies Used

| Technology     | Description                            |
|----------------|----------------------------------------|
| Python         | Core programming language              |
| Streamlit      | Frontend framework for web UI          |
| HTML & CSS     | Custom styles via `st.markdown()`      |


##  Project Structure

KalaYatra/
│
├── app.py # Main Streamlit application
├── requirements.txt # List of Python dependencies
└── README.md # Project documentation (this file)

| **File/Folder**    | **Description**                                    |
| ------------------ | -------------------------------------------------- |
| `app.py`           | Main Streamlit application entry point             |
| `requirements.txt` | List of Python dependencies needed for the project |
| `README.md`        | Project documentation (overview, usage, etc.)      |


## Architecture Diagram

| **Layer**                | **Component**                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User Interface**       | **User Browser** (Desktop / Mobile View)                                                                                                                      |
| **Frontend (Streamlit)** | - Header & Navigation  <br> - Home Page <br> - Art Forms Page <br> - Responsible Tourism Page <br> - Kathak Page <br> - Contact Page (Form) <br> - Login Page |
| **Session Management**   | - Tracks current page  <br> - Login button state                                                                                                              |
| **Backend Resources**    | - `art_forms.json` (JSON data file) <br> - `kathak_info.py` (Python module) <br> - *Future:* User DB / Auth API                                               |
| **Optional (Future)**    | Cloud Deployment <br> (Streamlit Community / Sharing, AWS, GCP, etc.)                                                                                         |


##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/KalaYatra.git
cd KalaYatra
