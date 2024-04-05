from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # 'detail is refering to the name of the url we want to redirect to'
        # path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
        return reverse('detail', kwargs={'finch_id': self.id})
        # cat_id refers to the name of the param
        # refer to the route above, and the value,
        # self.id, refers to the cat that was just created
        # on the post request

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    )

    # create a cat_id Foreign Key in psql
    # we don't put the id, django does automatically
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
