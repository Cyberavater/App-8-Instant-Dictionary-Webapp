import justpy as jp


class DefaultLayout(jp.QuasarPage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # layout = jp.QLayout(a=self, view="hHh lpR fFf")
        header = jp.QHeader(a=self, elevated=True)
        # header.on("class", "bg-primary text-white")
        toolbar = jp.QToolbar(a=header)
        q_drawer = jp.QDrawer(a=self, show_if_above=True, v_model="left", side="left", bordered=True)

        scroll_area = jp.QScrollArea(a=q_drawer, classes="fit")
        drawer_list = jp.QList(a=scroll_area)
        list_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=drawer_list, text="Home", href="/", classes=list_classes)
        jp.Br(a=drawer_list)
        jp.A(a=drawer_list, text="Dictionary", href="/dictionary", classes=list_classes)
        jp.Br(a=drawer_list)
        jp.A(a=drawer_list, text="About", href="/about", classes=list_classes)
        jp.Br(a=drawer_list)

        jp.QBtn(a=toolbar, dense=True, flat=True, icon="menu", click=self.move_drawer, drawer=q_drawer)
        # q_button.on("round", True)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
