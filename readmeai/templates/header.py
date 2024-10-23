from typing import Any, ClassVar

from readmeai.config.constants import HeaderStyleOptions
from readmeai.templates.base import BaseTemplate


class HeaderTemplate(BaseTemplate):
    """
    Class variable for rendering the README.md header style.
    """

    HEADER_TEMPLATES: ClassVar[dict] = {
        HeaderStyleOptions.ASCII: """\
<div align="{align}">\n{image}\n</div>
<p align="{align}">\n\t<em>{slogan}</em>\n</p>
<p align="{align}">\n\t{shields_icons}</p>
<p align="{align}">{badges_tech_stack_text}</p>
<p align="{align}">\n\t{badges_tech_stack}</p>
<br>
""",
        HeaderStyleOptions.CLASSIC: """\
<p align="{align}">
    <img src="{image}" align="{align}" width="{image_width}">
</p>
<p align="{align}"><h1 align="{align}">{repo_name}</h1></p>
<p align="{align}">\n\t<em>{slogan}</em>\n</p>
<p align="{align}">\n\t{shields_icons}</p>
<p align="{align}">{badges_tech_stack_text}</p>
<p align="{align}">\n\t{badges_tech_stack}</p>
<br>
""",
        HeaderStyleOptions.COMPACT: """\
<div align="left">
<img src="{image}" width="{image_width}" align="left" style="margin-right: 15px"/>
<h2 style="display: inline-block; vertical-align: middle; margin-top: 0;">{repo_name}</h2>
<p align="left">\n\t<em>{slogan}</em>\n</p>
<p align="left">\n\t{shields_icons}</p>
<p align="left">{badges_tech_stack_text}</p>
<p align="left">\n\t{badges_tech_stack}</p>
</div>
<br clear="left"/>
""",
        HeaderStyleOptions.MODERN: """\
<div align="left" style="position: relative;">
<img src="{image}" align="right" width="{image_width}" style="margin: -20px 0 0 20px;">
<h1>{repo_name}</h1>
<p align="left">\n\t<em>{slogan}</em>\n</p>
<p align="left">\n\t{shields_icons}</p>
<p align="left">{badges_tech_stack_text}</p>
<p align="left">\n\t{badges_tech_stack}</p>
</div>
<br clear="right">
""",
        HeaderStyleOptions.SVG: """\
<div align="{align}">\n\t<img src="{image}">\n</div>
<p align="{align}">\n\t<em>{slogan}</em>\n</p>
<p align="{align}">\n\t{shields_icons}</p>
<p align="{align}">{badges_tech_stack_text}</p>
<p align="{align}">\n\t{badges_tech_stack}</p>
<br>
""",
    }

    def __init__(self, style: str = HeaderStyleOptions.CLASSIC) -> None:
        self.style = style

    def render(self, data: dict[str, Any]) -> str:
        """Render the header based on the provided data."""
        template = self.HEADER_TEMPLATES.get(
            self.style,
            self.HEADER_TEMPLATES[HeaderStyleOptions.CLASSIC],
        )
        return template.format(**data)

    @staticmethod
    def get_header_template(template: str) -> str:
        """Get the header template for the given style."""
        return HeaderTemplate.HEADER_TEMPLATES[HeaderStyleOptions(template)]
