from fasthtml.common import *

def projects():
    return Div(
        Titled('Projects',
            Div(
                H2('Recent Projects', _class='text-2xl font-semibold text-blue-700 mb-4'),
                Ul(
                    Li(
                        Div(
                            H3('Portfolio Website', _class='text-xl font-bold mb-2'),
                            P('A personal portfolio website built with FastHTML and Tailwind CSS.', _class='text-gray-600 mb-2'),
                            P(A('View Project', href='https://portfolio.example.com', _class='text-blue-500 underline'))
                        ),
                        _class='mb-6'
                    ),
                    # Add more projects similarly...
                )
            ),
            _class="p-6 bg-white rounded-lg shadow-md"
        ),
        id="projects"
    )
