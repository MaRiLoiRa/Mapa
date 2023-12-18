

import folium
mapa_lojas_westernUnion = folium.Map(location=[-12.982521, -38.513893], zoom_start=5, control_scale=True)
#folium.TileLayer("cartodbpositron").add_to(mapa)
folium.TileLayer(tiles= 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
                 attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                 name= "Esri.WorldStreetMap").add_to(mapa_lojas_westernUnion)

locais = [
    {"coordenadas": [-12.982521, -38.513893], "nome": "4949 - BA Salvador - Shopping Center Lapa"},
    {"coordenadas": [-3.727042, -38.492821], "nome": "3939 - CE - Fortaleza (RUA)"},
    {"coordenadas": [-3.727092, -38.567009], "nome": "6464 - CE - Shopping Rio Mar Kennedy"},
    {"coordenadas": [-15.789126, -47.883007], "nome": "6565 - DF - Brasilia Park Shopping"},
    {"coordenadas": [-15.79575531249659, -47.89292370554968], "nome": "5858 - DF - Brasilia Venâncio"},
    {"coordenadas": [-15.839883, -48.43377], "nome": "5050 - DF - Taguatinga Carrefour"},
    {"coordenadas": [-20.312481, -40.288429], "nome": "3838 - ES - Vitoria - Shopping Vitória"},
    {"coordenadas": [-16.661722, -49.262150], "nome": "6262 - GO - Goiania - Shop. Estação da Moda"},
    {"coordenadas": [-19.974371, -43.946178], "nome": "2727 - BH Shopping"},
    {"coordenadas": [-18.854038, -41.948879], "nome": "3131 - BH  Centro (RUA)"},
    {"coordenadas": [-18.858135, -41.943058], "nome": "3030 - MG - Governador Valadares (RUA)"},
    {"coordenadas": [-21.778067, -46.602848], "nome": "3333 - MG - Poços de Caldas"},
    {"coordenadas": [-18.911570, -48.260410], "nome": "3232 - MG - Uberlândia Carrefour"},
    {"coordenadas": [-20.457415, -54.604893], "nome": "5555 - MS - Campo Grande (RUA)"},
    {"coordenadas": [-1.405112, -48.432442], "nome": "3535 - PA - Belém - Shopping Castanheira"},
    {"coordenadas": [-7.115289, -34.880165], "nome": "4343 - PA - Shopping Tambia João Pessoa"},
    {"coordenadas": [-8.103488, -34.888107], "nome": "4444 - PE - Recife - Galeria Trade Center Julião Lins (RUA)"},
    {"coordenadas": [-25.430992, -49.270000], "nome": "5959 - PR - Galeria Minerva Curitiba"},
    {"coordenadas": [-25.430197, -49.266312], "nome": "7070 - PR - Curitiba Shopping Italia"},
    {"coordenadas": [-23.285429, -51.152225], "nome": "7171 - PR - Londrina Shopping"},
    {"coordenadas": [-23.419853, -51.932278], "nome": "6363 - PR - Maringá - Shopping Cidade"},
    {"coordenadas": [-5.820152, -35.207935], "nome": "4242 - RN - Natal Portugal Center"},
    {"coordenadas": [-30.86510, -51.247849], "nome": "7373 - RS - Porto Alegre I - Barra Shopping Sul"},
    {"coordenadas": [-30.30415, -51.226166], "nome": "4848 - RS - Porto Alegre II (RUA)"},
    {"coordenadas": [-26.992985, -48.646320], "nome": "8080 - SC - Balneário Shopping"},
    {"coordenadas": [-28.679907, -49.369506], "nome": "6969 - SC - Criciuma Galeria Metropolitan"},
    {"coordenadas": [-27.595085, -48.548786], "nome": "0404 - SC - Florianópolis Galeria"},
    {"coordenadas": [-27.618431, -48.647793], "nome": "5454 - SC - São José - Shopping Continente"},
    {"coordenadas": [-19.479073, -42.525642], "nome": "2626 - MG - Ipatinga"},
    {"coordenadas": [-5.78612, -42.799240], "nome": "2828 - PI - Teresina"},
    {"coordenadas": [-19.890453, -43.966896], "nome": "4040 - MG - Shopping Del Rey"},
    {"coordenadas": [-29.915140, -51.165207], "nome": "5252 - RS - Canoas Shopping"},
    {"coordenadas": [-8.103488, -34.888107] , "nome": "5757 - PE - Recife II"},
    {"coordenadas": [-3.732937, -38.498825], "nome": "6464 - CE - Fortaleza III"},
    {"coordenadas": [-29.167117, -51.176960], "nome": "7575 - RS - Caxias do Sul"},
    {"coordenadas": [-21.763203, -43.347637], "nome": "7979 - MG - Juiz de Fora"},
    {"coordenadas": [-20.312481, -40.288429], "nome": "8181 - ES - Vila Velha"},
    {"coordenadas": [-10.969227, -37.37159], "nome": "8686 - Aracaju Shopping"},
    {"coordenadas": [-2.512889, -44.244366], "nome": "8585 - MA - São Luis Shopping"},
    {"coordenadas": [-12.997757, -38.462799], "nome": "8787 - BA - Salvador II Shopping"},
    {"coordenadas": [-16.672035, -49.258874], "nome": "8888 - GO - Goiania II Shopping"},
    {"coordenadas": [-24.945724, -53.477261], "nome": "8989 - PR - Cascavel Shopping"},
    
    
]

for local in locais:
    folium.Marker(
        location=local["coordenadas"],
        popup=local["nome"]
    ).add_to(mapa_lojas_westernUnion)

mapa_lojas_westernUnion.save('mapa_lojas_westernUnion.html')





