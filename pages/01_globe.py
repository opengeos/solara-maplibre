import solara
import reacton.ipyvuetify as rv
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(style="liberty", projection="globe", sidebar_visible=True)
    m.creater_container()
    return m


@solara.component
def Page():
    m = create_map()
    container = rv.Row(children=[m.container])
    return container
