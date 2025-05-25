import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        center=[-122.514426, 37.562984],
        zoom=17,
        bearing=-96,
        height="750px",
        sidebar_visible=True,
    )
    m.add_basemap("Satellite")
    urls = [
        "https://static-assets.mapbox.com/mapbox-gl-js/drone.mp4",
        "https://static-assets.mapbox.com/mapbox-gl-js/drone.webm",
    ]
    coordinates = [
        [-122.51596391201019, 37.56238816766053],
        [-122.51467645168304, 37.56410183312965],
        [-122.51309394836426, 37.563391708549425],
        [-122.51423120498657, 37.56161849366671],
    ]
    m.add_video(urls, coordinates)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
