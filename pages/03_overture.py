import solara
import reacton.ipyvuetify as rv
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        center=[-74.0095, 40.7046],
        zoom=16,
        pitch=60,
        bearing=-17,
        style="positron",
        height="750px",
    )
    m.create_container(sidebar_visible=True)
    m.add_basemap("Esri.WorldImagery", visible=False)
    m.add_overture_3d_buildings(template="simple")
    m.add_layer_control()
    return m


@solara.component
def Page():
    m = create_map()
    container = rv.Row(children=[m.container])
    return container
