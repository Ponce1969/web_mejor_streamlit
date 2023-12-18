
# 1. importar librerias
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import base64
from PIL import Image
from email.message import EmailMessage
from seguro import EMAIL_PASSWORD
import smtplib
from save_consulta import save_consulta, create_database
from streamlit_card import card



#navbar
st.set_page_config(page_title="Cerrajeria",page_icon="🔐", layout= "wide" , initial_sidebar_state="collapsed") 


# Crear base de datos al inicio del script.
create_database()



# crear lottie animacion, debe ser json para que funcione.
url = "https://lottie.host/14042b4d-9ba3-4d98-bede-16b814a8dfaf/dRlZjcwAEy.json"
imagen_video = Image.open("imagenes/cabina.jpeg")

def load_lottie (url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie=load_lottie(url)

# crear intro.
with st.container():
    st.header(" ***Hola Bienvenido a la Web de :green[Cerrajeria]*** 🇺🇾   ")
    st.subheader("Brindando Seguridad y Experiencia en Agraciada 3901")  
    st.markdown(''' 
        :red[Apasionado de la Cerrajeria,]:orange[ Siempre con la Solucion ]
        :green[ mas conveniente,]:blue[ a nuestros clientes].''')
    
    
# sobre nosotros.
with st.container():
    st.write("---")
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre nosotros 🔎 ")
        st.write(
            """
            Nuestro objetivo es mostrar nuestros trabajos de cerrajeria,
            para acercar a los clientes a solucionar sus problemas de cerraduras
            mas comunes, cerraduras que se atascan por mala lubricacion o ninguna,
            por esa razon hay muchos videos de youtube explicando los problemas
            y sus soluciones, pondremos nuestras redes sociales y correo para que ,
            puedas estar en contacto con nosotros , nos puede enviar fotos de su consulta
            por Whatsapp y le responderemos con una solucion a su problema.
            """
        )
    with animation_column:
        st_lottie(lottie, height = 300)
 
        
#Servicios .
with st.container():
    st.write("---")
    st.header("Mi lugar , Tu lugar :rainbow[🗝️] !!!")
    image_column, separacion, text_column = st.columns([2,0.5,5])
    with image_column:
        st.image(imagen_video)
    with text_column: 
        st.write(
            """
            ***Mi lugar de trabajo Agraciada 3901 , esquina Angel Salvo 
            mas de 30 años, com mucho amor a la cerrajeria
            hacemos magia ,muchas veces con las copias de llaves rotas 
            o torcidas que nos llegan a diario, si tienen 
            una llave que nadie quiere copiar acerquese a la cabina,
            seguro se podra copiar, por el mismo precio que una llave entera.
            Te espero en el Paso Molino, debajo del viaducto.***
            """
        )
        
 #Galeria de trabajos.
with st.container():
    st.write("---")
    st.header("Galería de Trabajos 🛠️ ")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        img1 = Image.open("imagenes/puertafiat.jpeg")
        img1_resized = img1.resize((300, 300))  
        st.image(img1_resized, caption="Puerta fiat uno")

    with col2:
        img2 = Image.open("imagenes/puertaluminio.jpeg")
        img2_resized = img2.resize((300, 300))  
        st.image(img2_resized, caption="Cerradura europerfil")

    with col3:
        img3 = Image.open("imagenes/puerta.jpg")
        img3_resized = img3.resize((300, 300))  
        st.image(img3_resized, caption="Cerradura soprano brasilera")

    col4, col5, col6 = st.columns(3)

    with col4:
        img4 = Image.open("imagenes/puertamadera.jpeg")
        img4_resized = img4.resize((300, 300))  
        st.image(img4_resized, caption="Así empezó el trabajo")

    with col5:
        img5 = Image.open("imagenes/junior.jpeg")
        img5_resized = img5.resize((300, 300))  
        st.image(img5_resized, caption="Así quedó")

    with col6:
        img6 = Image.open("imagenes/s10.jpeg")
        img6_resized = img6.resize((300, 300))  
        st.image(img6_resized, caption="Otro ángulo de la misma puerta")


with st.container():
    st.write("---")
    st.header("Fábricas Nacionales de Cerraduras")
    
    st.markdown("""
    <div style="background-color:lightblue; padding:10px; border-radius:5px;">
        <p style="color:black; font-size:16px;">
            Entrando en la web de las fabricas, podremos observar todos los modelos, 
            eligiendo el que mas se adapte, a nuestra puerta , por cualquier consulta 
            dejaremos nuestro whatsapp, para cualquier inquietud o ayuda que requieran.
        </p>
    </div>
    """, unsafe_allow_html=True)   
    
    
     # Agregando espacio.
    st.markdown("<br>", unsafe_allow_html=True)  # Puedes ajustar el número de "<br>" para más espacio

    col1, col_space, col2 = st.columns([1,0.1,1])  # define a narrow middle column for space

    with col1:
        with open("imagenes/logo_star.jpeg", "rb") as f:
            data= f.read()
            encoded= base64.b64encode(data)

        data= "data:image/jpg;base64," + encoded.decode("utf-8")
        st.markdown(f"[![Logo star ]({data})](https://www.star.com.uy/)")
        

    with col2:
        with open("imagenes/logo_elisil.jpeg", "rb") as f:
            data= f.read()
            encoded= base64.b64encode(data)

        data= "data:image/jpg;base64," + encoded.decode("utf-8")
        st.markdown(f"[![Logo elisil ]({data})](https://elisil.com.uy/)")
        
# mandar y recibir correo .
def send_notification_email(receiver_email, subject, content):
    # Configuración del correo
    email = EmailMessage()
    email.set_content(content)
    email["Subject"] = subject
    email["From"] = "gompatri@gmail.com"
    email["To"] = receiver_email
    
    # Usar SMTP para enviar el correo
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        try:
            smtp.starttls()
            smtp.login("gompatri@gmail.com",EMAIL_PASSWORD)
            smtp.send_message(email)
        except Exception as err:
            print(f"aca hay un problema? {err=}")
            
            
# Estilos CSS
st.markdown("""
<style>
    .reportview-container .main .block-container {
        max-width: 1200px;
    }
    .stTextInput>div>div>input {
        background-color:#273346;
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid grey;
    }
    .stTextArea textarea {
        background-color:#273346;   
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid grey;
    }
    .stButton>button {
        font-size: 16px;
        padding: 0.6em 2em;
        color: white;
        border: none;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)




# formulario contacto
with st.container():
    st.write("---")


    # Dividiendo la sección en dos: una para el formulario y otra para las imágenes.
    form_col,  espacio_colum ,img_col = st.columns([3, 1 ,3])

    with form_col.form("contact_form"):
        st.title("CONTACTO")
        st.subheader("Déjenos su consulta y a la brevedad le responderemos. Muchas gracias.")
        # Dividiendo el formulario en dos columnas
        col1, col2 = st.columns(2)

        with col1:
            nombre_input = st.text_input("NOMBRE")
            email_input = st.text_input("EMAIL")

        with col2:
            asunto_input = st.text_input("ASUNTO")
        
        # Mensaje en toda la anchura
        mensaje_input = st.text_area("MENSAJE")
    
        submitted = st.form_submit_button("ENVIAR")

        if submitted:
            try:
                save_consulta(nombre_input, email_input, asunto_input, mensaje_input)
                send_notification_email("gompatri@gmail.com", "Nueva consulta recibida", f"Nombre:{nombre_input}\nAsunto: {asunto_input}\nMensaje: {mensaje_input}\nCorreo: {email_input}")
                st.success("Gracias por tu consulta!")
            except:
                st.error("Hubo un problema al guardar tu consulta. Por favor, inténtalo de nuevo más tarde.")
                
    with img_col:
        st.header("Cilindros Europerfil gama alta")
        
        # Agregando una fila de imagenes.
        img_row1_col1, img_row1_col2 = st.columns(2)
        
        with img_row1_col1:
            img1 = Image.open("/home/gonzapython/Documentos/vscode_codigo/web_mejor_streamlit/imagenes/cilindro-antibumping-ifam.jpg")
            st.image(img1, caption="Cilindro Antibumping ifan" , width=200)#width=200 para achicar la imagen.
            
        with img_row1_col2:
            img2 = Image.open("imagenes/abus_euro.jpeg")
            st.image(img2, caption="Cilindro  Europerfil abus" , width=200)
            
        # Agregando segunda fila de imagenes.
        img_row2_col1, img_row2_col2 = st.columns(2)
        
        with img_row2_col1:
            img3 = Image.open("imagenes/cilindro_tesa.jpeg")
            st.image(img3, caption="Cilindro Europerfil tesa" , width=200)
            
        with img_row2_col2:
            img4 = Image.open("imagenes/cilindro_lince.jpeg")
            st.image(img4, caption="Cilindro Europerfil lince" , width=200)
            
            
# redes sociales, logo de whatsapp.

with st.container():
    st.write("---")
    left_column, right_column = st.columns([1, 5])
    number = "598099171819" 

    with open("imagenes/WhatsApp.png", "rb") as f:
        data= f.read()
        encoded= base64.b64encode(data)

    data= "data:image/png;base64," + encoded.decode("utf-8")

    # Definiendo el tamaño de la imagen a 50px x 50px
    img_style = "width:50px; height:50px;"
    with left_column:    
        st.markdown(f'<a href="https://wa.me/{number}"><img src="{data}" style="{img_style}"></a>', unsafe_allow_html=True)


# Función que se ejecutará al hacer clic en la tarjeta
def on_card_click():
    st.write("¡Hola enviame un whatsapp o un correo!")

with open("imagenes/ganzua_significado.jpg", "rb") as f:
    data= f.read()
    encoded= base64.b64encode(data)

data= "data:image/jpg;base64," + encoded.decode("utf-8")

with right_column:
    card(
        title="Cerrajeria Gonzalo Ponce",
        text="Llámenos al celular 099171819 y obtenga un presupuesto gratuito",
        image= data,
        on_click=on_card_click,  # <- Aquí se está pasando el callback
        styles={
            "card":{
                "margin":"0 auto"
            }
        }
    )
                     
            