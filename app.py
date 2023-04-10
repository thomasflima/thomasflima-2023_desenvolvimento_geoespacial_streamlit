import streamlit as st
from streamlit_folium import folium_static
import folium
import requests

PAGE_CONFIG = {"page_title":"Limites de Curitiba","page_icon":"","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

def main():
    st.title("Limites de Curitiba")
    st.subheader("Meu primeiro mapa no streamlit by Thomas Lima")
    menu = ["Home","Mapa"]
    choice = st.sidebar.selectbox('Menu',menu)
    if choice == 'Home':
        st.subheader("Página Inicial 1")
    elif choice == 'Mapa':
        st.subheader("Visualizar Mapa")
        # Send a GET request to the API URL and get the GeoJSON data
        url = "https://servicodados.ibge.gov.br/api/v3/malhas/municipios/4106902?formato=application/vnd.geo+json&qualidade=minima"
        geo_json_data = requests.get(url).json()
        # Create a style for the GeoJSON data
        style = {'fillColor': 'red', #cor de preenchimento
                 'color': 'red',#cor da linha de contorno
                 'weight': 0.0, #espessura da linha
                }
        # Create a map and add the GeoJSON data to it
        m = folium.Map(location=[-25.5,-49.3],tiles='https://api.mapbox.com/styles/v1/thomaslima22/cld7mhupk000201qurvljhvk0/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoidGhvbWFzbGltYTIyIiwiYSI6ImNrcmNhcWYzOTUxNXUybnJ1MTYyemk2NnMifQ.iNn2WyeT4PxcDcELUieNaQ',
                       attr='Mapbox', zoom_start=11)
        folium.GeoJson(geo_json_data, style_function=lambda x: style).add_to(m)
        folium_static(m)
    else: 
        st.subheader("")

if __name__ == '__main__':
    main()
