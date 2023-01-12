class WeatherException(Exception):
    """Define class for custom weather exception"""

    def __init__(self, *args):
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Weather download exception, {0} '.format(self.message)
        else:
            return 'Weather exception has been raised'
