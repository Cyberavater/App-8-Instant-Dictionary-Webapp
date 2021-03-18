import justpy as jp
import webapp.layout as xp


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = xp.DefaultLayout(a=wp, view="hHh lpR fFf")

        page_container = jp.QPageContainer(a=lay)

        div = jp.Div(a=page_container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        afdgdfglk ;lsdfgldkfl; ;fmdfsjg;ij; kjsdoiugfjdsfdk
        """, classes="text-lg")
        return wp
