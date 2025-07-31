import streamlit as st
import pandas as pd

st.set_page_config(page_title = "RakingCarrerasPerú", page_icon = "✅")

st.title("📈 Ranking Carreras en el Perú")

lista = [[1,'Medicina',                                 3564, 9175], 
         [2,'Agronegocios',                             1440, 9343],
         [3,'Geología',                                 1725, 7246],
         [4,'Ciencias de la Computación',               1693, 7600],
         [5,'Ingeniería de Sistemas y Cómputo',         1524, 7293],
         [6,'Enfermería',                               1800, 6012],
         [7,'Ingeniería Minera, Metalurgia y Petróleo', 1600, 7139],
         [8,'Ciencias Politicas',                       1540, 7000],
         [9,'Estadística',                              1500, 7042],
         [10,'Ingeniería de Telecomunicaciones',        1637, 6500],
         [11,'Economía',                                1400, 7173],
         [12,'Oficiales de la Policía Nacional',        3176, 4354],
         [13,'Ingeniería eléctrica',                    1500, 6659],
         [14,'Ingeniería mecánica',                     1500, 6720],
         [15,'Derecho',                                 1700, 6598]
         ]

df = pd.DataFrame(lista, columns=["Ranking","Nombre_Carrera", 
                                  "Rango_Inferior", 
                                  "Rango_Superior"])

st.dataframe(df, hide_index = True, height=300)