import re

class LogParser:
    def parse_logs(self, logs):
        parsed_logs = []
        log_pattern = r'"reqId":"([^"]+)".*?"level":(\d+).*?"time":"([^"]+)".*?"message":"([^"]+)"'
        
        for log in logs:
            match = re.search(log_pattern, log)
            if match:
                parsed_logs.append({
                    "reqId": match.group(1),
                    "level": int(match.group(2)),
                    "time": match.group(3),
                    "message": match.group(4),
                })
        return parsed_logs
