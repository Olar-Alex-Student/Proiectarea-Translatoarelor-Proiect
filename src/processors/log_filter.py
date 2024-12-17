class LogFilter:
    def filter_by_level(self, logs, level):
        return [log for log in logs if log["level"] == level]
