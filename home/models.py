from django.db import models

# Create your models here.

class contact(models.Model):
    username = models.CharField(max_length=122 , primary_key=True)
    password = models.CharField(max_length=9)
    score = models.FloatField(default=0.0)

    #def __str__(self):
        #return self.username

class cand_ans(models.Model):
    id = models.AutoField(primary_key=True)
    q_id = models.IntegerField()
    ques = models.TextField()
    ans = models.TextField()
    keywords_ans = models.TextField(null=True)

class ques_ans(models.Model):
    qa_id = models.IntegerField(primary_key=True)
    ques = models.TextField()
    ans = models.TextField(default=["x" , "y" , "z"] , null=True)

class cand_bank(models.Model):
    user = models.CharField(max_length=122 , null=True)
    id = models.AutoField(primary_key=True)
    q_id = models.IntegerField()
    ques = models.TextField()
    ans = models.TextField()
    keywords_ans = models.TextField(null=True)





