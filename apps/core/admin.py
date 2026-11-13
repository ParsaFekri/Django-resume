from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import slugify
from .models import (
    HeroSection, About, SocialLink, Skill, SkillIcon
    )

def image_preview(obj, field_name, width=60, height=60, border_radius=0):
    # این تابع یک هلپر است که در متد های مختلف قابل استفاده است و برای ساخت پیشنمایش بند انگشتی یک فیلد تصویری استفاده میشود در پنل ادمین
    field = getattr(obj, field_name, None)  # تابع داخلی پایتون است که یک فیلد و آبجکت را میگیرد و در آین مثال فیلد تصویر را از آبجکت بگیرد
    
    if field:
        return format_html(
            '<img src="{}" style="width:{}px; height:{}px; border-radius:{}px; object-fit:cover;">',
            field.url, width, height, border_radius
        )
    return format_html(
        '<span style="color:red;"> - </span>'
    )

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'job_title', 'avatar_preview']  # در این قسمت ستون هایی در پنل ادمین نمایش داده میشود که میتواند نام فیلد باشد مثل دوتای اول و میتواند تابع باشد مثل سومین
    
    readonly_fields = ['avatar_preview_field']   # فیلد هایی که اینجا نوشته بشن قابل ویرلیش در پنل ادمین نیستن و فقط مشاهده میشوند و برای پیش نمایش تصویر استفاده میشود و کاربر میتواند اواار غعلی را ببیند بدون ذخیره مخجدد
    
    # برای گروه بندی فیلد ها در فرم ویرایش
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields':('name', 'job_title', 'button_text'),
        }),
        ('فایل ها',{
            'fields':('avatar', 'avatar_preview_field', 'resume_file'),
        })
    )
    
    def avatar_preview(self, obj):
        return image_preview(obj, 'avatar', 50, 50, 5)
    
    avatar_preview.short_description = 'آواتار'
    
    
    def avatar_preview_field(self, obj):
        return image_preview(obj, 'avatar', 150, 200, 10)
    
    avatar_preview_field.short_description = 'پیش نمایش آواتار'
    
    
    def has_add_permission(self, request):
        '''
        برای جلوگیری از افزودن بیش از یک رکورد به جدول هیروسکشن
        این متد یکی از متد های مدل ادمین جنگو میباشد
        '''
        if HeroSection.objects.exists():
            return False
        # return True
        return super().has_add_permission(request= request)
    

'''
    با استتفاده از این لاین میتوانیم یکسری فرم های تودرتو برای بخش ویرایش یک مدل تعریف نماییم
    پنل ادمین دو مدل سوشیال لیننک و اسکیل را بتوانیم همزمان بدون نیاز به جابجایی بین صفحات ویرایش کنیم about مثلا در این مثال میخواهیم در فرم ویرایش مدل
    ردیف های جدول اینلاین شده به شکل فشرده نمایش میابد برای فیلد های کوتاه و جداول با تعداد فیلد زیاد TabularInline در روش
'''
class SocialLinkInline(admin.TabularInline):
    # هر اینلاین به یک مدل متصل میشود 
    model = SocialLink
    extra = 1  # تعداد ردیف های خالی برای افزودن رکورد جدید در اینجا یک ردیف خالی ایجاد میکند
    fields = ['name', 'icon', 'url', 'order']  # فیلد هایی که در جدول اینلاین نمایش داده میشود به ترتیب نوشتار همین لیست
    ordering = ['order']
        

class SkillIconInline(admin.TabularInline):
    model = SkillIcon
    extra = 1
    fields = ['icon_image', 'url']
    
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ['title', 'description', 'percentage', 'bg_color']
    show_change_link = True  # ایجاد یک لینک برای تغییر داد هر مهارت 

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'job_title', 'signature_preview']
    
    inlines = [SocialLinkInline, SkillInline] # about لضلفه کردن اینلاین هایی که در بالا تعریف کردیم به فرم ویرایش 
    
    fieldsets = (
        (
            'اطلاعات اصلی', {
                'fields': ('quote', 'description', 'job_title', 'name')
            }
        ),
        (
            'تصاویر', {
                'fields': ('signature', 'signature_preview_field', 'main_image', 'main_image_preview')
            }
        ),
    )
    
    readonly_fields = ['signature_preview_field', 'main_image_preview']
    
    def signature_preview(self, obj):
        return image_preview(obj, 'signature', 50, 50, 5)
            
    signature_preview.short_description = 'امضای دیجیتال'
    
    def signature_preview_field(self, obj):
        return image_preview(obj, 'signature', 80, 30, 5)
            
    signature_preview_field.short_description = 'پیش نمایش امضای دیجیتال'
    
    def main_image_preview(self, obj):
        return image_preview(obj, 'main_image', 50, 50, 5)
            
    main_image_preview.short_description = 'پیش نمایش عکس اصلی'
    
    def has_add_permission(self, request):
        if About.objects.exists():
            return False
        # return True
        return super().has_add_permission(request= request)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):

    # ستون‌های نمایش‌داده‌شده در جدول لیست ادمین
    # icon_preview یک متد سفارشی برای نمایش بندانگشتی آیکون است
    list_display = ['name', 'about', 'url', 'order', 'icon_preview']

    # ویرایش مستقیم فیلد order از داخل جدول لیست
    # (بدون نیاز به باز کردن صفحه‌ی ویرایش)
    # ⚠️ فیلد list_editable نباید اولین ستون list_display باشه
    list_editable = ['order']

    # فیلتر سایدبار ادمین بر اساس فیلد about
    # (کاربر می‌تونه رکوردها رو بر اساس About مربوطه فیلتر کنه)
    list_filter = ['about']

    # باکس جستجو روی فیلدهای name و url
    search_fields = ['name', 'url']

    # بهینه‌سازی کوئری ForeignKey
    # با JOIN گرفتن about در یک کوئری، از مشکل N+1 جلوگیری می‌شه
    list_select_related = ['about']

    # تعداد رکوردهای نمایش داده‌شده در هر صفحه (پیش‌فرض ۱۰۰)
    list_per_page = 20

    def icon_preview(self, obj):
        return image_preview(obj, 'icon', 30, 30)

    # عنوان ستون در هدر جدول ادمین
    icon_preview.short_description = 'آیکون'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'about', 'percentage', 'bg_color_preview']
    inlines = [SkillIconInline]
    # ویرایش مستقیم درصد از لیست
    list_editable = ['percentage']
    list_filter = ['about']
    search_fields = ['title', 'description']
    list_select_related = ['about']
    list_per_page = 20

    # نمایش رنگ پس‌زمینه به‌صورت مربع رنگی
    def bg_color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block; width:20px; height:20px; '
            'background:{}; border-radius:4px; border:1px solid #ccc;"></span>',
            obj.bg_color
        )
    bg_color_preview.short_description = 'رنگ'


@admin.register(SkillIcon)
class SkillIconAdmin(admin.ModelAdmin):
    list_display = ['skill', 'icon_preview', 'url']
    list_filter = ['skill']
    # جستجو با نام مهارت مرتبط
    search_fields = ['skill__title']
    list_select_related = ['skill']
    list_per_page = 20

    def icon_preview(self, obj):
        return image_preview(obj, 'icon_image', 30, 30)
    icon_preview.short_description = 'آیکون'