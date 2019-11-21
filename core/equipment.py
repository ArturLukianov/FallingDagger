class Equipment:
    def __init__(self, body=None, head=None, left_hand=None, right_hand=None, legs=None):
        self.body = body
        self.head = head
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.legs = legs

    def sum_stats(self):
        return sum([self.body, self.head, self.legs, self.left_hand, self.right_hand])
