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

    m.add_ee_layer(asset_id="ESA/WorldCover/v200", opacity=0.8)
    m.add_overture_3d_buildings()

    m.add_legend_to_sidebar(
        builtin_legend="ESA_WorldCover", title="Land Cover Type", shape_type="rectangle"
    )
    m.add_colorbar_to_sidebar(cmap="terrain", label="Elevation")

    image = "https://i.imgur.com/KeiAsTv.gif"
    m.add_image_to_sidebar(image=image, expanded=False)

    video = "https://static-assets.mapbox.com/mapbox-gl-js/drone.mp4"
    m.add_video_to_sidebar(video, expanded=False)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
