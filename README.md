# Trabajo Aplicado 
Repositorio del trabajo aplicado de PROGRAMACIÓN I. 
Integrantes: Pilar Calderaro, Valentina Entrala, Tomas Lopez Durand, Ema Nielsen

Funcionamiento general: 

Descripcion de la fuente de datos:
El dataset que contiene a los 5mil paricipantes del test de Holland es un archivo de excel creado con IA y guardado en la carpeta "datos" dentro del repositorio.

Instrucciones para ejecutar el programa: 
 
Librerias utilizadas: Se utilizo la libreria de PANDAS y STREAMLIT

Estructura del repositorio: 

Explicación breve de las funciones principales:
-Finales:
-Clasif_rtas: Se recorre la lista de respuestas y se suma valores al contador dependiendo de lo que el usuario respondió.
-Filtrar_Dataset:
-Diseño: Se generan 3 gráficos (de barras, de torta, hexagonal) en base a las respuestas del usuario y al dataset con los 5mil participantes. Esos gráficos se pueden ver en un dashboard generado por streamlit.

Resultados: Este programa crea 3 gráficos distintos. Uno de torta, otro hexagonal y un último de líneas.

Diagramas de flujo: En la carpeta "guia de trabajo" se encuentran todos los diagramas de flujo y un texto explicando el funcionamiento general (un poco mas amplio que el de acá) del código.

Uso de IA:
-Se utilizó la IA para la creación del dataset con el siguiente propt:
    "Créame una base de datos que contenga los apartados de: personas, personalidad laboral de Holland, carreras elegidas, nivel de satisfacción con la carrera elegida. Como columnas y las filas deben ser una numeración (uno por uno) del total de participantes. Si ya existe una base de datos que contenga eso, no la crees, solo pásamela, si no existe, créala. Si la tenes que crear que sea larga (como una base de datos real)"

-Además utilizamos la IA para la creación del dashboard interactivo donde se responden las preguntas de la historia. El prompt fue el siguiente:
    