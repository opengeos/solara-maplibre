import solara
import reacton.ipyvuetify as rv
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(style="liberty", projection="globe", height="750px")
    m.creater_container(sidebar_visible=True)
    return m


@solara.component
def Page():
    m = create_map()
    container = rv.Row(children=[m.container])
    return container
