import streamlit as st
import json

# Load data from JSON
def load_art_data():
    with open('Data/art_forms.json', 'r') as f:
        return json.load(f)

def local_css():
    st.markdown("""
    <style>
        .main, .block-container {
            padding: 30px !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        
        Body{
            background: white;
        }
        * {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
    </style>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown("""
    <style>
        .header {
            position: sticky;
            top: 3rem; /* offset for Streamlit's toolbar */
            width: 100%;
            background: black;
            color: white;
            padding: 12px 30px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 9999;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        }
        .header .logo {
            font-size: 1.8rem;
            font-weight: bold;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            cursor: pointer;
        }
        
        .header nav{
            background: Black;
            display: flex;
            align-items: center;
        }
        .header nav a {
            color: white;
            background: transparent;
            margin-left: 24px;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s ease;
            padding: 10px 16px;
            border-radius: 6px;
        }
        .header nav a:hover {
            color: red;
        }
        
        .contact_page {
            background: blue;
        }
        
        .Login_button{
            background-color: #fff;
            color: black;
            padding: 12px 25px;
            font-size: 16px;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            margin-left: 20px;
        }
        
        .Login_button:hover{
            background: #222;
            color:#fff;
        }
    </style>

    <div class="header">
        <div class="logo">KalaYatra</div>
        <nav>
            <a href="#home">Home</a>
            <a href="#art-forms">Art Forms</a>
            <a href="#responsible-tourism">Responsible Tourism</a>
            <a href="#kathak">About</a>   
        </nav>
        <nav>
            <a class="Login_button">Contact</a>
        </nav>
    </div>
    """, unsafe_allow_html=True)
    
    


def render_Home_page():
    st.title("Welcome to KalaYatra")
    st.subheader("Discover Traditional Art Forms & Cultural Experiences Across India 🇮🇳")

    st.write("""
    Welcome to **KalaYatra**, your cultural companion to explore India's rich and diverse heritage.Experience vibrant festivals, traditional dances, ancient art forms, and learn how you can support responsible tourism.
    """)

    # Use columns for side-by-side image + text layout
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Pushkar_Fair_2016.jpg/320px-Pushkar_Fair_2016.jpg",
                 caption="Pushkar Camel Fair", use_container_width=True)

    with col2:
        st.markdown("""
        ### Pushkar Camel Fair  
        One of the world's largest camel fairs held annually in Rajasthan.It’s a vibrant festival of colors, folk performances and traditional crafts. A perfect blend of culture and commerce attracting tourists worldwide.
        """)

    st.write("---")

    col3, col4 = st.columns([1, 2])

    with col3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Kumbh_mela_sangam_prayagraj_india_2013-03-10_0187.JPG/320px-Kumbh_mela_sangam_prayagraj_india_2013-03-10_0187.JPG",
                 caption="Kumbh Mela", use_container_width=True)

    with col4:
        st.markdown("""
        ### Kumbh Mela  
        The world's largest religious gathering, held every 12 years at four river-bank pilgrimage sites.Millions gather to take a holy dip and participate in spiritual rituals.It’s a grand display of India's spiritual heritage and unity.
        """)

    st.write("---")

    st.markdown("""
    ## Why Responsible Tourism Matters?  
   Supporting local communities and preserving cultural traditions are essential for ensuring that the rich and diverse heritage of a region continues to thrive for future generations. When we protect these traditions, we not only honor the history and identity of the people but also maintain the unique cultural fabric that defines each community. Responsible tourism encourages visitors to be mindful of their impact, fostering respect for local customs, environments, and ways of life. As a traveler, you have the power to make a positive difference by choosing sustainable practices that support local artisans, businesses, and conservation efforts. This thoughtful approach to tourism helps create meaningful experiences that benefit both visitors and hosts, promoting a deeper understanding and appreciation of cultural heritage while safeguarding it for the long term.
    """)

    st.info("Explore, Experience, and Empower — Join KalaYatra on this vibrant journey through India's cultural heartlands!")






def render_Festival_page():
    st.markdown("""
        <style>
        div[data-baseweb="select"] {
            background-color: #e6ffe6;
            border-radius: 10px;
            padding: 5px;
            width: 400px;
        }

        .selected-festival {
            background-color: #fff;
            border-left: 5px solid #4CAF50;
            padding: 12px;
            border-radius: 8px;
            font-size: 20px;
            margin-top: 20px;
            color: #2e7d32;
        }

        .festival-container {
            display: flex;
            gap: 20px;
            margin-top: 30px;
        }

        .festival-container img {
            width: 300px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }

        .festival-text {
            font-size: 18px;
            color: #333;
            line-height: 1.7;
        }

        div[data-baseweb="select"] * {
            background: #fff;
            font-weight: bold;
            cursor:pointer;
            outline: none;
        }
        </style>

        <h1 style='text-align: center; color: Black;'>India's Festivals</h1>
        <p style='text-align: center;'>Explore the beauty and heritage of India</p>
        <hr>
    """, unsafe_allow_html=True)

    festivals = [
        "Diwali", "Holi", "Eid-ul-Fitr", "Eid-ul-Adha", "Navratri", "Durga Puja",
        "Ganesh Chaturthi", "Pongal", "Bihu", "Onam", "Christmas", "Good Friday",
        "Easter", "Raksha Bandhan", "Makar Sankranti", "Lohri", "Mahashivratri",
        "Janmashtami", "Guru Nanak Jayanti", "Ram Navami", "Baisakhi", "Mahavir Jayanti",
        "Buddha Purnima", "Chhath Puja", "Hanuman Jayanti", "Gudi Padwa", "Ugadi",
        "Vishu", "Karwa Chauth", "Dussehra (Vijayadashami)", "Thaipusam"
    ]

    selected_festival = st.selectbox("Choose a Festival to explore:", festivals)

    st.markdown(f"<div class='selected-festival'>You selected: <b>{selected_festival}</b></div>", unsafe_allow_html=True)

    # Description and image mapping
 
        
    descriptions = {
     
    "Diwali": {
        "desc": "<b>Diwali</b>, also known as <i>Deepavali</i>, is one of the most popular and grand festivals celebrated in India. It is a five-day festival of lights that symbolizes the victory of light over darkness and good over evil. On this occasion, people decorate their homes with oil lamps (diyas), candles, and colorful lights. Goddess Lakshmi, the deity of wealth and prosperity, is worshipped to seek blessings for a prosperous life. Families exchange sweets, wear new clothes, and light fireworks to celebrate the joy of the festival. Diwali is not only a religious celebration but also a time for togetherness, bonding, and spreading happiness among loved ones.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdMLaIq_nPXsT-4K9j6xf8LQ6u9NSRn7RAsA&s"
    },
    "Holi": {
        "desc": "**Holi** is a vibrant Hindu festival celebrated in India and other parts of the world. Known as the <b>Festival of Colors</b> or<b> Festival of Love</b>, it marks the arrival of spring and the victory of good over evil. People celebrate by throwing colored powders, dancing, singing, and enjoying festive foods. Holi promotes unity, joy, and the spirit of forgiveness.",
        "image": "https://i.pinimg.com/736x/42/cb/98/42cb9834e2a65ef3ee6d77abaf133371.jpg"
    },
    "Eid-ul-Fitr": {
        "desc": "Eid-ul-Fitr is an important Islamic festival celebrated at the end of Ramadan, the holy month of fasting. It is a day of joy, gratitude, and community. Muslims offer a special prayer called Eid Salah, give charity known as Zakat al-Fitr, and enjoy festive meals with family and friends. Eid-ul-Fitr symbolizes spiritual renewal, forgiveness, and unity.",
        "image": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiapuZYc3qviy3M-Y4mOntENo5l3V02PG35VI5sfZmrm9xb_4aVL7Gc8c7_Mt6thgh7ms02WnUxmL_yYt778mJNcaEY4fzu2MYcFjz4JQbelaLKAWamWg08x8k2S9wEktmogfLeEu47re3W/s320/Eid+ul+fitr+history.jpg"
    },
    "Eid-ul-Adha": {
        "desc": "Eid-ul-Adha commemorates the willingness of Prophet Ibrahim to sacrifice his son in obedience to God. It's marked by prayers, feasting, and animal sacrifice.",
        "image": "https://static.toiimg.com/photo/72837938.cms"
    },
    "Navratri": {
        "desc": "Navratri is a nine-night Hindu festival celebrating the divine feminine. Devotees fast, pray, and perform Garba and Dandiya dances.",
        "image": "https://www.holidify.com/images/cmsuploads/compressed/1061436_20190802141826.jpg"
    },
    "Durga Puja": {
        "desc": "**Durga Puja** is a major Hindu festival, especially celebrated in **West Bengal**, honoring **Goddess Durga’s victory over the demon Mahishasura**. It symbolizes the triumph of good over evil. The festival lasts several days and includes grand **pandals (decorated stages)**, traditional **music and dance**, rituals, and cultural performances. Families come together to worship, share festive meals, and celebrate with devotion and joy.",
        "image": "https://www.tripsavvy.com/thmb/73qb9wRKQmqEfnafjSdFCeDS5Wk=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/GettyImages-521065881-57f496745f9b586c35be0df9.jpg"
    },
    "Ganesh Chaturthi": {
        "desc": "Ganesh Chaturthi celebrates the birth of Lord Ganesha. Devotees install Ganesha idols in homes and public places and immerse them in water after 10 days.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Ganesh_Chaturthi_in_Mumbai.jpg"
    },
    "Pongal": {
        "desc": "Pongal is a harvest festival celebrated in Tamil Nadu. It’s marked by cooking the traditional dish 'Pongal', thanking the Sun God, and enjoying rural traditions.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/67/Pongal_dish.jpg"
    },
    "Bihu": {
        "desc": "Bihu is a set of Assamese festivals that celebrate the harvest, new year, and seasonal change. It includes folk dances, music, and traditional feasts.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Bihu_dancers.jpg"
    },
    "Onam": {
        "desc": "**Onam** is a major harvest festival celebrated in **Kerala**, India, to honor the homecoming of the legendary King **Mahabali**. It reflects **prosperity, unity, and cultural heritage**. The festival features **floral rangoli (Pookalam)**, traditional dances like **Thiruvathira**, **boat races**, and a grand feast called **Onam Sadhya**. Onam is a 10-day celebration filled with joy, devotion, and rich traditions.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Onam_Sadya.jpg"
    },
    "Christmas": {
        "desc": "**Christmas** is a Christian festival celebrated on **December 25th** to mark the **birth of Jesus Christ**. It is a joyful time filled with **decorations, gift-giving, carols**, and **family gatherings**. People decorate Christmas trees, attend church services, and share festive meals. The holiday symbolizes **love, peace, and goodwill** among all.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/32/Christmas_Decorations.jpg"
    },
    "Good Friday": {
        "desc": "Good Friday commemorates the crucifixion of Jesus Christ. Christians observe the day with fasting, prayer, and church services.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Good_Friday.jpg"
    },
    "Easter": {
        "desc": "Easter celebrates the resurrection of Jesus Christ. It’s observed with joy, Easter eggs, church services, and family gatherings.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/13/Easter_eggs_-_yellow_basket.jpg"
    },
    "Raksha Bandhan": {
        "desc": "Raksha Bandhan celebrates the bond between brothers and sisters. Sisters tie a rakhi (thread) on their brothers’ wrists, who in turn vow to protect them.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/db/Rakhi_on_Raksha_Bandhan.jpg"
    },
    "Makar Sankranti": {
        "desc": "Makar Sankranti marks the Sun's transition into Capricorn. Celebrated with kite flying, sesame sweets, and prayers for prosperity.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Makar_Sankranti.jpg"
    },
    "Lohri": {
        "desc": "Lohri is a Punjabi festival celebrating the winter harvest. People gather around bonfires, sing folk songs, and enjoy traditional sweets.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Lohri_festival.jpg"
    },
    "Mahashivratri": {
        "desc": "Mahashivratri is dedicated to Lord Shiva. Devotees fast and offer prayers all night, chanting mantras and visiting Shiva temples.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/36/Mahashivaratri.jpg"
    },
    "Janmashtami": {
        "desc": "Janmashtami marks the birth of Lord Krishna. Celebrated with devotional singing, fasting, and reenactments of Krishna’s life.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/33/Janmashtami_Celebration.jpg"
    },
    "Guru Nanak Jayanti": {
        "desc": "Guru Nanak Jayanti commemorates the birth of Guru Nanak Dev Ji, the founder of Sikhism. Sikhs celebrate with prayers, processions, and langar.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/15/Guru_Nanak_Jayanti_celebration.jpg"
    },
    "Ram Navami": {
        "desc": "Ram Navami celebrates the birth of Lord Rama. Devotees visit temples, read the Ramayana, and perform bhajans.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Ram_Navami.jpg"
    },
    # sjklsfkls
    "Baisakhi": {
        "desc": "Baisakhi, also spelled Vaisakhi, is a vibrant and joyous harvest festival celebrated mainly in Punjab and northern India, marking the beginning of the Punjabi New Year and the harvest of the Rabi crops. Observed on April 13 or 14, Baisakhi holds immense significance for Sikhs, as it commemorates the formation of the Khalsa Panth in 1699 by Guru Gobind Singh Ji, symbolizing courage, equality, and brotherhood. The day is celebrated with great enthusiasm through processions (Nagar Kirtans), folk dances like Bhangra and Gidda, and visits to Gurudwaras, where special prayers and community meals (langars) are organized. Baisakhi is not just a cultural celebration but also a spiritual reminder of unity, gratitude, and the values of hard work and faith.",
        "image": "https://th.bing.com/th/id/OIP.w7ld3d0bwwOuybP_3nwIhwHaE8?rs=1&pid=ImgDetMain"
    },
    "Mahavir Jayanti": {
        "desc": "Mahavir Jayanti is one of the most important religious festivals in Jainism, celebrating the birth of Lord Mahavir, the 24th and last Tirthankara (spiritual teacher) of Jainism. It is observed on the 13th day of the bright half of the Hindu month Chaitra (March–April). Lord Mahavir was born in 599 BCE in Kundalpur, Bihar, and dedicated his life to promoting non-violence (ahimsa), truth (satya), non-possessiveness (aparigraha), celibacy (brahmacharya), and non-stealing (asteya). On this day, devotees visit Jain temples, offer prayers, meditate, and engage in charitable activities. Processions with idol chariots (rath yatras), devotional songs, and discourses on Mahavir’s teachings are also organized. Mahavir Jayanti serves as a reminder to follow the path of righteousness, compassion, and spiritual discipline.",
        "image": "https://th.bing.com/th/id/OIP.rPvPBGeAFpxK2JlsgrTVagHaGk?rs=1&pid=ImgDetMain"
    },
    "Buddha Purnima": {
        "desc": "Buddha Purnima, also known as Vesak, is the most sacred day for Buddhists as it marks the birth, enlightenment (nirvana), and death (parinirvana) of Lord Gautama Buddha. Celebrated on the full moon day in the Hindu month of Vaisakha (April–May), this day holds deep spiritual significance and promotes the values of peace, compassion, and self-realization. Devotees visit Buddhist temples, offer prayers, meditate, and engage in charitable acts. The teachings of the Buddha—centered around the Four Noble Truths and the Eightfold Path—are remembered and reflected upon. Buddha Purnima is not only a celebration of a divine life but also a reminder to walk the path of truth, non-violence, and inner peace.",
        "image": "https://www.panasiabiz.com/wp-content/uploads/2023/05/Buddha-Purnima-2023-Wishes-Greetings-WhatsApp-status-to-shares.jpg"
    },
    "Chhath Puja": {
        "desc": "Chhath Puja is a sacred Hindu festival dedicated to the worship of the Sun God (Surya) and his consort Usha, celebrated with immense devotion and discipline, especially in Bihar, Jharkhand, eastern Uttar Pradesh, and Nepal. Observed six days after Diwali, the festival spans four days of rituals that include holy bathing, fasting, offering prayers at sunrise and sunset, and presenting traditional prasad like thekua, fruits, and sugarcane. Devotees express gratitude for life, health, and prosperity by offering arghya (water offerings) to the setting and rising sun, symbolizing balance and harmony in nature. Chhath Puja is not just a religious observance, but a spiritual celebration of purity, humility, and the eternal bond between human life and the cosmic forces.",
        "image": "https://th.bing.com/th/id/OIP.oWZlaJH8LgYiwt0AhqZgNQHaEU?rs=1&pid=ImgDetMain"
    },
    "Hanuman Jayanti": {
        "desc": "Hanuman Jayanti is a Hindu festival that celebrates the birth of Lord Hanuman, the devoted disciple of Lord Rama and a symbol of strength, devotion, and courage. It usually falls in March or April, during the full moon of the Chaitra month. Devotees visit temples, offer prayers, chant Hanuman Chalisa, and read the Ramayana to honor his loyalty and bravery. Many observe fasting and perform rituals seeking protection and blessings. Hanuman Jayanti inspires people to be fearless, humble, and devoted. It is a day of spiritual energy, reminding devotees of the power of faith and the importance of selfless service.",
        "image": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEil6XOC9TJFqgSgZrjwilhTIA_igv7EDMYnV3mdhJlnIqkSEPK01OT8VrdjfYam-e4ZDo9DchVMrQukhXieQLBYC35o8VNDjl3suUEj7ADHIG8vvC5aXxurFDDhFieIECrDn7M_6wQrFPq-pw189Fhv7yfcxJLK0l9AzxcB5FuGYco8kTDv_eJSc7Mg1Tw/w1200-h630-p-k-no-nu/Hanuman%20Jayanti%20Celebration.jpeg"
    },
    "Gudi Padwa": {
        "desc": "Gudi Padwa is the traditional New Year festival celebrated in Maharashtra and parts of Goa, usually in March or April. It marks the beginning of the Hindu lunisolar calendar and the arrival of spring. The highlight of the festival is the Gudi—a decorated pole with a bright cloth, neem leaves, garland, and an inverted copper pot—hoisted outside homes as a symbol of victory and prosperity. People clean their houses, make rangoli, wear new clothes, and prepare festive dishes like puran poli. Gudi Padwa signifies new beginnings, success, and happiness, and is celebrated with great joy, devotion, and cultural pride.",
        "image": "https://th.bing.com/th/id/OIP.HUd2Sfi4UI4cPooBt3rTrAHaE7?rs=1&pid=ImgDetMain"
    },
    "Ugadi": {
        "desc": "Ugadi is the New Year festival celebrated in the Indian states of Andhra Pradesh, Telangana, Karnataka, and parts of Maharashtra. It usually falls in March or April, marking the beginning of the Hindu lunisolar calendar. The word Ugadi comes from Yuga (age) and Adi (beginning), meaning the start of a new age. People clean their homes, decorate with mango leaves and rangoli, wear new clothes, and prepare a special dish called Ugadi Pachadi, which combines six tastes symbolizing different emotions of life. Ugadi is a time for reflection, renewal, and celebration, welcoming prosperity and happiness in the year ahead.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/A_Happy_Ugadi_puja_tray_Telugu_Hindu_New_Year_Vaisakhi.jpg/500px-A_Happy_Ugadi_puja_tray_Telugu_Hindu_New_Year_Vaisakhi.jpg"
    },
    "Vishu": {
        "desc": "Vishu is a traditional festival celebrated in Kerala and parts of Tamil Nadu, marking the beginning of the Malayalam New Year. It usually falls in mid-April and is dedicated to Lord Vishnu, especially his Krishna avatar. The most important ritual is the Vishukkani—an arrangement of auspicious items like rice, fruits, flowers, and a mirror, seen first thing in the morning for good luck. People wear new clothes (Vishu Kodi), burst firecrackers, and exchange gifts (Vishu Kaineettam). Traditional feasts are also prepared. Vishu symbolizes hope, prosperity, and new beginnings, and is celebrated with joy, devotion, and family togetherness.",
        "image": "https://th.bing.com/th?id=OIF.%2fp5KLYsBcovsP%2bChTL8G7A&rs=1&pid=ImgDetMain"
    },
    "Karwa Chauth": {
        "desc": "Dussehra, also known as Vijayadashami, is a major Hindu festival celebrated across India with great enthusiasm. It marks the victory of Lord Rama over the demon king Ravana, symbolizing the triumph of good over evil. In some regions, it also celebrates Goddess Durga’s victory over Mahishasura. People celebrate by burning effigies of Ravana, performing Ram Leela (a dramatic retelling of Rama’s story), and organizing fairs and processions. Dussehra falls on the tenth day of the Navratri festival and reminds people to follow truth, righteousness, and courage. It brings communities together in joy, devotion, and festive spirit.",
        "image": "https://th.bing.com/th/id/OIP.UElj-p6NMlPjNAsEtAop5AHaHa?rs=1&pid=ImgDetMain"
    },
    "Dussehra (Vijayadashami)": {
        "desc": "Dussehra, also known as Vijayadashami, is a major Hindu festival celebrated across India with great enthusiasm. It marks the victory of Lord Rama over the demon king Ravana, symbolizing the triumph of good over evil. In some regions, it also celebrates Goddess Durga’s victory over Mahishasura. People celebrate by burning effigies of Ravana, performing Ram Leela (a dramatic retelling of Rama’s story), and organizing fairs and processions. Dussehra falls on the tenth day of the Navratri festival and reminds people to follow truth, righteousness, and courage. It brings communities together in joy, devotion, and festive spirit.",
        "image": "https://static2.tripoto.com/media/filter/tst/img/OgData/1476125471_dussehra_festival.jpg"
    },
    "Thaipusam": {
        "desc": " Thaipusam is a Hindu festival celebrated mainly by the Tamil community in honor of Lord Murugan, the god of war. It falls in the Tamil month of Thai (January–February) and marks the day when Goddess Parvati gave Murugan a divine spear to defeat evil. Devotees show their faith through acts of penance like carrying *kavadi* (decorated structures) and piercing their bodies with hooks or skewers. The most famous celebration takes place at Batu Caves in Malaysia. Thaipusam is a powerful display of devotion, endurance, and spiritual purification, bringing communities together in deep religious and cultural unity.",
        "image": "https://www.holidify.com/images/cmsuploads/compressed/maxresdefault_20201007160832.jpg"
    }
}

    if selected_festival in descriptions:
      info = descriptions[selected_festival]
      st.markdown(f"""
          <style> 
              .festival-container {{
                  display: flex;
                  align-items: center;
                  gap: 20px;
                  margin-top: 30px;
                  padding: 20px;
                  border-radius: 10px;
              }}

              .festival-container img {{
                  width: 300px;
                  height: auto;
                  border-radius: 8px;
                  object-fit: cover;
              }}

              .festival-text {{
                  font-size: 18px;
                  color: #2e7d32;
                  line-height: 1.6;
                  flex: 1;
                  margin-left: 30px;
              }}
          </style>

          <div class="festival-container">
              <img src="{info['image']}" alt="{selected_festival}">
              <div class="festival-text">{info['desc']}</div>
          </div>
      """, unsafe_allow_html=True)
    else:
      st.markdown("<p style='margin-top:20px; color: gray;'>Information coming soon for this festival.</p>", unsafe_allow_html=True)


def render_Tourism_Page():
    st.markdown("""
        <style>
        /* Style the dropdown */
        div[data-baseweb="select"] {
            background-color: #e6ffe6;
            border-radius: 10px;
            padding: 5px;
            width: 400px;
        }

        /* Style for the selected destination */
        .selected-destination {
            background-color: #fff;
            border-left: 5px solid #4CAF50;
            padding: 12px;
            border-radius: 8px;
            font-size: 20px;
            margin-top: 20px;
            color: #2e7d32;
        }

        div[data-baseweb="select"] * {
            background: #fff;
            font-weight: bold;
            cursor:pointer;
            outline: none;
        }
        </style>

        <h1 style='text-align: center; color: Black ;'>Tourism Places</h1>
        <p style='text-align: center;'>Explore the beauty and heritage of India</p>
        <hr>
    """, unsafe_allow_html=True)

    destinations = [
        "Taj Mahal, Agra",
        "Jaipur's Palaces, Rajasthan",
        "Backwaters of Kerala",
        "Beaches of Goa",
        "Himalayan Treks"
    ]

    selected_place = st.selectbox("Choose a destination to explore:", destinations)

    # Show styled selected place
    st.markdown(f"<div class='selected-destination'> {selected_place}</div>", unsafe_allow_html=True)

    # Show description
    if selected_place == "Taj Mahal, Agra":
      st.markdown("""
            <style>
                 .custom-container {
                display: flex;
                align-items: flex-start;
                gap: 20px;
                margin-top: 40px;
            }
            .custom-container img {
                max-width: 300px;
                border-radius: 10px;
            }
            .custom-text {
                font-size: 18px;
                line-height: 1.6;
                color: #2e7d32;
                font-weight: 500;
                margin-left: 30px
            }
            </style>
            <div class="custom-container">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Taj-Mahal.jpg/640px-Taj-Mahal.jpg">
                <div class="custom-text">
                    <p>The <b> Taj Mahal </b>, located in Agra, Uttar Pradesh, is one of the most iconic tourist attractions in India and a UNESCO World Heritage Site.
                    Built by the Mughal Emperor Shah Jahan in memory of his beloved wife Mumtaz Mahal, this white marble monument is renowned for its stunning architecture and emotional legacy.
                    The Taj Mahal reflects a perfect blend of Persian, Islamic, and Indian styles, with intricate carvings and beautifully landscaped Mughal gardens. It attracts millions of tourists 
                    every year from around the world, making it a major part of India’s tourism industry. Visitors are especially drawn to its breathtaking views during sunrise and under the full moon. 
                    Easily accessible from major cities like Delhi and Jaipur, it remains a symbol of love and a must-visit destination for both domestic and international travelers.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    elif selected_place == "Jaipur's Palaces, Rajasthan":
       st.markdown("""
            <style>
                 .custom-container {
                display: flex;
                align-items: flex-start;
                gap: 20px;
                margin-top: 40px;
            }
            .custom-container img {
                max-width: 300px;
                border-radius: 10px;
            }
            .custom-text {
                font-size: 18px;
                line-height: 1.6;
                color: #2e7d32;
                font-weight: 500;
                margin-left: 30px
            }
            </style>
            <div class="custom-container">
                <img src="https://www.tourmyindia.com/images/city-palace-jaipur.jpg">
                <div class="custom-text">
                    <p>Jaipur, the capital of Rajasthan, is renowned for its majestic palaces that reflect the grandeur of Rajput and Mughal architecture. The **City Palace** is a stunning complex with courtyards, gardens, and museums. Nearby, the **Hawa Mahal** or “Palace of Winds” features 953 small windows designed for royal women to watch the streets unseen. The **Jal Mahal**, set in the middle of Man Sagar Lake, appears to float on water, offering a magical view. These palaces together capture the royal history and architectural brilliance of Jaipur.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    elif selected_place == "Backwaters of Kerala":
         st.markdown("""
            <style>
                 .custom-container {
                display: flex;
                align-items: flex-start;
                gap: 20px;
                margin-top: 40px;
            }
            .custom-container img {
                max-width: 300px;
                border-radius: 10px;
            }
            .custom-text {
                font-size: 18px;
                line-height: 1.6;
                color: #2e7d32;
                font-weight: 500;
                margin-left: 30px
            }
            </style>
            <div class="custom-container">
                <img src="https://static.toiimg.com/thumb/msid-91888972,width-748,height-499,resizemode=4,imgsize-243110/.jpg">
                <div class="custom-text">
                    <p>The backwaters of Kerala are a unique and tranquil network of lakes, lagoons, rivers, and canals running parallel to the Arabian Sea coast.
                    Stretching across towns like Alleppey (Alappuzha), Kumarakom, and Kollam, these serene waterways are lined with lush coconut trees, quaint villages, and paddy fields. A popular way to explore them is on a traditional houseboat (kettuvallam), offering a peaceful escape into nature. 
                    The backwaters are not just scenic but also play a vital role in Kerala’s rural life, culture, and ecosystem.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    elif selected_place == "Beaches of Goa":
         st.markdown("""
            <style>
                 .custom-container {
                display: flex;
                align-items: flex-start;
                gap: 20px;
                margin-top: 40px;
            }
            .custom-container img {
                max-width: 300px;
                border-radius: 10px;
            }
            .custom-text {
                font-size: 18px;
                line-height: 1.6;
                color: #2e7d32;
                font-weight: 500;
                margin-left: 30px
            }
            </style>
            <div class="custom-container">
                <img src="https://www.oyorooms.com/travel-guide/wp-content/uploads/2021/08/BlogImage-16Aug_SouthGoa_Image-12-1.jpg">
                <div class="custom-text">
                    <p>The <b>beaches of Goa</b> are among the most famous in India, drawing visitors with their golden sands, swaying palms, and vibrant atmosphere. In </b>North Goa</b>, beaches like <b>Baga</b>, <b>Calangute</b>, and <b>Anjuna</b> are known for their energetic vibe, beach shacks, water sports, and lively nightlife. <b>Vagator</b> offers dramatic red cliffs and scenic views, while <b>Arambol</b> is popular among backpackers and artists for its bohemian charm. In contrast, <b>South Goa</b> is quieter and more peaceful, perfect for those seeking relaxation. Beaches like <i>Palolem</i>, <i>Agonda</i>, and <i>Colva</i> are known for their pristine beauty, calm waters, and tranquil surroundings. Many of these spots offer yoga retreats, cozy beach huts, and dolphin-watching tours. Whether you're looking for adventure or serenity, Goa’s beaches offer the perfect coastal escape.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    elif selected_place == "Himalayan Treks":
        st.markdown("""
            <style>
                 .custom-container {
                display: flex;
                align-items: flex-start;
                gap: 20px;
                margin-top: 40px;
            }
            .custom-container img {
                max-width: 300px;
                border-radius: 10px;
            }
            .custom-text {
                font-size: 18px;
                line-height: 1.6;
                color: #2e7d32;
                font-weight: 500;
                margin-left: 30px
            }
            </style>
            <div class="custom-container">
                <img src="https://trekthehimalayas.com/images/HomePageImages/Desktop/45f54547-59a1-41e4-89f7-44d2da93736e_Ali-Bedni-Bugyal%20(5).jpg">
                <div class="custom-text">
                    <p>The <b> Himalayan treks </b> offer some of the most breathtaking and adventurous experiences in India. From the lush green trails of <b>Valley of Flowers</b> in Uttarakhand to the rugged paths of the <b>Markha Valley</b> in Ladakh and the scenic <b>Kashmir Great Lakes</b>, these treks showcase snow-capped peaks, alpine meadows, and serene lakes. Suitable for both beginners and experienced trekkers, each route reveals the natural and cultural richness of the Himalayas, making it a paradise for adventure seekers.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)


def render_rituals_fair():
    st.markdown("""
        <style>
        .page-title {
            text-align: center; 
            color: black; 
        }
        .page-subtitle {
            text-align: center;
            margin-top: 5px;
            color: #2e7d32;
        }
        hr {
            margin: 20px 0;
            border: 1px solid #4CAF50;
        }
        .grid-container {
           display: grid;
           grid-template-columns: repeat(300px 300px);
           gap: 50px;
           padding: 10px 40px 40px 40px;
           justify-content: center; 
        }
        .card {
            border-radius: 15px;
            padding: 20px;
            transition: transform 0.2s ease-in-out;
        }

        .card img {
            
            width: 40%;
            border:2px solid transparent;
            max-height: 350px;
            object-fit: cover;
            margin-bottom: 15px;
        }
        
        .card-image{
            display:flex;
            content-align:center;
            justify-content:center;
        }
        .card-title {
            text-align:center;
            font-size: 22px;
            font-weight: 700;
            color: #2e7d32;
            margin-bottom: 10px;
        }
        .card-desc {
            font-size: 16px;
            line-height: 1.5;
            margin:50px;
            text-align:justify;
            color:black;
        }
        </style>

        <h1 class="page-title">Rituals and Fairs in India</h1>
        <p class="page-subtitle">Explore the beauty and heritage of India</p>
        <hr>

        <div class="grid-container">
    """, unsafe_allow_html=True)

    rituals = [
        {

            "title": "Pushkar Camel Fair",
            "desc": "The **Pushkar Camel Fair**, held in the holy town of Pushkar in Rajasthan, India, is one of the most vibrant and iconic cultural festivals in the country. Celebrated every year around the time of **Kartik Purnima** (usually in October or November), the fair attracts thousands of visitors, including pilgrims, local villagers, livestock traders, and international tourists. The fair is most famous for its large-scale trading of camels, horses, and cattle, where beautifully decorated animals are paraded, bought, and sold. Beyond the livestock trading, the Pushkar Camel Fair is a colorful showcase of Rajasthani culture, featuring folk music and dance performances, camel races, turban-tying competitions, moustache contests, and even a traditional bride and groom dress-up competition. The event also holds deep spiritual significance, as thousands of devotees take a holy dip in the sacred Pushkar Lake and offer prayers at the **Brahma Temple**, which is one of the very few temples dedicated to Lord Brahma in the world. The fair is a unique blend of spirituality, tradition, and festivity, offering a once-in-a-lifetime cultural experience that captures the true essence of rural Rajasthan.",
            "image": "https://as1.ftcdn.net/v2/jpg/10/02/14/22/1000_F_1002142218_3Zzof4JEVDeJaJhMAGoxtW2w7huc2gYP.jpg"
        },
        {
            "title": "Kumbh Mela",
            "desc": "The **Kumbh Mela** is one of the largest and most sacred religious gatherings in the world, deeply rooted in Hindu tradition and spirituality. Held every 12 years at four rotating pilgrimage sites—**Prayagraj (Allahabad), Haridwar, Ujjain**, and **Nashik**—this massive event draws millions of devotees, saints (sadhus), monks, and tourists from across India and around the globe. The central ritual of the Kumbh Mela is the **Shahi Snan** (royal bath), where devotees take a dip in the holy rivers—Ganga, Yamuna, Saraswati, Godavari, or Shipra—believing that the sacred waters will cleanse them of sins and grant salvation. The event is not only a religious experience but also a grand cultural spectacle featuring spiritual discourses, devotional singing, religious processions, and gatherings of various Akharas (religious sects). The origin of the Kumbh Mela is rooted in Hindu mythology, based on the story of the Samudra Manthan (churning of the ocean), during which drops of the divine nectar of immortality fell at these four locations. The Kumbh Mela symbolizes faith, unity, and devotion, offering a rare glimpse into India’s timeless spiritual traditions and the collective power of belief.",
            "image": "data:image/jpeg;base64,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"
        },
        {
            "title": "Lohri Festival",
            "desc": "Lohri is a vibrant and joyful Punjabi festival celebrated primarily in the northern regions of India, especially in Punjab, Haryana, Himachal Pradesh, and parts of Delhi. Observed every year on January 13th, Lohri marks the end of winter and the beginning of the harvest season, especially for the rabi crops like wheat. The festival holds great significance for farmers, but it is also celebrated with enthusiasm by families in general. At the heart of the celebration is a bonfire around which people gather in the evening. They offer sesame seeds (til), jaggery (gur), popcorn, and peanuts to the fire as a symbol of gratitude to nature and the Sun God. Traditional Punjabi songs are sung, and people perform the energetic bhangra and giddha dances. Lohri also marks a special occasion for families celebrating the birth of a child or a recent marriage. It is a time of community, joy, sharing, and the hope for a prosperous season ahead. The warmth of the bonfire and the spirit of togetherness make Lohri a cherished celebration of life and abundance.",
            "image": "data:image/jpeg;base64,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"
        },
        {
            "title": "Rath Yatra",
            "desc": "**Rath Yatra**, also known as the **Chariot Festival**, is one of the most famous and grand religious festivals in India, celebrated with great devotion and enthusiasm, especially in **Puri, Odisha**. The festival is dedicated to **Lord Jagannath**, an incarnation of Lord Vishnu, along with his siblings **Lord Balabhadra** and **Goddess Subhadra**. Every year, during the month of **Ashadha (June-July)**, the deities are taken out of the Jagannath Temple in a majestic procession and placed in beautifully decorated giant wooden chariots. These chariots are pulled by thousands of devotees through the streets of Puri to the Gundicha Temple, which is about 3 kilometers away. The pulling of the chariots is considered a sacred act, believed to grant salvation and blessings. The return journey, known as **Bahuda Yatra**, takes place after nine days. Rath Yatra symbolizes universal brotherhood, devotion, and the journey of life. It attracts millions of pilgrims and tourists from across the world, making it a spectacular spiritual and cultural event.",
            "image": "data:image/jpeg;base64,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"
        }
    ]

    # Render each ritual/fair as a card
    for ritual in rituals:
        st.markdown(f"""
           <div class="card">
           <div class="card-title">{ritual['title']}</div>
          <div class="card-image"><img src="{ritual['image']}" alt="{ritual['title']}"></div>
          
          <div class="card-desc">{ritual['desc']}</div>
          </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # Close grid-container div



def render_contact_page():
    # Inject some CSS
    st.markdown("""
        <style>
            /* Optional: make the form look nicer */
            .form-box {
                width: 100%;
                max-width: 500px;
                padding: 20px;
                box-shadow: 0 0 15px rgba(0,0,0,0.1);
                border-radius: 10px;
                background-color: #f9f9f9;
            }
            h1 {
                color: #2c3e50;
                text-align: center;
                margin-bottom: 20px;
            }

            /* Style form inputs */
            div[data-baseweb="input"] > input, 
            div[data-baseweb="textarea"] > textarea {
                border: 2px solid #3498db;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                transition: border-color 0.3s ease;
            }

            div[data-baseweb="input"] > input:focus, 
            div[data-baseweb="textarea"] > textarea:focus {
                border-color: #2980b9;
                outline: none;
            }

            /* Style the submit button */
            button[kind="primary"] {
                background-color: #000;
                color: white;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 5px;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }

            button[kind="primary"]:hover {
                background-color: #2980b9;
            }
            
       
        </style>
    """, unsafe_allow_html=True)

    st.markdown("# Contact Us")
    st.write("Feel free to reach out by filling the form below.")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Send")

        if submitted:
            if name and email and message:
                st.success("Thank you for contacting us! We'll get back to you soon.")
            else:
                st.error("Please fill in all the fields.")

def render_footer_page():
    st.markdown(
        """
        <style>
        .footer {
            position: sticky;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #111;  /* dark black */
            color: #eee;
            text-align: center;
            padding: 15px 10px;
            font-size: 14px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            box-shadow: 0 -2px 8px rgba(0, 0, 0, 0.5);
            z-index: 1000;
        }
        .footer a {
            color: #1e90ff;
            text-decoration: none;
            font-weight: 500;
            margin: 0 8px;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        </style>

        <div class="footer">
            © 2025 KalaYatra | Promoting Culture & Responsible Tourism
            <br>
            <small>Follow us on
                <a href="https://twitter.com" target="_blank">Twitter</a> |
                <a href="https://facebook.com" target="_blank">Facebook</a> |
                <a href="https://instagram.com" target="_blank">Instagram</a>
            </small>
        </div>
        """,
        unsafe_allow_html=True
    )


# To run in Streamlit, just call render_contact_page()

def main():
    st.set_page_config(layout="wide")
    local_css()
    render_header()
    render_Home_page()
    render_Festival_page()
    render_Tourism_Page()
    render_rituals_fair()
    render_contact_page()
    render_footer_page()

    # 👇 Add your section rendering functions here
    # render_home()
    # render_art_forms()
    # render_responsible_tourism()
    # render_kathak()
    # render_contact()
    # render_footer()

if __name__ == '__main__':
    main()
