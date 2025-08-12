from streamlit_option_menu import option_menu
import streamlit as st

st.set_page_config(layout="wide", page_title="Dashboard Prediksi Garis Pantai Kabupaten Brebes")

# Inject CSS supaya menu full height & ada footer
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: white;
        border: none;
        box-shadow: none;
    }
    [data-testid="stSidebar"] .sidebar-content{
        display: flex;
        flex-direction: column;
        height: 100%
        justify-content: space-between;
    }
            
    [data-testid="stSidebar"] .sidebar-content > *:not(:last-child) {
        margin-bottom: 20px;
    }

    .sidebar-content {
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    .sidebar-footer {
        margin-top: auto;
        padding: 50px;
        font-size: 12px;
        color: #0056b3;
        text-align: center;
        margin-top: auto;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)

    selected = option_menu(
        "Prediksi Spasial Temporal",
        ["Informasi Umum", 
         "Informasi Garis Pantai", 
         "Analisis Perubahan Garis Pantai", 
         "Prediksi Garis Pantai", 
         "Evaluasi Hasil Prediksi"],
        icons=['info-circle', 'map', 'graph-up', 'water', 'check-circle'],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
                "padding": "5px", 
                "background-color": "#ffffff",
            },
            "icon": {
                "color": "#0056b3",  
                "font-size": "18px"
            },
            "nav-link": {
                "font-size": "16px", 
                "text-align": "left", 
                "margin": "0px",
                "--hover-color": "#e6f0ff",
                "color": "#0056b3",
                "font-weight": "bold"
            },
            "nav-link-selected": {
                "background-color": "#0056b3",
                "color": "white"
            }
        }
    )

    st.markdown('<div class="sidebar-footer">© 2025 Dashboard Prediksi Garis Pantai</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)




# GANTI IF menu == ... MENJADI:
if selected == "Informasi Umum":
    st.title("Informasi Umum")
    st.markdown("""
        Dashboard ini dikembangkan untuk menampilkan hasil deteksi dan prediksi perubahan garis pantai...
    """)
elif selected == "Informasi Garis Pantai":
    st.title("🧾 Informasi Garis Pantai")
elif selected == "Analisis Perubahan Garis Pantai":
    st.title("📈 Analisis Perubahan Garis Pantai")
elif selected == "Prediksi Garis Pantai":
    st.title("🌊 Garis Pantai di Kabupaten Brebes")
elif selected == "Evaluasi Hasil Prediksi":
    st.title("🔄 Perbandingan Perubahan Garis Pantai")

