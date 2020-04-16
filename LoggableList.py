class LoggableList(list, Loggable):
    def append(self, elm):
        super(LoggableList, self).append(elm)
        self.log(elm)