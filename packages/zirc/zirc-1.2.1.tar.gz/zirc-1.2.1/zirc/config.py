class IRCConfig(object):
    """
    Class for holding zIRC config infomation.
    
    >>> self.config = zirc.IRCConfig(nickname="IRCConfigTest")
    >>> self.connect(self.config)
    """
    def __init__(self, **c):
        self.dict = {"host": "irc.freenode.net",
                  "port": 6667,
                  "nickname": "my-zIRC-Bot",
                  "ident": "bot",
                  "realname": "zIRC Bot",
                  "channels": ["#zirc"],
                  "sasl_user": None,
                  "sasl_pass": None
                  }
        self.dict.update(c)

    def sterilise(self, method):
        return method(self.dict)

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value