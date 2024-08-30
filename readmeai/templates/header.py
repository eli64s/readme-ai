import enum
from typing import Any, ClassVar

from .base_template import BaseTemplate


class HeaderStyle(enum.StrEnum):
    """
    Enum containing header styles for the README file.
    """

    CLASSIC = enum.auto()
    COMPACT = enum.auto()
    MODERN = enum.auto()


class HeaderTemplate(BaseTemplate):
    """
    Class variable for rendering the README.md header style.
    """

    HEADER_TEMPLATES: ClassVar[dict] = {
        HeaderStyle.CLASSIC: """\
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
<p align="{align}">\n\t{badge_icons}</p>

<br>
""",
        HeaderStyle.COMPACT: """\
[<img src="{image}" align="left" width="{image_width}" padding="20">]()

## &nbsp;&nbsp; {repo_name}

&nbsp;&nbsp;&nbsp;&nbsp; *{slogan}*

<p align="left">&nbsp;&nbsp;\n\t{shields_icons}</p>

<br>
""",
        HeaderStyle.MODERN.value: """\
[<img src="{image}" align="right" width="25%" padding-right="350">]()

# `{repo_name}`

#### {slogan}

<p align="left">\n\t{shields_icons}</p>
<p align="left">\n\t{badge_icons}</p>

<br>
""",
    }

    def __init__(self, style: str = HeaderStyle.CLASSIC) -> None:
        """
        Initialize the header template with the given style.
        """
        self.style = style

    def render(self, data: dict[str, Any]) -> str:
        """
        Render the header based on the current style and given data.
        """
        template = self.HEADER_TEMPLATES.get(
            self.style,
            self.HEADER_TEMPLATES[HeaderStyle.CLASSIC],
        )
        return template.format(**data)

    @staticmethod
    def get_header_template(template: str) -> str:
        """
        Get the header template for the given style.
        """
        try:
            return HeaderTemplate.HEADER_TEMPLATES[HeaderStyle(template)]
        except ValueError:
            return HeaderTemplate.HEADER_TEMPLATES[HeaderStyle.CLASSIC]
