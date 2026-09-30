import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("template_for_python_uv_projects")


class MyClass:
    def my_method(self):
        return "Hello World"


logger.info("template_for_python_uv_projects loaded")
