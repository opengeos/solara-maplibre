import os
import solara
import pandas as pd
import leafmap.maplibregl as leafmap
import ipywidgets as widgets


def create_map():

    os.environ["TITILER_ENDPOINT"] = "https://titiler.xyz"
    url = "https://huggingface.co/datasets/giswqs/NASA-OPERA/resolve/main/SanFrancisco_OPERA-DISP-S1/filenames.csv"
    df = pd.read_csv(url)
    dates = df["date"].to_list()
    images = df["url"].to_list()

    m = leafmap.Map(
        projection="globe",
        height="750px",
        sidebar_visible=True,
        layer_manager_expanded=False,
    )
    m.add_basemap("USGS.Imagery")
    vmin = -0.02
    vmax = 0.02
    palette = "seismic"
    m.add_time_slider(
        images,
        labels=dates,
        vmin=vmin,
        vmax=vmax,
        colormap_name=palette,
        opacity=0.7,
        expanded=True,
        time_interval=1,
    )
    m.add_colorbar(vmin=vmin, vmax=vmax, palette=palette, label="Displacement (m)")
    # m.set_terrain()

    terrain_checkbox = widgets.Checkbox(
        value=False,
        description="Add 3D Terrain",
        style={"description_width": "initial"},
    )

    def on_terrain_change(change):
        if change["new"]:
            m.set_terrain()
        else:
            m.remove_terrain()

    terrain_checkbox.observe(on_terrain_change, names="value")

    m.add_to_sidebar(terrain_checkbox, add_header=False)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
