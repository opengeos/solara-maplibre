import solara
from anymap import MapLibreMap


class Map(MapLibreMap):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        super().add_basemap("Esri.WorldImagery")
        super().add_layer_control(collapsed=False)


@solara.component
def Page():
    with solara.Card():
        Map().element()


Page()
