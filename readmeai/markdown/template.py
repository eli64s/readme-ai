from abc import ABC, abstractmethod


class ReadmeTemplate(ABC):
    def __init__(self, project):
        self.project = project

    @abstractmethod
    def render(self):
        pass

    def render_description(self):
        return f"{self.project.name} - {self.project.description}"

    def render_install(self):
        return "TODO: Render install"

    # Other common sections


class LibraryTemplate(ReadmeTemplate):
    def render(self):
        readme = f"# {self.project.name}\n\n"

        readme += self.render_description() + "\n\n"

        readme += "## Installation\n\n"
        readme += self.render_install() + "\n\n"

        # Render other sections

        return readme


class WebTemplate(ReadmeTemplate):
    def render_install(self):
        return "TODO: Render web install"

    # Override other sections


template_registry = {"library": LibraryTemplate, "web": WebTemplate}


class Project:
    def __init__(self, type, name, description):
        self.type = type
        self.name = name
        self.description = description


def gen_readme(project):
    template_class = template_registry[project.type]
    template = template_class(project)

    return template.render()


# Example
project = Project("library", "My Library", "Awesome reusable code")

print(gen_readme(project))
