from tkinter import *
from tkinter import ttk, filedialog, messagebox

import modelo_tar as tarik

from PIL import ImageTk, Image
import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

font1 = "Arial" 
gwi = 1280
ghe = 720

try:
    # Cargar el modelo
    modelPAU = tf.keras.models.load_model('modelo_deteccion_fuego_paula.h5')
    modelo_cargado = True
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    modelo_cargado = False

def process_image(image_path):
    """Preprocesa la imagen para el modelo"""
    try:
        img = Image.open(image_path)
        img = img.resize((224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception as e:
        print(f"Error en el procesamiento de la imagen: {e}")
        return None

def predict_fire(image_path, mod):
    """Realiza la predicción"""
    if not modelo_cargado:
        messagebox.showerror("Error", "El modelo no está cargado correctamente")
        return None

    processed_image = process_image(image_path)

    if processed_image is not None:
        try:

            if mod == "Modelo Tradicional":
                print(image_path)
                prediction = tarik.leer_img(image_path)
                print(prediction)
                return prediction
            elif mod == "Red Convolucional":
                prediction = modelPAU.predict(processed_image, verbose=0)
                return prediction[0][0]
            
        except Exception as e:
            print(f"Error en la predicción: {e}")
            return None
    return None

class FireDetectionGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("Detecta-Fuegos-100")
        self.root.resizable(False, False)
        self.current_frame = Frame(root, width=gwi, height=ghe, bg="#FFCC99")
        self.current_frame.place(anchor='center', relx=0.5, rely=0.5)
        self.loaded_image = None
        self.photo = None

    def create_default_image(self, width, height, text="No Image"):
        """Crea una imagen por defecto cuando no se encuentra el archivo"""
        img = Image.new('RGB', (width, height), color='#FFCC99')
        return ImageTk.PhotoImage(img)

    def select_image(self, mod):

        """Función para seleccionar una imagen"""
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")]
            )
            if file_path:
                # Mostrar imagen seleccionada
                image = Image.open(file_path)
                image = image.resize((400, 400))
                self.photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=self.photo)
                
                # Realizar predicción
                probability = predict_fire(file_path, mod)
                if probability is not None:
                    self.update_result(probability)
                else:
                    messagebox.showerror("Error", "No se pudo procesar la imagen")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar la imagen: {e}")

    def update_result(self, probability):
        """Actualiza el resultado de la predicción"""
        if (probability) > 0.5:
            result_text = f"No hay fuego\nProbabilidad: {probability:.2%}"
            self.result_label.config(text=result_text, fg="green")
        else:
            result_text = f"¡FUEGO DETECTADO!\nProbabilidad: {1-probability:.2%}"
            self.result_label.config(text=result_text, fg="red")

    def main_menu(self):
        """Menú principal"""
        self.current_frame.place_forget()
        self.current_frame = Frame(self.root, width=gwi, height=ghe, bg="#FFCC99")
        self.current_frame.place(anchor='center', relx=0.5, rely=0.5)

        # Título principal
        label_title = Label(self.current_frame, text="Detector de Fuego", 
                          font=(font1, 64), fg="red", bg="#FFCC99")
        label_title.place(x=300, y=70)

        # Crear imágenes por defecto
        default_image = self.create_default_image(350, 350)

        # Botones principales
        btn_modelo1 = Button(self.current_frame, text="Iniciar Detección", 
                           font=(font1, 16), command=lambda: self.modelo1())
        btn_modelo1.place(anchor='center', x=600, y=400)

    def modelo1(self):
        """Interfaz del modelo"""
        self.current_frame.place_forget()
        self.current_frame = Frame(self.root, width=gwi, height=ghe, bg="#FFCC99")
        self.current_frame.place(anchor='center', relx=0.5, rely=0.5)

        # Título
        title_label = Label(self.current_frame, text="Detector de Fuego", 
                          font=(font1, 48), fg="red", bg="#FFCC99")
        title_label.place(x=400, y=50)

        # Botón para volver al menú principal
        back_button = Button(self.current_frame, text="Volver al Menú", 
                           font=(font1, 12), command=self.main_menu)
        back_button.place(x=50, y=50)

        # Marco para la imagen con imagen por defecto
        default_display = self.create_default_image(400, 400, "Seleccione una imagen")
        self.image_label = Label(self.current_frame, image=default_display, 
                               width=400, height=400, bg="white")
        self.image_label.image = default_display
        self.image_label.place(x=440, y=150)

        #Combobox para seleccionar el tipo de modelo
        model_select = ttk.Combobox(state="readonly",values=["Modelo Tradicional", "Red Convolucional"])
        model_select.set("Red Convolucional")
        model_select.place(x=690, y=580)

        # Botón para seleccionar imagen
        select_button = Button(self.current_frame, text="Seleccionar Imagen", 
                             font=(font1, 16), command= lambda : self.select_image(model_select.get()))
        select_button.place(x=440, y=570)

        # Etiqueta para mostrar resultado
        self.result_label = Label(self.current_frame, text="", 
                                font=(font1, 24), bg="#FFCC99")
        self.result_label.place(x=500, y=630)

# Verificar si el modelo está cargado antes de iniciar la aplicación
if __name__ == "__main__":
    root = Tk()
    if not modelo_cargado:
        messagebox.showwarning("Advertencia", 
            "No se pudieron cargar los modelos. La aplicación funcionará con funcionalidad limitada.")
    app = FireDetectionGUI(root)
    app.main_menu()
    root.mainloop()