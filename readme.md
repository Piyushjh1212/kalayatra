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

### 📁 Project Structure

| File / Folder         | Description                                |
|-----------------------|--------------------------------------------|
| `app.py`              | Main Streamlit application                 |
| `requirements.txt`    | List of Python dependencies                |
| `README.md`           | Project documentation (this file)         |


## Architecture Diagram


| **Component**                | **Role/Function**                                                            | **Technology Used**                        | **Data Flow / Interaction**                                           |
| ---------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------------- |
| **Frontend (Web UI)**        | User interface to explore art forms, contact, login, and educational content | **Streamlit (Python-based Web UI)**        | Renders pages dynamically, user fills forms, clicks links, views info |
| **Navigation Header**        | Sticky navigation bar for smooth page routing                                | Streamlit + HTML/CSS (inline in Streamlit) | Handles navigation clicks (e.g., Home, Art Forms, Contact, Login)     |
| **Art Forms Data Loader**    | Loads traditional Indian art information from JSON files                     | Python (`json` module)                     | Parses `art_forms.json` to display cultural content                   |
| **Dynamic Pages Renderer**   | Displays different sections like Kathak, Responsible Tourism, Contact, etc.  | Streamlit Functions                        | Based on menu click, the respective function is called                |
| **Contact Form Module**      | Allows users to submit their queries or feedback                             | Streamlit Forms                            | Accepts input fields and validates submission                         |
| **Login Placeholder**        | For future user login functionality                                          | Streamlit Button                           | Placeholder for auth logic (can be extended with Firebase/Auth API)   |
| **Local Styling (CSS)**      | Custom layout and design of the interface                                    | Injected via Streamlit `st.markdown()`     | Applies global font, spacing, colors, responsiveness                  |
| **Static Assets (optional)** | Images, icons, or videos related to art & culture                            | Streamlit File Support / CDN               | Loaded when needed in art or culture display                          |
| **Deployment Server**        | Hosts the web app                                                            | Streamlit Cloud / Heroku / Render          | Users access through browser                                          |


## Contact 

Created by Piyush Jhariya

[piyushjhariya65@gmail.com]

https://growallcoaching.in (update if available)

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/KalaYatra.git
cd KalaYatra



