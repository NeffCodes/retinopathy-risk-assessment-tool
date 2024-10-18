from django.db import models

class PositionChoices(models.TextChoices):
    LEFT = "left", "Left"
    RIGHT = "right", "Right"

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
