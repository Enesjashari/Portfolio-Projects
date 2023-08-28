from django.db import models

# Model representing an author.
class Author(models.Model):
    # The name of the author.
    name = models.CharField(max_length=100)

# Model representing a category.
class Category(models.Model):
    # The name of the category.
    name = models.CharField(max_length=100)

# Model representing a paper.
class Paper(models.Model):
    # The title of the paper.
    title = models.CharField(max_length=200, default=' ')
    
    # The abstract of the paper.
    abstract = models.TextField(default=' ')
    
    # Authors associated with the paper.
    authors = models.ManyToManyField(Author, default=' ')
    
    # Return the title of the paper when the object is displayed as a string.
    def __str__(self):
        return self.title


# Model representing student data related to a paper.
class StudentData(models.Model):
    # Identifier for the student data.
    id = models.CharField(max_length=1000, primary_key=True, default=' ')
    # The name associated with the data.
    name = models.CharField(max_length=1000, default=' ')
    # Authors of the paper associated with the data.
    authors = models.CharField(max_length=1000, default=' ')
    # Title of the paper.
    title = models.CharField(max_length=1000, default=' ')
    # Comments related to the data.
    comments = models.CharField(max_length=1000, default=' ')
    # Reference to the journal.
    journal_ref = models.CharField(max_length=1000, default=' ')
    # Digital Object Identifier (DOI) for the paper.
    doi = models.CharField(max_length=1000, default=' ')
    # Report number associated with the paper.
    report_no = models.CharField(max_length=1000, default=' ')
    # Categories associated with the data.
    categories = models.CharField(max_length=1000, default=' ')
    # License information for the paper.
    license = models.CharField(max_length=1000, default=' ')
    # Abstract of the paper.
    abstract = models.CharField(max_length=1000, default=' ')
    # Parsed author information.
    authors_parsed = models.CharField(max_length=1000, default=' ')

    # Note: The 'categories' and 'publication_date' fields are commented out,
    # likely indicating they were considered but not yet implemented.

    # categories = models.ManyToManyField(Category)
    # publication_date = models.DateField()