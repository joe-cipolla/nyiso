import dash_bootstrap_components as dbc
import dash_html_components as html


def Navbar():
    navbar = dbc.Navbar(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src='images/logo_inv.jpg', height="30px")),
                        dbc.Col(dbc.NavbarBrand("Power Trading Analytics", className="ml-2"))
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://github.com/joe-cipolla/ptap"
            ),
            dbc.NavItem(dbc.NavLink("Home", href="/index")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        color="dark",
        dark=True,
    )
    return navbar
