import streamlit as st
from streamlit.components.v1 import html
import base64
from PIL import Image
import time
import json

# ====== 🎚️ CONSTANTS ======
BACKGROUND_COLOR = "#0a0a0a"
PRIMARY_COLOR = "#ffffff"
SECONDARY_COLOR = "#7a7a7a"
ACCENT_COLOR = "#ff4d4d"
FONT_FAMILY = "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"

# ====== 🔁 Background Encoding Function ======
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ====== 🖌️ STYLE INJECTION ======
def inject_style(bg_img):
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    :root {{
        --bg-color: {BACKGROUND_COLOR};
        --primary-color: {PRIMARY_COLOR};
        --secondary-color: {SECONDARY_COLOR};
        --accent-color: {ACCENT_COLOR};
        --font-family: {FONT_FAMILY};
    }}

    .stApp {{
        background: url('data:image/png;base64,{bg_img}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: var(--font-family);
        color: var(--primary-color);
        line-height: 1.6;
    }}

    html {{ scroll-behavior: smooth; }}

    h1, h2, h3, h4, h5, h6 {{
        font-weight: 600;
        letter-spacing: -0.03em;
        margin-bottom: 1.5rem;
    }}

    h1 {{
        font-size: 3.5rem;
        line-height: 1.1;
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .profile-container {{
        position: relative;
        width: 220px;
        height: 220px;
        margin: 0 auto 2rem;
        border-radius: 50%;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }}

    .profile-img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 1px;
        filter: grayscale(30%);
        transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 0 0 0 1px rgba(255,255,255,0.1);
    }}

    .profile-container:hover .profile-img {{ transform: scale(1.05); }}

    .glass-panel {{
        background: rgba(15, 15, 15, 0.5);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        opacity: 0;
        animation: fadeIn 0.6s forwards;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    .glass-panel:hover {{
        border-color: rgba(255, 77, 77, 0.6);
        box-shadow: 0 0 40px rgba(255, 77, 77, 0.75);
    }}

    .skill-container {{ margin-bottom: 1.5rem; }}

    .skill-info {{
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.5rem;
    }}

    .skill-meter {{
        height: 4px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 2px;
        overflow: hidden;
    }}

    .skill-progress {{
        height: 100%;
        background: linear-gradient(90deg, var(--accent-color), #ff7b7b);
        border-radius: 2px;
        transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .interactive-text {{
        position: relative;
        display: inline-block;
        cursor: pointer;
        transition: color 0.3s ease;
    }}

    .interactive-text:hover {{ color: var(--accent-color); }}

    .interactive-text::after {{
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 0;
        height: 1px;
        background: var(--accent-color);
        transition: width 0.4s ease;
    }}

    .interactive-text:hover::after {{ width: 100%; }}

    .project-card {{
        position: relative;
        overflow: hidden;
        border-radius: 12px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .project-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(0, 255, 255, 0.25), transparent);
        opacity: 0;
        transition: opacity 0.4s ease;
    }}

    .project-card:hover::before {{ opacity: 1; }}

    .project-tag {{
        display: inline-block;
        padding: 0.25rem 0.75rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        font-size: 0.7rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        transition: all 0.3s ease;
    }}

    .project-tag:hover {{
        background: var(--accent-color);
        color: var(--bg-color);
    }}

    .nav-dots {{
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 2rem 0;
    }}

    .nav-dot {{
        width: 10px;
        height: 10px;
        background: var(--secondary-color);
        border-radius: 50%;
        cursor: pointer;
        transition: all 0.3s ease;
    }}

    .nav-dot.active {{
        background: var(--accent-color);
        transform: scale(1.3);
    }}

    @media (max-width: 768px) {{
        h1 {{ font-size: 2.5rem; }}
        .glass-panel {{ padding: 1.5rem; }}
    }}
    </style>
    """, unsafe_allow_html=True)
    

# ====== 🖼️ COMPONENTS ======
def profile_component():
    with open("Haris.jpeg", "rb") as img_file:
        img_data = base64.b64encode(img_file.read()).decode()

    st.markdown(f"""
    <div style="text-align: center;">
        <div class="profile-container">
            <img src="data:image/png;base64,{img_data}" class="profile-img">
        </div>
        <h1>HARIS FAROOQ</h1>
        <p style="color: {SECONDARY_COLOR}; letter-spacing: 2px; font-size: 1rem; margin-top: -1.5rem;">UI/UX AND AI ENTHUSIAST</p>
        <br>
    </div>
    """, unsafe_allow_html=True)

def skill_component(name, level):
    st.markdown(f"""
    <div class="skill-container">
        <div class="skill-info">
            <span>{name}</span>
            <span style="color: {SECONDARY_COLOR};">{level}%</span>
        </div>
        <div class="skill-meter">
            <div class="skill-progress" style="width: {level}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def project_card(title, description, tags, link="#", active=False):
    tag_html = "".join([f'<span class="project-tag">{tag}</span>' for tag in tags])

    st.markdown(f"""
    <div class="glass-panel project-card" style="animation-delay: {0.1 if active else 0.2}s;">
        <h3 style="margin-bottom: 1rem;">{title}</h3>
        <p style="color: {SECONDARY_COLOR}; line-height: 1.6; margin-bottom: 1.5rem;">{description}</p>
        <div style="margin-bottom: 1.5rem;">{tag_html}</div>
        <div>
            <a href="{link}" target="_blank" style="text-decoration: none;">
                <span class="interactive-text" style="display: inline-flex; align-items: center; gap: 0.5rem;">
                    VIEW PROJECT 
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </span>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ====== 🖼️ MAIN APP ======
def main():
    st.set_page_config(
        page_title="Haris Farooq | AI enthusiast",
        page_icon="✦",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    bg_img = get_base64("space2.png")
    inject_style(bg_img)

    profile_component()

    st.markdown("""
    <div class="glass-panel" style="animation-delay: 0.1s;">
        <h2>ABOUT</h2>
        <p style="color: #7a7a7a; line-height: 1.8; margin-bottom: 1.5rem;">
             I craft intelligent systems that merge technical precision with real-world impact.
            With hands-on experience in AI, automation, and design, I build tools that solve problems and scale.
            From Streamlit dashboards to C++ simulations, I blend logic with creativity.
            My mission: to drive AI innovation across Pakistan’s emerging industries.
        </p>
        <div style="display: flex; gap: 1.5rem;">
            <span class="interactive-text" style="display: inline-flex; align-items: center; gap: 0.3rem;">
                📍 Based in Karachi
            </span>
            <span class="interactive-text" style="display: inline-flex; align-items: center; gap: 0.3rem;">
                🎓 Studying at GIKI
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<div class="glass-panel" style="animation-delay: 0.2s;"><h2>CORE STRENGTHS</h2>""", unsafe_allow_html=True)
    skill_component("Graphic Designing", 95)
    skill_component("UI/UX Design", 92)
    skill_component("Data visualization", 88)
    skill_component("Streamlit", 90)
    skill_component("Prompt Engineering", 95)
    skill_component("Object Oriented Programming", 80)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin: 3rem 0;">
        <h2>SELECTED RECENT WORK</h2>
        <p style="color: #7a7a7a; max-width: 600px; margin: 0 auto;">A curated selection of recent projects...</p>
    </div>
    """, unsafe_allow_html=True)

    project_card(
        "Spendr - Personal Finance Tracker",
        "Spendr is a sleek and interactive personal finance app built using Streamlit. It helps users track expenses, visualize spending trends with dynamic graphs, and manage budgets — all in a minimalist, responsive UI.",
        ["Streamlit", "Python", "Plotly", "Data Visualization", "UX Design"],
        link="https://github.com/HarisFarooq23/Spendr"
    )

    project_card(
        "StockVerse - Investment Portfolio Tracker",
        "StockVerse is a powerful stock portfolio app built with Streamlit, allowing users to explore famous investor portfolios, analyze stock trends with real-time data, and visualize sector-wise distributions through interactive charts.",
        ["Streamlit", "Python", "yfinance", "Plotly", "Investment Analysis"],
        link="https://github.com/HarisFarooq23/StockVerse"
    )

    project_card(
        "Canva Design Portfolio",
        "A curated collection of digital designs created using Canva, ranging from social media posts and event banners to society documentation and personal branding visuals — each crafted with a keen eye for layout, color, and typography.",
        ["Canva", "Graphic Design", "Branding", "Social Media"],
        
    )
    
    active_project = st.session_state.get('active_project', 0)
    
    st.markdown("""
    <div class="nav-dots">
        <div class="nav-dot %s" onclick="setProject(0)"></div>
        <div class="nav-dot %s" onclick="setProject(1)"></div>
        <div class="nav-dot %s" onclick="setProject(2)"></div>
    </div>
    """ % (
        "active" if active_project == 0 else "",
        "active" if active_project == 1 else "",
        "active" if active_project == 2 else ""
    ), unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-panel" style="text-align: center; animation-delay: 0.3s;">
        <h2>GET IN TOUCH</h2>
        <p style="color: #7a7a7a; margin-bottom: 2rem;">Interested in collaborating or just want to say hello?</p>
        <div style="display: flex; justify-content: center; gap: 1.5rem;">
            <a href="https://github.com/HarisFarooq23" style="text-decoration: none;">
                <span class="interactive-text">GITHUB</span>
            </a>
            <a href="https://www.linkedin.com/in/harisfarooq23/" target="_blank" style="text-decoration: none;">
                <span class="interactive-text">LINKEDIN</span>
            </a>
            <a href="mailto:harisnetbackup@gmail.com" target="_blank" style="text-decoration: none;">
                <span class="interactive-text">EMAIL</span>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align: center; margin: 4rem 0 2rem; color: {SECONDARY_COLOR};">
        <p style="font-size: 0.8rem; letter-spacing: 1px;">
            © {time.strftime("%Y")} HARIS FAROOQ — DEVELOPED THROUGH ITERATIVE PROMPT ENGINEERING WITH ♥
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() comvert whole this code for vercel , with minimal changes and similar effects , use a different background , instad use some other bqackground , not a static image preferabby . and add interactive elements as much as you can to this website . 
