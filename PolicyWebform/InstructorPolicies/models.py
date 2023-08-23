from django.db import models

# Create your models here.
class DocumentData(models.Model):
    InstructorName = models.CharField(max_length=100)
    CourseNameSection = models.CharField(max_length=100)
    OfficeLocation = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    OfficeHours = models.CharField(max_length=100)
    FinalExamDate = models.CharField(max_length=100)
    FinalExamTime = models.CharField(max_length=100)
    Textbook = models.CharField(max_length=100)
    AppropriateBehavior = models.CharField(max_length=1000)
    Assessments = models.CharField(max_length=1000)
    GradingScale = models.CharField(max_length=100)
    LateWork = models.CharField(max_length=1000)
    ExtraCredit = models.CharField(max_length=1000)
    FinalExamPolicy = models.CharField(max_length=1000)
    RequiredMaterials = models.CharField(max_length=1000)
    SuggestedMaterials = models.CharField(max_length=1000)
    CourseFees = models.CharField(max_length=1000)
    GroupWork = models.CharField(max_length=1000)
    PreviousWork = models.CharField(max_length=1000)
    ScholasticHonesty = models.CharField(max_length=1000)
    AttendancePolicy = models.CharField(max_length=1000)
    CommunicationPolicy = models.CharField(max_length=1000)
    AppropriateTechnologyUse = models.CharField(max_length=1000)
    PersonalResponsibility = models.CharField(max_length=1000)
    StandardsForWrittenWork = models.CharField(max_length=1000)
    ComputerConsiderations = models.CharField(max_length=1000)
    OnlineLearningPlatform = models.CharField(max_length=1000)
    TeachingPhilosophy = models.CharField(max_length=1000)