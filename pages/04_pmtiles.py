import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="dark-matter",
        projection="globe",
        height="750px",
        center=[-100, 40],
        zoom=4,
        sidebar_visible=True,
    )

    building_pmtiles = "https://overturemaps-tiles-us-west-2-beta.s3.amazonaws.com/2025-04-23/buildings.pmtiles"
    road_pmtiles = "https://overturemaps-tiles-us-west-2-beta.s3.amazonaws.com/2025-04-23/transportation.pmtiles"
    building_style = {
        "layers": [
            {
                "id": "Buildings",
                "source": "buildings",
                "source-layer": "building",
                "type": "line",
                "paint": {
                    "line-color": "#ff0000",
                    "line-width": 1,
                },
            },
        ]
    }
    road_style = {
        "layers": [
            {
                "id": "Roads",
                "source": "transportation",
                "source-layer": "segment",
                "type": "line",
                "paint": {
                    "line-color": "#ffffff",
                    "line-width": 2,
                },
            },
        ]
    }
    m.add_pmtiles(
        building_pmtiles, style=building_style, tooltip=True, fit_bounds=False
    )
    m.add_pmtiles(road_pmtiles, style=road_style, tooltip=True, fit_bounds=False)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
