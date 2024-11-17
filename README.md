# Trabajo Final - Procesamiento de Imágenes 

## Objetivo del trabajo
La propuesta de este trabajo es evaluar la capacidad de técnicas tradicionales y avanzadas de procesamiento de imágenes para detectar incendios en zonas urbanas a partir de imágenes captadas por cámaras. Para ello, se explorarán dos enfoques: uno basado en transformaciones geométricas y segmentación de imágenes, y otro basado en redes neuronales convolucionales. Ambos enfoques serán evaluados en términos de velocidad de detección, precisión y capacidad para identificar correctamente la presencia y expansión de incendios en escenarios urbanos. Se buscará la respuesta a las siguientes preguntas:
 
* ¿Cuál de las dos técnicas de procesamiento de imágenes es más rápida para detectar incendios urbanos?
* ¿Cuál de las dos técnicas se equivoca menos en la detección de incendios urbanos?
* En promedio, ¿cuál es la precisión de ambas técnicas para detectar incendios urbanos?

## Alumnos participantes
El equipo para la realización de esta trabajo final está conformado por las siguientes personas:

* Rodrigo Alonso Ramírez Cesti (u202210690)
* Tarik Gustavo Morales Oliveros (u202210472)
* Eduardo José Rivas Siesquén (u202216407)
* Paula Jimena Mancilla Cienfuegos (u202115844)

## Descripción del dataset
Utilizaremos la base de datos “FIRE Dataset”, recuperada de Kaggle el 18 de Septiembre del 2024. 
Esta base de datos consiste de dos folders: 
- fire_images: Un folder con 755 imágenes que contienen escenarios de fuegos/incendios, en diferentes ambientes.
- non-fire_images: Un folder con 244 imágenes de múltiples escenarios, como bosques, árboles, cuerpos de agua, personas, etc.
Todas las imágenes se encuentran presentes en un mismo formato (png).
URL del sitio web donde se obtuvo la base de datos: [Link del dataset](https://www.kaggle.com/datasets/phylake1337/fire-dataset)

## Conclusiones
- La tecnología de segmentación y procesamiento de imágenes sirve de gran ayuda para identificar cosas en lugares a los que los ojos humanos no pueden llegar. No solo se puede usar para detectar fuegos, sino también objetos peligrosos, armas, personas sospechosas de algún crimen, etc.
- El modelo más rápido y confiable de los dos ha sido el de la Red Convolucional. Es más rápido ya que pudimos cargarlo como un modelo pre-entrenado en el código, en vez de tener que entrenarlo cada vez que se ejecuta el programa. Y es más confiable, ya que por los diferentes tests que hemos hecho, la Red Convolucional es más confiable para detectar fuego puro. Sin embargo, el Modelo Tradicional sí puede detectar fuegos en menores cantidades, y sirve para detectar humo más confiablemente.
- El análisis realizado en el presente trabajo ha demostrado la importancia de evaluar tanto el rendimiento como la implementación de modelos en este tipo de tareas, destacando estas técnicas por su enfoque práctico con usos de métricas para medir el rendimiento y generar interpretaciones basadas en precisión, sensibilidad y exactitud. La correcta estructuración del código en nuestros modelos, y el uso de herramientas de evaluación robustas pueden ser suficientes para abordar problemas específicos de clasificación, con lo cual se permite generar sistemas eficientes, incluso en escenarios con recursos limitados, mientras se mantienen estándares de confiabilidad y aplicabilidad.
- La sencillez de funcionamiento, tasas de efectividad y la necesidad solamente de inputs básicos como imágenes hace que este programa pueda ser fácilmente aplicado en diferentes sistemas y lugares en el mundo, especialmente zonas urbanas, donde se necesitaría únicamente de la obtención periódica de imágenes de una área por medio de una cámara para poder realizar la supervisión de la zona y detectar incendios cuando estos se originen. De esta forma, tiene un impacto en las dimensiones social, ambiental y económico.

## Licencia
El código de este proyecto está publicado bajo la [Licencia MIT](https://github.com/EduRS14/CC235-TP-TF-2024-2/blob/main/LICENSE)

