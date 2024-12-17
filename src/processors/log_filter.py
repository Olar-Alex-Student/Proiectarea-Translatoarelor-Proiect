class LogFilter:
    def filter_by_level(self, logs, level):
        """Filtrează logurile pe baza unui nivel specific."""
        return [log for log in logs if log["level"] == level]
