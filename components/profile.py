from fasthtml.common import *
from components.header import header
from components.introduction import introduction
from components.skills import skills
from components.projects import projects
from components.contact import contact

def portfolio():
    return Div(
        # Link to the compiled Tailwind CSS
        Link(href='/static/css/output.css', rel='stylesheet'),

        # Inline style for media queries
        Style(
            """
            @media (min-width: 768px) {
                .container {
                    width: 800px;
                    margin: 0 auto;
                }
            }
            """
        ),
        
        # Rendering all the components
        header(),
        introduction(),
        skills(),
        projects(),
        contact(),
        _class='container'  # Apply the container class with the responsive width
    )
