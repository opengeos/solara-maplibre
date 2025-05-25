import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="dark-matter",
        projection="globe",
        height="750px",
        zoom=2.5,
        sidebar_visible=True,
    )
    points_url = "https://github.com/opengeos/datasets/releases/download/world/world_cities.geojson"
    # lines_url = (
    #     "https://github.com/opengeos/datasets/releases/download/vector/cables.geojson"
    # )
    # polygons_url = (
    #     "https://github.com/opengeos/datasets/releases/download/world/countries.geojson"
    # )
    m.add_geojson(points_url, name="Points", fit_bounds=False)
    # m.add_geojson(lines_url, name="Lines")
    # m.add_geojson(polygons_url, name="Polygons")

    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
