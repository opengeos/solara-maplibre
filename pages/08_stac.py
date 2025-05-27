import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="liberty",
        projection="globe",
        height="750px",
        zoom=2.5,
        sidebar_visible=True,
    )
    m.add_basemap("Satellite", visible=False)
    m.add_stac_gui()
    m.add_draw_control()
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
