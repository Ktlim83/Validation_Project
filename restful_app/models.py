from __future__ import unicode_literals
from django.db import models

# manager class should always be above wanted class 
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors
    
    # FOR EMAIL VALIDATION with IMPORT NEEDED (suggested to use the variable globally and not to just 1 function)
    # "import re " = the regex module
    # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    #     if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
    #         errors['email'] = ("Invalid email address!")
    

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    
    def __str__(self):
        return f"{self.id} {self.title}"