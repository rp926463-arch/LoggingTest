import logging.config
import re


class SensitiveDataFilter(logging.Filter):
    pattern = re.compile(r"\d{4}-\d{4}-\d{4}-\d{4}")

    def filter(self, record):
        # Modify the log record to mask sensitive data
        record.msg = self.mask_sensitive_data(record.msg)
        return True

    def mask_sensitive_data(self, message):
        # Implement your logic to mask or modify sensitive data
        # For example, redact credit card numbers like this
        message = self.pattern.sub("[REDACTED]", message)
        return message
