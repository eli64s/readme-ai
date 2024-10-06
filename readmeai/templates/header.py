import enum
from typing import Any, ClassVar

from readmeai.templates.base import BaseTemplate


class HeaderStyleOptions(str, enum.Enum):
    """
    Enum of supported 'Header' template styles for the README file.
    """

    CLASSIC = "classic"
    COMPACT = "compact"
    MODERN = "modern"


class HeaderTemplate(BaseTemplate):
    """
    Class variable for rendering the README.md header style.
    """

    HEADER_TEMPLATES: ClassVar[dict] = {
        HeaderStyleOptions.CLASSIC: """\
<p align="{align}">
  <img src="{image}" width="{image_width}" alt="{repo_name}-logo">
</p>
<p align="{align}">
    <h1 align="{align}">{repo_name}</h1>
</p>
<p align="{align}">
    <em>{slogan}</em>
</p>
<p align="{align}">\n\t{shields_icons}</p>
<p align="{align}">\n\t{badges_tech_stack}</p>
<br>
""",
        HeaderStyleOptions.COMPACT: """\
[<img src="{image}" align="left" width="{image_width}" padding="20">]()

## &nbsp;&nbsp; {repo_name}

&nbsp;&nbsp;&nbsp;&nbsp; *{slogan}*

<p align="left">&nbsp;&nbsp;\n\t{shields_icons}</p>
<br>
""",
        HeaderStyleOptions.MODERN.value: """\
[<img src="{image}" align="right" width="25%" padding-right="350">]()

# `{repo_name}`

#### {slogan}

<p align="{align}">\n\t{shields_icons}</p>
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
