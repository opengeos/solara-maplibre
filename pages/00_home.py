import solara


@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## 3D Mapping with Leafmap and MapLibre

        This is a Solara template for a 3D mapping application using Leafmap and MapLibre. Click on the menu above to see the different examples.
        <br>
        Source code: <https://github.com/opengeos/solara-maplibre>

        ![image](https://github.com/user-attachments/assets/efc9e43b-99c0-40b4-af08-4971e8b96919)
        """

        solara.Markdown(markdown)
