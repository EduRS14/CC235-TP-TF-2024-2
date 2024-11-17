import zipfile
import os
import cv2
import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Descomprimir el archivo .zip
zip_path = "content/archive.zip"
extract_path = "content/dataset"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# Verificar la estructura de las carpetas
for root, dirs, files in os.walk(extract_path):
    print(root, "contiene", len(files), "archivos y", len(dirs), "carpetas")

# Definir rutas a las carpetas de Train, Test, y Validation
train_folder = os.path.join(extract_path, "Train")
test_folder = os.path.join(extract_path, "Test")
vali_folder = os.path.join(extract_path, "Vali")

# Cargar las imágenes desde las carpetas
def load_images_from_folder(folder):
    images, labels = [], []
    for label, subfolder in enumerate(["Fire", "Non-Fire"]):
        path = os.path.join(folder, subfolder)
        for filename in os.listdir(path):
            img_path = os.path.join(path, filename)
            img = cv2.imread(img_path)
            if img is not None:
                img = cv2.resize(img, (224, 224))
                images.append(img)
                labels.append(label)
    return np.array(images), np.array(labels)

# Segmentación de colores para detectar fuego
def segment_fire(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    fire_mask = mask1 | mask2
    return fire_mask

# Segmentación de colores para detectar humo (ajustado con rango HSV)
def segment_smoke(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_gray = np.array([0, 0, 200])  # Tonos grisáceos claros
    upper_gray = np.array([180, 50, 255])
    smoke_mask = cv2.inRange(hsv, lower_gray, upper_gray)
    return smoke_mask

# Evaluación del modelo
def evaluate_model(images, labels, detector_function):
    y_true, y_pred = [], []
    for img, label in zip(images, labels):
        mask = detector_function(img)
        detected = 1 if np.sum(mask) > 0 else 0
        y_true.append(label)
        y_pred.append(detected)
    f1 = f1_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    return f1, precision, recall

# Cargar datos
train_images, train_labels = load_images_from_folder(train_folder)
test_images, test_labels = load_images_from_folder(test_folder)

# Evaluar detección de fuego
print("Evaluación para detección de fuego:")
fire_f1, fire_precision, fire_recall = evaluate_model(test_images, test_labels, segment_fire)
print(f"F1 Score: {fire_f1:.2f}, Precision: {fire_precision:.2f}, Recall: {fire_recall:.2f}")

# Evaluar detección de humo
print("\nEvaluación para detección de humo:")
smoke_f1, smoke_precision, smoke_recall = evaluate_model(test_images, test_labels, segment_smoke)
print(f"F1 Score: {smoke_f1:.2f}, Precision: {smoke_precision:.2f}, Recall: {smoke_recall:.2f}")

# Visualización de resultados con leyenda
def get_antiprobability(image):
    print("got to antiprob")
    print()
    img = image
    fire_mask = segment_fire(img)

    # Calcular la antiposibilidad (porcentaje de píxeles no detectados como fuego)
    total_pixels = fire_mask.size
    fire_pixels = np.sum(fire_mask > 0)
    anti_fire_probability = (fire_pixels / total_pixels)
    print("got to calculate antiprob")
    print()
    return anti_fire_probability


# Visualización de detección de fuego y humo con leyendas
def leer_img(dir):
    img = cv2.imread(dir)
    img = cv2.resize(img, (224,224))
    return get_antiprobability(img)

#img = cv2.imread('UI_images/cat.PNG')
