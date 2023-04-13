from .base_model import BaseModel


class Movie(BaseModel):
    def __init__(self, movie_data: dict):
        self.id = movie_data["_id"]
        self.name = movie_data["name"]
        self.runtime_in_minutes = movie_data["runtimeInMinutes"]
        self.budget_in_millions = movie_data["budgetInMillions"]
        self.box_office_revenue_in_millions = movie_data["boxOfficeRevenueInMillions"]
        self.academy_award_nominations = movie_data["academyAwardNominations"]
        self.academy_award_wins = movie_data["academyAwardWins"]
        self.rotten_tomatoes_score = movie_data["rottenTomatoesScore"]

    def __str__(self):
        return f"{self.name} ({self.id})"
