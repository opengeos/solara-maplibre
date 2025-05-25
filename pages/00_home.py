import solara


@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## A Solara Template for MapLibre


        """

        solara.Markdown(markdown)
