# LIBRARIES
from django.db import models
from django.utils import timezone
# Importing the validators.
from django.core.validators import FileExtensionValidator
from custom_validators.validators import validate_file_size

# CLASSES
# Create your models here.

# Creating a data class called MetaDescription to control how objects will be created/stored in the database.
class MetaDescription(models.Model):
    text = models.TextField(max_length=500, null=False, blank=False, default="About Doga Ege Ozden's current position, status, job fields that he is interested with, job experiences and education.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.")

    class Meta:
        verbose_name_plural = "Meta Description"

# Creating a data class called AboutCurrentPosition to control how objects will be created/stored in the database.
class AboutCurrentPosition(models.Model):
    text = models.TextField(max_length=350, null=False, blank=False, default="A self taught programmer seeking for a full time position, where he can utilize his skills and knowledge in web development field.", help_text="Explain what are dealing with currently as the third person.<br><strong>Ex: </strong>A self taught programmer seeking for a full time position, where he can utilize his skills and knowledge in web development field.")

    class Meta:
        verbose_name_plural = "About Current Position"

# Creating a data class called Resume to control how objects will be created/stored in the database.
class Resume(models.Model):
    field_name = models.CharField(max_length=300, null=False, blank=False, verbose_name="Field Name", default="Full-Stack Web Developer", help_text="Write the name of the field which you prepared resume for.")
    
    resume_name = models.CharField(max_length=300, null=False, blank=False, verbose_name="Resume Name", default="Full-Stack Web Developer", help_text="Give your resume a name.<br><strong>Note: </strong>This name will be used to name the object.")
    
    def upload_resume_file(self, field_attname):
        """A function which generates dynamic paths for resume files."""
        return f'resumes/{self.field_name}/{self.file}'

    file = models.FileField(null=False, blank=False, default="/assets/resume_dogaegeozden_full_stack_web_developer.pdf", upload_to=upload_resume_file, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file type is pdf.</li><li>You can use the Libre Writer to convert word files to pdf files.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['pdf']), validate_file_size],)

    class Meta:
        verbose_name_plural = "Resumes"

    def __str__(self):
        """String for representing the Model object."""
        return self.resume_name

