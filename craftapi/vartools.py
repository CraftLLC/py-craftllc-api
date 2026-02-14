class VarTools:
    """Tools for working with variables and data formatting."""
    
    def __init__(self, varlist):
        """
        Initializes VarTools with a list of variables.

        :param varlist: Dictionary or list of variables to process.
        """
        self.varlist = varlist
    
    def get_var_value(self, var):
        """
        Returns the value of a specific variable from the list.

        :param var: Variable name (key in the dictionary).
        :return: Variable value.
        """
        return self.varlist[var]
    
    def clean_type(self, var):
        """
        Gets the variable type name in a clean format (without 'class').

        :param var: Variable name.
        :return: String with the type name (e.g., 'str', 'int').
        """
        var_type = str(type(self.varlist[var]))
        result = var_type.split("'")[1]
        return result

    def format_time(self, seconds, lang="en"):
        """
        Formats the number of seconds into a human-readable time string (e.g., '2 days').

        :param seconds: Time in seconds.
        :param lang: Output language ("en" or "uk"). Defaults to "en".
        :return: Formatted time string.
        """
        units = [
            ("year", 365 * 24 * 60 * 60),
            ("month", 30 * 24 * 60 * 60),
            ("week", 7 * 24 * 60 * 60),
            ("day", 24 * 60 * 60),
            ("hour", 60 * 60),
            ("minute", 60),
            ("second", 1)
        ]

        if lang == "uk":
            endings = {
                "second": ["секунда", "секунди", "секунд"],
                "minute": ["хвилина", "хвилини", "хвилин"],
                "hour": ["година", "години", "годин"],
                "day": ["день", "дня", "днів"],
                "week": ["тиждень", "тижня", "тижнів"],
                "month": ["місяць", "місяця", "місяців"],
                "year": ["рік", "роки", "років"]
            }

        else:
            endings = {
                "second": ["second", "seconds", "seconds"],
                "minute": ["minute", "minutes", "minutes"],
                "hour": ["hour", "hours", "hours"],
                "day": ["day", "days", "days"],
                "week": ["week", "weeks", "weeks"],
                "month": ["month", "months", "months"],
                "year": ["year", "years", "years"]
            }

        for unit, duration in units:
            if seconds >= duration:
                number = seconds // duration
                if 11 <= number % 100 <= 19:
                    form = endings[unit][2]
                else:
                    last_digit = number % 10
                    if last_digit == 1:
                        form = endings[unit][0]
                    elif 2 <= last_digit <= 4:
                        form = endings[unit][1]
                    else:
                        form = endings[unit][2]
                return f"{number} {form}"
