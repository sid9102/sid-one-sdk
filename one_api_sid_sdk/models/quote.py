from .base_model import BaseModel


class Quote(BaseModel):
    def __init__(self, quote_data):
        super().__init__()
        self.id = quote_data["_id"]
        self.dialog = quote_data["dialog"]
        self.movie = quote_data["movie"]
        self.character = quote_data["character"]
