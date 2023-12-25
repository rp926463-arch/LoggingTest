import logging

from psutil import cpu_percent, virtual_memory


class PsutilFilter(logging.Filter):
    """psutil logging filter."""

    def filter(self, record: logging.LogRecord) -> bool:
        """Add contextual information about the currently used CPU and virtual memory percentages into the given log record."""
        record.psutil = f"c{cpu_percent():02.0f}m{virtual_memory().percent:02.0f}"  # type: ignore
        return True