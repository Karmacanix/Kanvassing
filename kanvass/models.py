from django.db import models
from django.contrib.auth import get_user_model
from tree_queries.models import TreeNode
from tree_queries.query import TreeQuerySet


UserModel = get_user_model()


# Create your models here.
class KanvassQuerySet(TreeQuerySet):
    def active(self):
        return self.filter(is_active=True)

class Kanvass(TreeNode):
    name = models.CharField(max_length=120)
    start_date = models.DateField(verbose_name="Start")
    end_date = models.DateField(verbose_name="End")
    is_active = models.BooleanField(default=True)
    sponsor = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    objects = KanvassQuerySet.as_manager()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return f"/kanvass/{self.pk}/"
    
    def __str__(self):
        return self.name

