import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from PIL import Image

# --- 1. SET PAGE CONFIG ---
st.set_page_config(page_title="Prenatal Pro", layout="wide")

# --- 2. HIGH-VISIBILITY DARK TEXT CSS ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #FFFFFF; }

    /* FORCE DARK TEXT FOR VISIBILITY */
    /* Targets all standard text, paragraphs, and list items */
    html, body, [class*="css"], .stText, p, li, span {
        color: #1A1A1A !important; 
        font-weight: 500 !important;
    }

    /* Headings - Dark Burgundy for visibility */
    h1, h2, h3 { 
        color: #700B33 !important; 
        font-weight: 800 !important; 
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] { 
        background-color: #FCE4EC !important; 
        border-right: 2px solid #F8BBD0;
    }

    /* Widget Labels (Inputs) - Bold Black */
    .stWidgetLabel p {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }

    /* Rounded Cards with Borders */
    div.stBlock {
        background-color: #FFF9FA;
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #F8BBD0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* Buttons */
    .stButton>button {
        border-radius: 25px;
        background-color: #D81B60;
        color: white !important;
        font-weight: bold;
        border: none;
        padding: 10px 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🌸 Prenatal Pro")
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Growth Tracker", "Ultrasound AI", "Notes & Calendar"],
        icons=["house", "graph-up", "camera", "calendar-heart"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#FCE4EC"},
            "nav-link": {"font-size": "16px", "text-align": "left", "color": "#700B33", "font-weight": "600"},
            "nav-link-selected": {"background-color": "#D81B60", "color": "white"},
        }
    )

# --- 4. CALCULATOR LOGIC ---
def calculate_due_date(lmp):
    return lmp + timedelta(days=280)

# --- 5. PAGE CONTENT ---

if selected == "Dashboard":
    st.header("Welcome back, Mama! ✨")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.subheader("Your Pregnancy Timeline")
        lmp_date = st.date_input("Select Last Menstrual Period (LMP)", datetime.now() - timedelta(weeks=10))
        due_date = calculate_due_date(lmp_date)
        
        # Calculations
        today = datetime.now().date()
        total_days = (today - lmp_date).days
        weeks = total_days // 7
        days = total_days % 7
        
        st.info(f"**Current Status:** {weeks} Weeks, {days} Days")
        st.success(f"**Estimated Due Date:** {due_date.strftime('%B %d, %Y')}")

    with col2:
        st.subheader("Progress Visualization")
        # Progress Pie Chart
        days_gone = max(0, min(total_days, 280))
        days_left = 280 - days_gone
        
        df_pie = pd.DataFrame({
            "Stage": ["Completed", "Remaining"],
            "Days": [days_gone, days_left]
        })
        fig = px.pie(df_pie, values='Days', names='Stage', 
                     color_discrete_sequence=['#D81B60', '#F8BBD0'], hole=0.6)
        fig.update_layout(showlegend=True, margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)

elif selected == "Growth Tracker":
    st.header("📈 Growth Analysis")
    
    # Placeholder Data
    weeks_list = list(range(4, 41))
    baby_weights = [0.5, 1, 2, 4, 7, 13, 23, 35, 45, 70, 100, 140, 190, 240, 300, 
                    360, 430, 500, 600, 660, 800, 1000, 1100, 1300, 1500, 1700, 
                    1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300, 3500, 3600, 3700]
    
    st.subheader("Baby's Estimated Weight Growth (Grams)")
    df_growth = pd.DataFrame({"Week": weeks_list, "Weight (g)": baby_weights})
    
    fig_growth = px.area(df_growth, x="Week", y="Weight (g)", 
                         color_discrete_sequence=['#D81B60'])
    st.plotly_chart(fig_growth, use_container_width=True)

elif selected == "Ultrasound AI":
    st.header("🔬 Ultrasound Analysis System")
    st.write("Upload your scan for a simulated analysis of fetal development.")
    
    uploaded_file = st.file_uploader("Choose an ultrasound image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Scan', use_container_width=True)
        
        if st.button("Analyze Scan"):
            with st.spinner("Analyzing structures..."):
                # Simulation of AI result
                st.success("Analysis Complete!")
                st.markdown("""
                - **Fetal Position:** Cephalic (Normal)
                - **Detection:** Heartbeat detected
                - **Estimated Gestational Age:** Matches timeline
                """)
                st.warning("⚠️ Disclaimer: This is an AI simulation. Please consult your OB-GYN.")

elif selected == "Notes & Calendar":
    st.header("📅 Appointments & Daily Notes")
    
    date_choice = st.date_input("Select Date")
    note_input = st.text_area("Write down symptoms, appointments, or notes for your doctor:")
    
    if st.button("Save to Log"):
        st.balloons()
        st.success(f"Entry saved for {date_choice}!")
