import justpy as jp


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout, elevated=True)
        # header.on("class", "bg-primary text-white")
        toolbar = jp.QToolbar(a=header)
        q_drawer = jp.QDrawer(a=layout, show_if_above=True, v_model="left", side="left", bordered=True)

        scroll_area = jp.QScrollArea(a=q_drawer, classes="fit")
        drawer_list = jp.QList(a=scroll_area)
        list_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=drawer_list, text="Home", href="/", classes=list_classes)
        jp.Br(a=drawer_list)
        jp.A(a=drawer_list, text="Dictionary", href="/dictionary", classes=list_classes)
        jp.Br(a=drawer_list)
        jp.A(a=drawer_list, text="About", href="/about", classes=list_classes)
        jp.Br(a=drawer_list)

        q_button = jp.QButton(a=toolbar, dense=True, flat=True, icon="menu", click=cls.move_drawer, drawer=q_drawer)
        # q_button.on("round", True)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")
        page_container = jp.QPageContainer(a=layout)

        div = jp.Div(a=page_container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        afdgdfglk ;lsdfgldkfl; ;fmdfsjg;ij; kjsdoiugfjdsfdk
        """, classes="text-lg")
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
