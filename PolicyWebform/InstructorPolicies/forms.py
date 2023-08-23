from django import forms
from .models import DocumentData

class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentData
        fields = ['InstructorName', 'CourseNameSection', 'OfficeLocation', 'Phone', 'Email', 'OfficeHours', 'FinalExamDate', 'FinalExamTime', 'Textbook', 'AppropriateBehavior', 'Assessments', 'GradingScale', 'LateWork', 'ExtraCredit', 'FinalExamPolicy', 'RequiredMaterials', 'SuggestedMaterials', 'CourseFees', 'GroupWork', 'PreviousWork', 'ScholasticHonesty', 'AttendancePolicy', 'CommunicationPolicy', 'AppropriateTechnologyUse', 'PersonalResponsibility', 'StandardsForWrittenWork', 'ComputerConsiderations', 'OnlineLearningPlatform', 'TeachingPhilosophy']
        