import json

from django.db import models

class Grid(models.Model):
    num_columns = models.IntegerField()
    num_rows = models.IntegerField()
    grid = models.CharField(max_length = 200)

    # grid is converted to string using json
    # Note: if using PostgreSQL use djnago.contrib.JSONField()
    def set_grid(self, input_grid):
        self.grid = json.dumps(input_grid)

    def get_grid(self, input_grid):
        return json.loads(self.grid)
