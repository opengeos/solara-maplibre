import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        center=[-74.0095, 40.7046],
        zoom=16,
        pitch=60,
        bearing=-17,
        style="positron",
        height="750px",
        sidebar_visible=True,
    )
    m.add_basemap("Satellite", visible=False)
    m.add_overture_3d_buildings(template="simple")
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
