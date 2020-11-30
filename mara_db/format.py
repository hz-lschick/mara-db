"""Different formats for piping"""

class Format:
    """Base format definition"""

    def __repr__(self) -> str:
        return (f'<{self.__class__.__name__}: '
                + ', '.join([f'{var}={getattr(self, var)}'
                             for var in vars(self) if getattr(self, var)])
                + '>')


class CsvFormat(Format):
    """
    CSV file format. See https://tools.ietf.org/html/rfc4180
    """
    def __init__(self, delimiter_char: str = None, quote_char: str = None, with_header_line: bool = None):
        """
        CSV file format. See https://tools.ietf.org/html/rfc4180

        Args:
            header_line: If a header line should be added
            delimiter_char: The character that separates columns
            quote_char: The character for quoting strings
        """
        self.delimiter_char = delimiter_char
        self.quote_char = quote_char
        self.with_header_line = with_header_line


class JsonlFormat(Format):
    """New line delimited JSON stream. See https://en.wikipedia.org/wiki/JSON_streaming"""
    pass


class AvroFormat(Format):
    """Apache Avro"""
    pass


class ParquetFormat(Format):
    """Apache Parquet"""
    pass


class OrcFormat(Format):
    """Apache ORC"""
    pass
