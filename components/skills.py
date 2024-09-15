from fasthtml.common import *

def skills():
    return Div(
        # Inline style for media queries
        Style(
            """
            .skills-grid {
                display: grid;
                grid-template-columns: 1fr;
                gap: 1rem;
            }

            @media (min-width: 768px) {
                .skills-grid {
                    grid-template-columns: repeat(2, 1fr);
                }
            }
            """
        ),
        Titled('Skills',
            Div(
                H2('Technical Skills', _class='text-2xl font-semibold text-blue-700 mb-4'),
                
                # Container for grid layout with CSS class
                Div(
                    Div(
                        H3('Programming Languages', _class='text-xl font-semibold text-blue-600 mb-2'),
                        Ul(
                            Li('HTML', _class='text-lg mb-2'),
                            Li('CSS', _class='text-lg mb-2'),
                            Li('Python', _class='text-lg mb-2'),
                            Li('JavaScript', _class='text-lg mb-2'),
                            _class="list-disc ml-5"
                        ),
                        _class='mb-4'
                    ),
                    Div(
                        H3('Frontend Frameworks', _class='text-xl font-semibold text-blue-600 mb-2'),
                        Ul(
                            Li('React', _class='text-lg mb-2'),
                            Li('HTML5, CSS3, Tailwind CSS, Material UI', _class='text-lg mb-2'),
                            _class="list-disc ml-5"
                        ),
                        _class='mb-4'
                    ),
                    Div(
                        H3('Backend Frameworks', _class='text-xl font-semibold text-blue-600 mb-2'),
                        Ul(
                            Li('Flask', _class='text-lg mb-2'),
                            Li('FastAPI', _class='text-lg mb-2'),
                            Li('NodeJS', _class='text-lg mb-2'),
                            _class="list-disc ml-5"
                        ),
                        _class='mb-4'
                    ),
                    Div(
                        H3('Fullstack Frameworks', _class='text-xl font-semibold text-blue-600 mb-2'),
                        Ul(
                            Li('FastHTML', _class='text-lg mb-2'),
                            Li('Flask', _class='text-lg mb-2'),
                            _class="list-disc ml-5"
                        )
                    ),
                    _class="skills-grid"  # Use custom CSS class
                ),
                _class="p-6 rounded-lg shadow-md mb-8"
            ),
            _class="p-6 rounded-lg shadow-md mb-8"
        ),
        id="skills"
    )
