import numpy as np
import pandas as pd
# import plotly.express as px
import dash_bootstrap_components as dbc
import dash
from dash import html, dcc, Input, Output, callback, State
# from dash.exceptions import PreventUpdate

app = dash.Dash(__name__, use_pages = True) # external_stylesheets=[dbc.themes.QUARTZ]

server = app.server

navitems = dbc.Row([
        dbc.Col(
            [
                dbc.NavItem(
                    dbc.NavLink(
                        page['name'],
                        href=page['path'],
                        active = 'exact',
                        class_name="nav-link"
                    )
                ) for page in dash.page_registry.values()
            ]
        ),
        dbc.Col(
            [
                dbc.NavItem(
                    dbc.NavLink(
                        "About",
                        href="#about",
                        external_link=True,
                        active = 'exact', class_name="nav-link")
                )
            ],
            class_name = 'nav-item',
        ),
        dbc.Col(
            [
                dbc.NavItem(
                    dbc.NavLink(
                        "Contact",
                        href="#contact",
                        external_link=True,
                        active = 'exact', class_name="nav-link")
                )
            ],
            class_name = 'nav-item',
        ),
    ],
    className="navbar-nav ms-auto mt-3 mt-md-0",
    align = 'center',
),
# +[
#                 dbc.NavItem(
#                     dbc.NavLink(
#                         "About",
#                         href="#about",
#                         external_link=True,
#                         active = 'exact', class_name="nav-link")
#                 )
#             ]+[
#                 dbc.NavItem(
#                     dbc.NavLink(
#                         "Contact",
#                         href="#contact",
#                         active = 'exact',
#                         external_link=True,
#                         class_name="nav-link",
#                     )
#                 )
#             ]

app.layout = html.Div(
    [
        # main app framework
        dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        # Use row and col to control vertical alignment of logo / brand
                        dbc.Row(
                            [
                                # dbc.Col(html.Img(src=LOGO, height="30px")),
                                dbc.Col(dbc.NavbarBrand("MierenNest", className="navbar-brand")),
                            ],
                            align="center",
                            className="g-0",
                        ),
                        href="https://www.linkedin.com/in/ambar-qadeer/",
                        style={"textDecoration": "none"},
                    ),
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0, class_name = 'navbar-toggler navbar-toggler-right'),
                    dbc.Collapse(
                        navitems,
                        id="navbarResponsive",
                        is_open=False,
                        navbar=True,
                        class_name = 'collapse navbar-collapse'
                    ),
                ],
                
            ),
            id = "mainNav",
            color="None",
            dark=None,
            class_name="navbar navbar-expand-md navbar-light fixed-top py-3"
        ),
        # dbc.NavbarSimple(
        #     id = "mainNav",
        #     children=[
        #         dbc.NavItem(
        #             dbc.NavLink(
        #                 page['name'],
        #                 href=page['path'],
        #                 active = 'exact',
        #                 class_name="nav-link"
        #             )
        #         ) for page in dash.page_registry.values()
        #     ]+[
        #         dbc.NavItem(
        #             dbc.NavLink(
        #                 "About",
        #                 href="#about",
        #                 external_link=True,
        #                 active = 'exact', class_name="")
        #         )
        #     ]+[
        #         dbc.NavItem(
        #             dbc.NavLink(
        #                 "Contact",
        #                 href="#contact",
        #                 active = 'exact',
        #                 external_link=True,
        #                 class_name="",
        #             )
        #         )
        #     ],
        #     brand="MierenNest",
        #     brand_href="https://www.linkedin.com/in/ambar-qadeer",
        #     color= None,
        #     # width = 'auto',
        #     fixed = True,
        #     dark=None,
        #     fluid = True,
        #     sticky = 'top',
        #     class_name = 'navbar navbar-expand-md navbar-light w-100 align-items-center',
        #     style = {'height':'10vh'},
        #     brand_style={'fontSize':'3vh', 'fontWeight':'bold', 'fontStretch':'expanded', 'backgroundColor' : 'transparent'},
        # ),
        # dbc.Nav(
        #     id = "mainNav",
        #     children=[
        #         dbc.NavItem(
        #             dbc.NavLink(
        #                 page['name'],
        #                 href=page['path'],
        #                 active = 'exact',
        #                 class_name="nav-item nav-link"
        #             )
        #         ) for page in dash.page_registry.values()
        #     ]+[
        #         dbc.NavItem(
        #             dbc.NavLink(
        #                 "About",
        #                 href="#about",
        #                 external_link=True,
        #                 active = 'exact', class_name="nav-item nav-link")
        #         )
        #     ]+[
        #         dbc.NavItem(
        #             dbc.NavLink(
        #                 "Contact",
        #                 href="#contact",
        #                 active = 'exact',
        #                 external_link=True,
        #                 class_name="nav-item nav-link",
        #             )
        #         )
        #     ],
        #     class_name = 'navbar navbar-expand-lg navbar-light fixed-top py-3',
        #     style = {'height':'10vh', },
        # ),
        dash.page_container
    ],
    style = {'width':'100%', 'height':'auto', 'padding':'0px', 'margin':'0px'},
)

@app.callback(
    Output("navbarResponsive", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbarResponsive", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run(debug=True,)