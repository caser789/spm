class Transaction(object):

    def to_dict(self):
        pass

    def __repr__(self):
        pass

    @classmethod
    def create(cls):
        return cls()

    def update(self):
        pass

    def expire(self):
        pass

    def cancel(self):
        pass

    def create_provision(self):
        pass