# Creating a data class called Experience to control how objects will be created/stored in the database.
class Experience(models.Model):
    job_title = models.CharField(max_length=300, null=False, blank=False, verbose_name="Job Title", default="Job Title", help_text="Write the job title of your experience.")# max max_length = required
    
    company_name = models.CharField(max_length=300, null=False, blank=False, verbose_name="Company Name", default="Company", help_text="Write the name of the company that you worked for.")# max max_length = required
    
    work_Status = (
        ('p', 'Present'),
        ('c', 'Complete'),
    )
    
    start_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="Start Date", help_text="Please use the fallowing format: YYYY-MM-DD")
    
    end_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="End Date", help_text="Please use the fallowing format: YYYY-MM-DD")
    
    working_status = models.CharField(
        max_length=1,
        choices=work_Status,
        blank=False,
        null=False,
        default='n',
        help_text='Working status', 
        verbose_name="Working Status",)
    
    text = models.TextField(max_length=550, blank=True, null=True, help_text="Write a short job description.")
    
    header = models.CharField(max_length=200, null=True, blank=True, help_text="Write a header which will be located on top of the list item. Ex: Summary")
    
    list_item_1 = models.CharField(max_length=500, null=True, blank=True, verbose_name="List Item 1", help_text="Write a task that you completed during your experience.")
   
    list_item_2 = models.CharField(max_length=500, null=True, blank=True, verbose_name="List Item 2", help_text="Write a task that you completed during your experience.")
   
    list_item_3 = models.CharField(max_length=500, null=True, blank=True, verbose_name="List Item 3", help_text="Write a task that you completed during your experience.")
   
    list_item_4 = models.CharField(max_length=500, null=True, blank=True, verbose_name="List Item 4", help_text="Write a task that you completed during your experience.")
   
    list_item_5 = models.CharField(max_length=500, null=True, blank=True, verbose_name="List Item 5", help_text="Write a task that you completed during your experience.")
    
    def upload_experience_image_1(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        return f'experience/{self.company_name}/{self.img_1}'

    img_1 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_1, verbose_name="Experince Picture 1", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    
    def upload_experience_image_2(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        return f'experience/{self.company_name}/{self.img_2}'

    img_2 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_2, verbose_name="Experince Picture 2", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_3(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        return f'experience/{self.company_name}/{self.img_3}'
 
    img_3 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_3, verbose_name="Experince Picture 3", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_4(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        return f'experience/{self.company_name}/{self.img_4}'

    img_4 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_4, verbose_name="Experince Picture 4", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_5(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        return f'experience/{self.company_name}/{self.img_5}'

    img_5 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_5, verbose_name="Experince Picture 5", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_6(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        return f'experience/{self.company_name}/{self.img_6}'

    img_6 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_6, verbose_name="Experince Picture 6", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_7(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        return f'experience/{self.company_name}/{self.img_7}'

    img_7 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_7, verbose_name="Experince Picture 7", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_8(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        return f'experience/{self.company_name}/{self.img_8}'

    img_8 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_8, verbose_name="Experince Picture 8", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_9(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        return f'experience/{self.company_name}/{self.img_9}'

    img_9 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_9, verbose_name="Experince Picture 9", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_experience_image_10(self, field_attname):
        """A function which generates dynamic paths for experience images."""
        return f'experience/{self.company_name}/{self.img_10}'

    img_10 = models.ImageField(null=True, blank=True, upload_to=upload_experience_image_10, verbose_name="Experince Picture 10", help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.6 width/height</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
   
    class Meta:
        verbose_name_plural = "Experiences"
   
    def __str__(self):
        """String for representing the Model object."""
        return self.job_title

# Creating a data class called Education to control how objects will be created/stored in the database.
class Education(models.Model):
    name = models.CharField(max_length=159, null=False, blank=False, verbose_name="School Name", help_text="Write the name of the college/university that you have graduated from.")
    
    city = models.CharField(max_length=50, null=True, blank=True, help_text="Write the name of the city where your college/university is located.")
    
    province = models.CharField(max_length=30, null=True, blank=True, help_text="Write the name of the province where your college/university is located.")
    
    start_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="Start Date", help_text="Please use the fallowing format: YYYY-MM-DD")
    
    end_date = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="End Date", help_text="Please use the fallowing format: YYYY-MM-DD")
    
    major = models.CharField(max_length=100, null=False, blank=False, verbose_name="Major", default="Business Administration and Marketing", help_text="Write your program's name.")
    
    diploma = models.TextField(max_length=150, null=True, blank=True, verbose_name="Diploma", default="Ontario Colleges Advanced Diploma", help_text="Write the name of the diploma that you received.")
    
    para = models.TextField(max_length=150, null=True, blank=True, verbose_name="Paragraph", help_text="Write a short paragraph that best describes your college/university.")
    
    alt = models.TextField(max_length=500, null=False, blank=False, verbose_name="ALT", default="Digital Marketing Specialist", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    
    class Meta:
        verbose_name_plural = "Education"
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

# Creating a data class called ResumePageVisit to control how objects will be created/stored in the database.
class ResumePageVisit(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
   
    class Meta:
        verbose_name_plural = 'Resume Page\'s Visit Information'
        ordering = ['-visit_time']

# Creating a data class called ResumeFileClicks to control how objects will be created/stored in the database.
class ResumeFileClicks(models.Model):
    resume_choice = models.CharField(max_length=500, null=True, blank=True, verbose_name="Visitor's Resume Choice")
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    
    class Meta:
        verbose_name_plural = 'Resume File Click Information'
        ordering = ['-click_time']