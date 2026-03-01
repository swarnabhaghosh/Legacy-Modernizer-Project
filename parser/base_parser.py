class BaseParser:
    def parse(self, repo_path):
        """
        Parse repository and return method_map
        Must be implemented by child parsers.
        """
        raise NotImplementedError("Parser must implement parse()")