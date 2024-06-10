import base64
import streamlit as st
from streamlit_option_menu import option_menu
import CPATP, Chatbot, Pembelajaran, Latihan
from st_social_media_links import SocialMediaIcons
from streamlit.components.v1 import html as st_html



st.set_page_config(
    page_title='💧 Fluida Statis'
)


@st.cache_data  # 👈 Add the caching decorator
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.snow()

img = get_img_as_base64('leaf.png')
main = get_img_as_base64('daun.png')

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url('data:image/png;base64,{main}');
background-size: 100%;
background-position: center;
background-repeat: repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-size: 100%;
background-position: left; 
background-repeat: repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

class MultiApp:

    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })
    

    def run():
        # app = st.sidebar(
        with st.sidebar:
            st.image('Logo.png')
            st.info('**Yo students! Start here ↓**', icon='👋🏾')
            with st.expander("💡**How to use**", expanded=True):
                st.info(
                    """
                        1. Bacalah "Capaian Pembelajaran" terlebih dahulu.
                        2. Setelah selesai klik "Pilihan Pembelajaran" yang sesuai dengan gaya belajarmu
                        3. Silahkan klik latihan soal jika kalian sudah selesai mempelajari fluida statis 
                        4. Jika kalian butuh bantuan mengenai materi fluida statis, silahkan klik menu "Chatbot".
                        """
                )
       
            app = option_menu(
                menu_title='Fluida Statis',
                options=['Capaian Pembelajaran','Pilihan Pembelajaran','Latihan Soal' ,'Chatbot'],
                icons=['playstation','journal-bookmark-fill','journal','robot'],
                menu_icon='water',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
                "icon": {"color": "white", "font-size": "23px"}, 
                "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},}    
                )

            st.audio('lofi.m4a', loop=True)
            
            # Coba-Coba

            st.html(
                """
                <div style="text-align:center; font-size:14px; color:lightgrey">
                    <hr style="margin-bottom: 6%; margin-top: 0%;">
                    Share the ❤️ on social media
                </div>"""
            )

            social_media_links = [
                'https://www.instagram.com/shel_vyo/',
                'https://www.linkedin.com/in/shelvy-okvia-466621138/',
                'https://www.youtube.com/@shelvyokvia9294/videos',
                'https://medium.com/@shelvy5113'
            ]

            social_media_icons = SocialMediaIcons(
                social_media_links, colors=["lightgray"] * len(social_media_links)
            )

            social_media_icons.render(sidebar=True)

            st.html(
                """
                <div style="text-align:center; font-size:12px; color:lightgrey">
                    <hr style="margin-bottom: 6%; margin-top: 6%;">
                    <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
                        <img alt="Creative Commons License" style="border-width:0"
                            src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />
                    </a><br>
                    You can modify and build upon this work non-commercially. All derivatives should be
                    credited to <b>Shelvy Okvia<b> and
                    be licenced under the same terms.
                </div>
            """
            )

        if app == "Capaian Pembelajaran":
            CPATP.app()
        if app == "Chatbot":
            Chatbot.app()    
        if app == "Pilihan Pembelajaran":
            Pembelajaran.app()
        if app == "Latihan Soal":
            Latihan.app()         
          
          
             
    run()    
            


            