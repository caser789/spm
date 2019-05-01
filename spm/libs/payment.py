class Payment(object):

    def __init__(self, pid):
        pass

    def to_dict(self):
        pass

    def __repr__(self):
        pass

    @staticmethod
    def next_id(self):
        pass

    @classmethod
    def create(cls):
        pass

    @classmethod
    def from_transaction(cls, tid, pid):
        pass

    @classmethod
    def list(cls):
        pass

    @classmethod
    def list_by_category(cls):
        pass

    @classmethod
    def list_by_transaction_id(cls, tid):
        pass

    @classmethod
    def list_ongoing_by_transaction_id(cls, tid):
        pass

    @classmethod
    def latest_from_transaction(cls):
        pass
