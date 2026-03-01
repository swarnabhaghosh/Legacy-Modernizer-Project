from parser.java_parser import JavaParser
from parser.python_parser import PythonParser


def get_parser(language):
    language = language.lower()

    if language == "java":
        return JavaParser()

    elif language == "python":
        return PythonParser()

    else:
        raise ValueError(f"Unsupported language: {language}")