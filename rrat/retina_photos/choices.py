from django.db import models

class PositionChoices(models.TextChoices):
    LEFT = "os", "OS"
    RIGHT = "od", "OD"

class StatusChoices(models.TextChoices):
    UNPROCESSED = 'unprocessed', 'Unprocessed'
    PENDING = 'pending', 'Pending'
    DONE = 'done', 'Done'

class PrognosisChoices(models.TextChoices):
    NORMAL = 'normal', 'Normal / No DR'
    MILD = 'mild', 'Mild'
    MODERATE = 'moderate', 'Moderate'
    SEVERE = 'severe', 'Severe'
    PROLIFERATIVE = 'proliferative', 'Proliferative'
