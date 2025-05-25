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
    data = "https://github.com/opengeos/datasets/releases/download/vector/countries.geojson"
    first_symbol_id = m.find_first_symbol_layer()["id"]
    m.add_data(
        data,
        column="POP_EST",
        scheme="Quantiles",
        cmap="Blues",
        legend_title="Population",
        name="Population",
        before_id=first_symbol_id,
        extrude=True,
        scale_factor=1000,
        fit_bounds=False,
    )
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
