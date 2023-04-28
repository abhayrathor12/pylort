from django.db import models


class courses(models.Model):
    name=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name
    
    

class Duration(models.Model):
    duration=models.IntegerField()


    def __str__(self) -> str:
        return str(self.duration)


class Students(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    cour=models.ForeignKey(courses,on_delete=models.CASCADE)
    fees=models.IntegerField(default=50)
    phone=models.IntegerField()
    dur=models.ForeignKey(Duration,on_delete=models.CASCADE)
    joined_date=models.DateField()



    def __str__(self) -> str:
        return "%s %s %s "%(self.first_name,self.last_name,self.cour)


    

