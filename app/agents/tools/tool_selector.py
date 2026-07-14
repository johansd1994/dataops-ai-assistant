class ToolSelector:

    @staticmethod
    def select(message: str):

        text = message.lower()

        if any(word in text for word in [
            "athena",
            "sql",
            "consulta",
            "query",
            "tabla",
            "database",
            "base de datos"
        ]):
            return "athena"

        if any(word in text for word in [
            "s3",
            "bucket",
            "archivo",
            "objeto"
        ]):
            return "s3"

        return None