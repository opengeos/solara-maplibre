import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="positron",
        projection="globe",
        height="750px",
        zoom=2.5,
        sidebar_visible=True,
    )
    geojson = "https://github.com/opengeos/datasets/releases/download/world/mgrs_grid_zone.geojson"
    m.add_geojson(geojson)
    m.add_labels(geojson, "GZD", text_color="white", min_zoom=2, max_zoom=10)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
