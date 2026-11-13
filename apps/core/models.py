from django.db import models
from django.utils.text import slugify

class HeroSection(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    job_title = models.CharField(max_length=200, verbose_name='عنوان شغل')
    button_text = models.CharField(max_length=100, verbose_name='متن دکمه')
    resume_file = models.FileField(upload_to='hero/resume/', verbose_name='رزومه', blank=True, null=True)
    avatar = models.ImageField(upload_to='hero/', verbose_name='تصویر آواتار')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='اطلاعات شخصی'
        verbose_name_plural='اطلاعات شخصی'
        

class About(models.Model):
    quote = models.CharField(max_length=100, verbose_name='نقل قول')
    description = models.TextField(verbose_name='توضیحات درباره من')
    job_title = models.CharField(max_length=200, verbose_name='عنوان شغل')
    name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    signature = models.ImageField(upload_to='about/', verbose_name='امضای دیجیتال')
    main_image = models.ImageField(upload_to='about/', verbose_name='عکس اصلی درباره من')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='درباره من'
        verbose_name_plural='درباره من'
        
'''
on_delete توضیحات 
حذف شود چه اتفاقی برای سوشیال لینک های آن رخ دهد about هنگامی که رکوردی از
به شکل خودکار حذف میشود n تمام رکورد های متناظر آن در جول سمت  aboutبا حذف هر رکورد cascade حالت
'''
# About مدل شبکه های اجتماعی مربوط به مدل 
class SocialLink(models.Model):
    about = models.ForeignKey(
    About, # وصل میشود about مدل مقصد به عبارتی دیگر هرشبکه اجتماعی به یک 
    on_delete= models.CASCADE,
    related_name= 'social_links', # میباشد About برای دسترسی معکوس استفاده میشود یعنی یک نام از سمت 
    verbose_name='درباره'
    )
    name = models.CharField(max_length=50, verbose_name='نام شبکه اجتماعی')
    icon = models.ImageField(upload_to='about/social/', verbose_name='آیکون شبکه اجتماعی')
    url = models.URLField(verbose_name='لینک شبکه اجتماعی')
    order = models.PositiveIntegerField(default=0, verbose_name='تزتیب نمایش')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='شبکه اجتماعی'
        verbose_name_plural='شبکه های اجتماعی'
        ordering=['order']
        

# About مدل مهارت ها مربوط به مدل 
class Skill(models.Model):
    about = models.ForeignKey(
        About, # وصل میشود about مدل مقصد به عبارتی دیگر هرشبکه اجتماعی به یک 
        on_delete= models.CASCADE,
        related_name= 'skills', # میباشد About برای دسترسی معکوس استفاده میشود یعنی یک نام از سمت 
        verbose_name='درباره'
        )
    title = models.CharField(max_length=100, verbose_name='عنوان مهارت')
    description = models.TextField(verbose_name='توضیحات')
    percentage = models.PositiveIntegerField(verbose_name='درصد تسلط')
    bg_color = models.CharField(max_length=30, verbose_name='رنگ پس زمینه')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='مهارت'
        verbose_name_plural='مهارت ها'
        
# Skill آیکون های مربوط به هر مهارت مربوط به مدل 
class SkillIcon(models.Model):
    skill = models.ForeignKey(
        Skill,
        on_delete= models.CASCADE,
        related_name='icons',
        verbose_name='توانایی'
    )
    icon_image = models.ImageField(upload_to='about/skill_icons/', verbose_name='تصویر آیکون')
    url = models.URLField(blank=True, null=True, verbose_name='لینک(اختیاری)')
    
    def __str__(self):
        return f'آیکون  {self.skill.title}'

    class Meta:
        verbose_name='آیکون مهارت'
        verbose_name_plural='آیکون مهارت ها'