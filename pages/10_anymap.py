import solara
from anymap import MapLibreMap


class Map(MapLibreMap):
    def __init__(self, **kwargs):
        super().__init__(
            center=[-117.592133766, 47.653004], zoom=15.3, height="750px", *kwargs
        )
        super().add_basemap("Esri.WorldImagery")
        super().add_layer_control(collapsed=True)
        super().add_geoman_control(
            collapsed=True, show_info_box=True, info_box_mode="click"
        )


@solara.component
def Page():
    with solara.Card():
        Map().element()


Page()
