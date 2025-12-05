import dash_bootstrap_components as dbc
import dash
from dash import html
# from dash.exceptions import PreventUpdate
# import warnings

dash.register_page(__name__, path='/', name = 'Home')

def serve_layout():
    return dbc.Container(
                fluid = True,
                children = [
                    dbc.Row([
                        dbc.Col([
                            dbc.Carousel(
                                items=[
                                    {
                                        "key": "1",
                                        "src": "/static/images/mns1.jpeg",
                                        "header": "Help us help you",
                                        "caption": "MierenNest is a community of students and the industry aimed at accelerating career development for student and young \
                                        professionals, improving the collective training baseline.",
                                        "caption_class_name": "position-absolute top-50 start-50 translate-middle text-start align-content-around h-75",
                                        "img_style":{'height':'100vh','width':'auto','filter':'grayscale(60%) brightness(40%)','objectFit':'cover'},
                                        "img_class_name":"",
                                    },
                                    {
                                        "key": "2",
                                        "src": "/static/images/mns2.jpeg",
                                        "header": "The currency",
                                        "caption": "Knowledge transfer is the backbone of the space ecosystem. Each entity is specialised and unable to function without \
                                        external expertise.",
                                        "caption_class_name":"position-absolute top-50 start-50 translate-middle text-start align-content-around h-75",
                                        "img_style":{'height':'100vh','width':'auto','filter':'grayscale(60%) brightness(40%)','objectFit':'cover'},
                                        "img_class_name":"",
                                    },
                                    {
                                        "key": "3",
                                        "src": "/static/images/mns3.jpg",
                                        "header": "If you want something done right, do it yourself",
                                        "caption": "In the start-up ecosystem, this manifests as a need for expertise without a pathway to develop it. External experts \
                                        are usually not a feasible option for start/scale-ups.",
                                        "caption_class_name":"position-absolute top-50 start-50 translate-middle text-start align-content-around h-75",
                                        "img_style":{'height':'100vh','width':'auto','filter':'grayscale(60%) brightness(40%)','objectFit':'cover'},
                                        "img_class_name":"",
                                    },
                                    {
                                        "key": "4",
                                        "src": "/static/images/mns4.jpg",
                                        "header": "Temet Nosce",
                                        "caption": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                                        "caption_class_name":"position-absolute top-50 start-50 translate-middle text-start align-content-around h-75",
                                        "img_style":{'height':'100vh','width':'auto','filter':'grayscale(60%) brightness(40%)','objectFit':'cover'},
                                        "img_class_name":"",
                                    },
                                    {
                                        "key": "5",
                                        "src": "/static/images/mns5.jpeg",
                                        "header": "If you are not being charged, you are the product",
                                        "caption": "Researchers are information and knowledge on the move. Students carry knowledge through doors. They apply it to \
                                        specific cases and  turn it into solutions. Welcome to the knowledge economy.",
                                        "caption_class_name":"position-absolute top-50 start-50 translate-middle text-start align-content-around h-75",
                                        "img_style":{'height':'100vh','width':'auto','filter':'grayscale(60%) brightness(40%)','objectFit':'cover'},
                                        "img_class_name":"",
                                    },
                                ], style = {'width':'100%','height':'auto', 'fontSize' : '3vh'}, class_name = "", #'filter':'grayscale(80%) brightness(40%)',
                            ),
                        ],style = {'height':'100%', 'width':'100%'},class_name= "d-flex m-0 p-0 "),
                    ],style = {'height':'100%', 'width':'100%', 'margin':'0',}, className = "d-flex p-0 "),

                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Img(
                                        title = "Strategy icons created by DinosoftLabs - Flaticon",
                                        alt="Strategy icons created by DinosoftLabs - Flaticon",
                                        src="/static/images/puzzle-piece.png",
                                        style = {'filter':'invert(1)', 'objectFit':'scale-down','height':'20vh'},
                                    ),
                                    html.P(["MierenNest is a symbiotic community of students and the industry aimed at accelerating career development for student and young professionals"],
                                        style = {'overflow':'visible','height':'20vh'},),
                                    # <a href="https://www.flaticon.com/free-icons/strategy" title="strategy icons">Strategy icons created by DinosoftLabs - Flaticon</a>
                                ],
                                style = {'height':'50vh','flexDirection':'column', "gap":"10%"},
                                className = "d-flex text-white justify-content-center align-items-center m-0 p-5",
                                width = 12,
                                md = 3,
                            ),
                            dbc.Col(
                                [
                                    html.Img(
                                        title = "Strategy icons created by DinosoftLabs - Flaticon",
                                        alt="Strategy icons created by DinosoftLabs - Flaticon",
                                        src="/static/images/puzzle-piece.png",
                                        style = {'filter':'invert(1)', 'objectFit':'scale-down','height':'20vh', 'justifyContent':'center', 'borderColor':'white'},
                                    ),
                                    html.P(["More than just internships, we provide mini-R&D extensions consisting of students but with research grade output guarantees through supervision by professionals"],
                                        style = {'overflow':'visible','height':'20vh'},),
                                    # <a href="https://www.flaticon.com/free-icons/strategy" title="strategy icons">Strategy icons created by DinosoftLabs - Flaticon</a>
                                ],
                                style = {'height':'50vh','flexDirection':'column', "gap":"10%"},
                                className = "d-flex text-white justify-content-center align-items-center m-0 p-5",
                                width = 12,
                                md = 3,
                                
                            ),
                            dbc.Col(
                                [
                                    html.Img(
                                        title = "Strategy icons created by DinosoftLabs - Flaticon",
                                        alt="Strategy icons created by DinosoftLabs - Flaticon",
                                        src="/static/images/puzzle-piece.png",
                                        style = {'filter':'invert(1)', 'objectFit':'scale-down','height':'20vh'},
                                    ),
                                    html.P(["We enable this collaboration through our suite of management / admin services focussed on efficient project execution. Our services offer an informed pathway to recruitment for start-ups and scale-ups navigating financial constraints"],
                                        style = {'overflow':'visible','height':'20vh'},),
                                ],
                                style = {'height':'50vh','flexDirection':'column', "gap":"10%"},
                                className = "d-flex text-white justify-content-center align-items-center m-0 p-5",
                                width = 12,
                                md = 3,
                                
                            ),
                        ],
                        id = 'about',
                        style = {'height':'auto', 'width':'100%', 'padding':'0', 'paddingBottom':'5vh', 'paddingTop':'5vh', 'gap':'0%',}, # 'flex-direction':'column'
                        className = "d-flex flex-column flex-md-row bg-primary align-items-center justify-content-center m-0",
                    ),

                    dbc.Row([
                            dbc.Col(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(["Let's get in touch !"])
                                        ],
                                        # style = {"width":'35%'},
                                        className = "d-flex h2 m-0 p-0",
                                    ),
                                    html.Hr(
                                        style={
                                        # # "borderWidth": "0.5vh",
                                        "width": "10%",
                                        # # "borderColor": "#F3DE8A",
                                        "opacity": "unset",
                                        },
                                        className='hr divider',
                                    ),
                                    dbc.Row([
                                            dbc.Col(
                                                [
                                                    html.P(["At MierenNest we encourage authenticity, we embody our experiences and believe these \
                                                            are best communicated in-person. We encourage all our stakeholders — students, space \
                                                            business and other aligned organizations — to schedule in-person conversations."],
                                                            # style = {'border':'1','border-color':'primary'}
                                                    ),
                                                    dbc.Button(
                                                        ["Book an appointment"],
                                                        color="primary",
                                                        external_link = True,
                                                        target="_blank",
                                                        href = 'https://calendar.app.google/X7zW6sV1u6VL2Sj3A',
                                                        style = {'margin':'0', 'marginTop':'2em'},
                                                        className="d-grid mx-auto",
                                                    ),
                                                ],
                                            ),
                                        ],
                                        style = {'textAlign':'justify', 'gap':'10%',},
                                        className = "d-flex col-form-label justify-content-center align-items-center m-0 p-0",
                                    ),
                                ],
                                className = "d-flex flex-column justify-content-center align-items-center text-center m-0 p-5",
                                width = 12,
                                md = 4,
                            ),
                        ],
                        id = 'contact',
                        style = {'height':'auto','padding':'0', 'paddingBottom':'5vh', 'paddingTop':'5vh'},
                        className = "d-flex bg-white align-items-center justify-content-center m-0"
                    ),
                ],style = {'height':'auto', 'width':'100%'}, className = "m-0 p-0",
            )

layout = serve_layout