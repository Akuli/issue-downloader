class Book(models.Model):
    author = models.ForeignKey(Author, null=True)
