class FakeNewsData:
    def store_claim(self, claim):
        self.claim_tokens = list()
        words = claim.split()
        for word in words:
            if len(word) > 3:
                self.claim_tokens.append(word)
        self.claim_tokens.sort()
    
    def store_result(self, result):
<<<<<<< HEAD
        print("Result=" + result.upper())
        if result.upper() == "TRUE":
            self.result = "True"
        elif result.upper() == "FALSE":
            self.result = "False"
        else:
            self.result = "Maybe"
=======
        result = result.strip().lower()
        if result == "true":
            self.claim_result = "True"
        elif result == "false":
            self.claim_result = "False"
        else:
            self.claim_result = "Maybe"
>>>>>>> 412b9fd... Added handler for FactCheckIndia and an in memory store to save results

    def store_url(self, source_url):
        self.source_url = source_url

    def print(self):
<<<<<<< HEAD
        print(self.result)
=======
        print(self.claim_result)
>>>>>>> 412b9fd... Added handler for FactCheckIndia and an in memory store to save results
        print(self.source_url)
        print(self.claim_tokens)

    def __init__(self, claim, result, source_url):
        self.store_result(result)
        self.store_claim(claim)
        self.store_url(source_url)

class InMemoryDBInterface:
    def __init__(self):
        self.db = list()

    def write(self, claim, result, source_url):
        data = FakeNewsData(claim, result, source_url)
        data.print()
        self.db.append(data)

    def get_items(self):
        return self.db

