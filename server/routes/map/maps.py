from . import map_bp
from flask import url_for, render_template

import geobr as gbr
import folium
from folium.plugins import HeatMap


def create_map():
    #gbr.read_municipality(
    #    code_muni='4203202',  # Código do município de Camboriú
    #    year=2020,  # Ano dos dados
    #    simplified=True  # Simplifica a geometria para melhor desempenho
    #)

    coordinates = [
        {"nome": "Prefeitura de Camboriú", "lat": -27.0248, "lon": -48.6523},
        {"nome": "Hospital Cirúrgico Camboriú", "lat": -27.0265, "lon": -48.6518},
        {"nome": "Escola Municipal Professora Clotilde Ramos Chaves", "lat": -27.0098, "lon": -48.6393},
        {"nome": "Supermercado Koch Camboriú", "lat": -27.0181, "lon": -48.6437},
        {"nome": "USF Santa Regina", "lat": -27.0223, "lon": -48.6407}
    ]
    m = folium.Map(location=[-27.02, -48.65], zoom_start=13)

    heat_data = [[local["lat"], local["lon"]] for local in coordinates]

    heat_map = HeatMap(heat_data, radius=15).add_to(m)

    m.get_root().width = '1400px'
    m.get_root().height = '800px'
    return m.get_root()._repr_html_()

##map/view
@map_bp.route('/view')
def maps():
    #moc
    items=['Dengue', 'Focos do mosquito', 'Gripe', 'AIDS', 'HPV', 'HIV']
    iframe = create_map()
    return render_template('index.jinja', title='SAUNA Maps', iframe=iframe, items=items)