import streamlit as st

# ----------- CONFIGURATION ----------- 
st.set_page_config(page_title="KalaYatra", layout="wide")

# ----------- CUSTOM CSS ----------- 
st.markdown("""
    <style>
    /* Background and fonts */
    *{ 
    margin: 0;
    padding:0;
    box-sizing: border-box;
  }
    body {
        font-family: 'Segoe UI', sans-serif;
    }

    .title {
        font-size: 3.2em;
        text-align: center;
        color: #4B0082;
        font-weight: bold;
        margin-top: 1rem;
    }

    .subtitle {
        font-size: 1.5em;
        text-align: center;
        color: #6A5ACD;
        margin-bottom: 2rem;
    }

    .section {
        background-color: #f5f5f5;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }

    .card:hover {
        transform: scale(1.02);
        transition: all 0.3s ease-in-out;
        box-shadow: 0 6px 18px rgba(0,0,0,0.2);
    }

    footer {
        text-align: center;
        color: #aaa;
        margin-top: 3rem;
        font-size: 0.9em;
    }
    </style>
""", unsafe_allow_html=True)

# ----------- SIDEBAR ----------- 
st.sidebar.image("https://images.unsplash.com/photo-1581091012184-7e0cdfbb6797?auto=format&fit=crop&w=400&q=60", use_container_width=True)
st.sidebar.markdown("<h2 style='color:#4B0082;'>KalaYatra</h2>", unsafe_allow_html=True)

# Login section in the sidebar
login_option = st.sidebar.radio("Navigation", ["🏠 Home", "🎨 Art Forms", "🎉 Experiences", "🌿 Tourism", "📬 Contact", "🔑 Login"])

# ----------- LOGIN PAGE ----------- 
if login_option == "🔑 Login":
    st.markdown("<div class='title'>Login</div>", unsafe_allow_html=True)
    
    # Login form
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            if username == "user" and password == "password123":  # Change these to your desired credentials
                st.success("Logged in successfully!")
                st.session_state.logged_in = True  # Track user session
                st.session_state.username = username
            else:
                st.error("Incorrect username or password.")

# ----------- HOME PAGE ----------- 
if login_option == "🏠 Home":
    if not getattr(st.session_state, 'logged_in', False):  # Check if user is logged in
        st.warning("Please log in to view the content.")
    else:
        st.image("https://images.unsplash.com/photo-1567581935884-3349723552f5?auto=format&fit=crop&w=1600&q=80", use_container_width=True)
        st.markdown("<div class='title'>KalaYatra</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle'>A Journey Through Indian Traditions, Culture, and Responsible Tourism</div>", unsafe_allow_html=True)
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<div class='section card'>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/7/75/Madhubani_art.jpg", caption="🎨 Madhubani Art", use_container_width=True)
            st.markdown("**Origin:** Bihar  \n**Style:** Folk painting with natural dyes")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='section card'>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/f/f4/Kathakali_Performer.JPG", caption="🕺 Kathakali Dance", use_container_width=True)
            st.markdown("**Origin:** Kerala  \n**Style:** Classical dance-drama")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col3:
            st.markdown("<div class='section card'>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/4/4c/Ecotourism_Tamenglong.jpg", caption="🌿 Responsible Travel", use_container_width=True)
            st.markdown("**Support Local** artisans & traditions with eco-friendly practices.")
            st.markdown("</div>", unsafe_allow_html=True)

# ----------- ART FORMS ----------- 
elif login_option == "🎨 Art Forms":
    if not getattr(st.session_state, 'logged_in', False):
        st.warning("Please log in to view the content.")
    else:
        st.markdown("<div class='title'>Traditional Indian Art Forms</div>", unsafe_allow_html=True)
        arts = {
            "Madhubani": {
                "img": "https://upload.wikimedia.org/wikipedia/commons/7/75/Madhubani_art.jpg",
                "origin": "Bihar",
                "style": "Folk painting with natural dyes"
            },
            "Warli": {
                "img": "https://upload.wikimedia.org/wikipedia/commons/6/63/Warli_painting.jpg",
                "origin": "Maharashtra",
                "style": "Tribal art using geometric patterns"
            },
            "Tanjore": {
                "img": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Tanjore_Painting_Lord_Vishnu.jpg",
                "origin": "Tamil Nadu",
                "style": "Gold-foiled classical religious painting"
            }
        }

        search = st.text_input("Search art form").lower()
        for art, info in arts.items():
            if search in art.lower() or not search:
                st.markdown("<div class='section card'>", unsafe_allow_html=True)
                st.image(info["img"], caption=art, use_container_width=True)
                st.markdown(f"**Origin:** {info['origin']}  \n**Style:** {info['style']}")
                st.markdown("</div>", unsafe_allow_html=True)

# ----------- EXPERIENCES ----------- 
elif login_option == "🎉 Experiences":
    if not getattr(st.session_state, 'logged_in', True):
        st.warning("Please log in to view the content.")
    else:
        st.markdown("<div class='title'>Cultural Experiences Across India</div>", unsafe_allow_html=True)
        choice = st.selectbox("Choose Category", ["Festivals", "Folk Music", "Traditional Foods", "Handicrafts"])

        if choice == "Festivals":
            st.image("https://cdn.zeebiz.com/sites/default/files/2024/03/25/285353-happy-holi-2024-wishes-images.jpg", caption="Holi – Festival of Colors", use_container_width=True)
            st.write("Holi celebrates color, joy, and victory of good over evil.")

        elif choice == "Folk Music":
            st.image("https://upload.wikimedia.org/wikipedia/commons/6/6e/Baul_performance_Bangladesh.jpg", caption="Baul Singing", use_container_width=True)
            st.write("Baul singers are mystical minstrels from Bengal, reflecting a blend of Bhakti and Sufi traditions.")

        elif choice == "Traditional Foods":
            st.image("https://upload.wikimedia.org/wikipedia/commons/6/6a/Rajasthani_Thali_in_Jaipur.jpg", caption="Rajasthani Thali", use_container_width=True)
            st.write("A royal plate of dal baati churma, gatte ki sabzi, and more.")

        elif choice == "Handicrafts":
            st.image("https://upload.wikimedia.org/wikipedia/commons/d/d6/Jaipur_Blue_Pottery.jpg", caption="Jaipur Blue Pottery", use_container_width=True)
            st.write("Made from Egyptian paste and known for its eye-catching blue glaze.")

# ----------- CONTACT PAGE ----------- 
elif login_option == "📬 Contact":
    if not getattr(st.session_state, 'logged_in', False):
        st.warning("Please log in to view the content.")
    else:
        st.markdown("<div class='title'>Contact Us</div>", unsafe_allow_html=True)
        with st.form("contact"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Message")
            if st.form_submit_button("Submit"):
                st.success("Thanks for contacting us! We'll get in touch soon.")

# ----------- FOOTER ----------- 
st.markdown("<footer>🌸 Made with ❤️ by Piyush Jhariya | KalaYatra © 2025</footer>", unsafe_allow_html=True)
