"""
Sites
"""

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify as djslugify
from django.contrib.sitemaps import ping_google

LANGUAGES = (
    ('Other', 'Other'),
    ('Mandarin', 'Mandarin'),
    ('Spanish', 'Spanish'),
    ('English', 'English'),
    ('Hindi', 'Hindi'),
    ('Arabic', 'Arabic'),
    ('Portuguese', 'Portuguese'),
    ('Bengali', 'Bengali'),
    ('Russian', 'Russian'),
    ('Japanese', 'Japanese'),
    ('Punjabi', 'Punjabi'),
    ('German', 'German'),
    ('Javanese', 'Javanese'),
    ('Wu', 'Wu'),
    ('Malay', 'Malay'),
    ('Telugu', 'Telugu'),
    ('Vietnamese', 'Vietnamese'),
    ('Korean', 'Korean'),
    ('French', 'French'),
    ('Marathi', 'Marathi'),
    ('Tamil', 'Tamil'),
    ('Urdu', 'Urdu'),
    ('Turkish', 'Turkish'),
    ('Italian', 'Italian'),
    ('Yue', 'Yue'),
    ('Thai', 'Thai'),
    ('Gujarati', 'Gujarati'),
    ('Jin', 'Jin'),
    ('Southern', 'Southern'),
    ('Persian', 'Persian'),
    ('Polish', 'Polish'),
    ('Pashto', 'Pashto'),
    ('Kannada', 'Kannada'),
    ('Xiang', 'Xiang'),
    ('Malayalam', 'Malayalam'),
    ('Sundanese', 'Sundanese'),
    ('Hausa', 'Hausa'),
    ('Odia', 'Odia'),
    ('Burmese', 'Burmese'),
    ('Hakka', 'Hakka'),
    ('Ukrainian', 'Ukrainian'),
    ('Bhojpuri', 'Bhojpuri'),
    ('Tagalog/Filipino', 'Tagalog/Filipino'),
    ('Yoruba', 'Yoruba'),
    ('Maithili', 'Maithili'),
    ('Uzbek', 'Uzbek'),
    ('Sindhi', 'Sindhi'),
    ('Amharic', 'Amharic'),
    ('Fula', 'Fula'),
    ('Romanian', 'Romanian'),
    ('Oromo', 'Oromo'),
    ('Igbo', 'Igbo'),
    ('Azerbaijani', 'Azerbaijani'),
    ('Awadhi', 'Awadhi'),
    ('Gan', 'Gan'),
    ('Cebuano', 'Cebuano'),
    ('Dutch', 'Dutch'),
    ('Kurdish', 'Kurdish'),
    ('Serbo-Croatian', 'Serbo-Croatian'),
    ('Malagasy', 'Malagasy'),
    ('Saraiki', 'Saraiki'),
    ('Nepali', 'Nepali'),
    ('Sinhalese', 'Sinhalese'),
    ('Chittagonian', 'Chittagonian'),
    ('Zhuang', 'Zhuang'),
    ('Khmer', 'Khmer'),
    ('Turkmen', 'Turkmen'),
    ('Assamese', 'Assamese'),
    ('Madurese', 'Madurese'),
    ('Somali', 'Somali'),
    ('Marwari', 'Marwari'),
    ('Magahi', 'Magahi'),
    ('Haryanvi', 'Haryanvi'),
    ('Hungarian', 'Hungarian'),
    ('Chhattisgarhi', 'Chhattisgarhi'),
    ('Greek', 'Greek'),
    ('Chewa', 'Chewa'),
    ('Deccan', 'Deccan'),
    ('Akan', 'Akan'),
    ('Kazakh', 'Kazakh'),
    ('Northern', 'Northern'),
    ('Sylheti', 'Sylheti'),
    ('Zulu', 'Zulu'),
    ('Czech', 'Czech'),
    ('Kinyarwanda', 'Kinyarwanda'),
    ('Dhundhari', 'Dhundhari'),
    ('Haitian', 'Haitian'),
    ('Eastern', 'Eastern'),
    ('Ilocano', 'Ilocano'),
    ('Quechua', 'Quechua'),
    ('Kirundi', 'Kirundi'),
    ('Swedish', 'Swedish'),
    ('Hmong', 'Hmong'),
    ('Shona', 'Shona'),
    ('Uyghur', 'Uyghur'),
    ('Hiligaynon', 'Hiligaynon'),
    ('Mossi', 'Mossi'),
    ('Xhosa', 'Xhosa'),
    ('Belarusian', 'Belarusian'),
    ('Balochi', 'Balochi'),
    ('Konkani', 'Konkani'),
)

OS = (
    ('Other', 'Other'),
    ('Unix', 'Unix'),
    ('BSD', 'BSD'),
    ('OS X', 'OS X'),
    ('Linux', 'Linux'),
    ('Windows', 'Windows'),
    ('Solaris', 'Solaris'),
    ('eComStation', 'eComStation'),
    ('OpenVMS', 'OpenVMS'),
    ('AIX', 'AIX'),
    ('IBM', 'IBM'),
    ('z/OS', 'z/OS'),
    ('HP-UX', 'HP-UX'),
)

WEBSERVERS = (
    ('Other', 'Other'),
    ('HFS', 'HFS'),
    ('IIS', 'IIS'),
    ('Monkey', 'Monkey'),
    ('Jexus', 'Jexus'),
    ('Wakanda', 'Wakanda'),
    ('AOL', 'AOL'),
    ('Apache', 'Apache'),
    ('IBM HTTP', 'IBM HTTP'),
    ('Mongoose', 'Mongoose'),
    ('nginx', 'nginx'),
    ('Oracle', 'Oracle'),
    ('Chaussette', 'Chaussette'),
    ('CherryPy', 'CherryPy'),
    ('Tornado', 'Tornado'),
    ('mod_wsgi', 'mod_wsgi'),
    ('Nginx WSGI', 'Nginx WSGI'),
    ('PyWX ', 'PyWX '),
    ('Google', 'Google'),
    ('Amazon', 'Amazon'),
)

DATABASES = (
    ('Other', 'Other'),
    ('Oracle', 'Oracle'),
    ('MySQL', 'MySQL'),
    ('MSSQL', 'MSSQL'),
    ('Microsoft SQL Server', 'Microsoft SQL Server'),
    ('PostgreSQL', 'PostgreSQL'),
    ('MongoDB', 'MongoDB'),
    ('DB2', 'DB2'),
    ('Cassandra', 'Cassandra'),
    ('Microsoft Access', 'Microsoft Access'),
    ('SQLite', 'SQLite'),
    ('XmlDatabases', 'XmlDatabases'),
    ('PostgreSQL', 'PostgreSQL'),
    ('Google', 'Google'),
    ('Amazon', 'Amazon'),
)

METHOD = (
    ('Other', 'Other'),
    ('Google App Engine', 'Google App Engine'),
    ('Gunicorn', 'Gunicorn'),
    ('mod_python', 'mod_python'),
    ('mod_wsgi', 'mod_wsgi'),
    ('FastCGI', 'FastCGI'),
    ('Django Development Server', 'Django Development Server'),
    ('Simple CGI (scgi)', 'Simple CGI (scgi)'),
    ('Tornado', 'Tornado'),
    ('wsgi', 'wsgi'),
    ('uWSGI', 'uWSGI'),
    ('PAAS (Heroku, GAE, Gondor, etc', 'PAAS (Heroku, GAE, Gondor, etc'),
)

PYTHONVERSIONS = (
    ('Other', 'Other'),
    ('Python 2.0.1', 'Python 2.0.1'),
    ('Python 2.2.0', 'Python 2.2.0'),
    ('Python 2.1.3', 'Python 2.1.3'),
    ('Python 2.2.1', 'Python 2.2.1'),
    ('Python 2.2.2', 'Python 2.2.2'),
    ('Python 2.4.2', 'Python 2.4.2'),
    ('Python 2.6.0', 'Python 2.6.0'),
    ('Python 2.7.0', 'Python 2.7.0'),
    ('Python 2.7.10', 'Python 2.7.10'),
    ('Python 2.7.12', 'Python 2.7.12'),
    ('Python 3.2.0', 'Python 3.2.0'),
    ('Python 3.3.1', 'Python 3.3.1'),
    ('Python 3.3.2', 'Python 3.3.2'),
    ('Python 3.4.0', 'Python 3.4.0'),
    ('Python 3.5.0', 'Python 3.5.0'),
    ('Python 3.5.1', 'Python 3.5.1'),
    ('Python 3.5.2', 'Python 3.5.2'),
)

FRAMEWORK = (
    ('Other', 'Other'),
    ('Django', 'Django'),
    ('TurboGears', 'TurboGears'),
    ('web2py', 'web2py'),
    ('CubicWeb', 'CubicWeb'),
    ('Django-hotsauce', 'Django-hotsauce'),
    ('Giotto', 'Giotto'),
    ('Grok', 'Grok'),
    ('Pylons', 'Pylons'),
    ('Reahl', 'Reahl'),
    ('wheezy.web', 'wheezy.web'),
    ('Zope2', 'Zope2'),
    ('Glashammer', 'Glashammer'),
    ('Kiss.py', 'Kiss.py'),
    ('Lino', 'Lino'),
    ('Nagare', 'Nagare'),
    ('Pylatte', 'Pylatte'),
    ('Tornado', 'Tornado'),
    ('watson-framework', 'watson-framework'),
    ('webapp2', 'webapp2'),
    ('WebCore', 'WebCore'),
    ('web.py', 'web.py'),
    ('Webware for Python', 'Webware for Python'),
    ('Werkzeug', 'Werkzeug'),
    ('WHIFF', 'WHIFF'),
    ('Bottle', 'Bottle'),
    ('CherryPy', 'CherryPy'),
    ('Flask', 'Flask'),
    ('Hug', 'Hug'),
    ('Pyramid', 'Pyramid'),
)

@python_2_unicode_compatible
class Site(models.Model):
    """
    Site
    """
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    title               = models.CharField(max_length=25, null=False, blank=False)
    web_site_address    = models.URLField(max_length=150, null=False, blank=False)
    slug                = models.SlugField()
    img                 = models.ImageField(upload_to='sites/%Y/%m/%d')
    description         = models.TextField(null=False, blank=False)
    language            = models.CharField(max_length=25, choices=LANGUAGES, null=False, blank=False)
    tags                = models.CharField(max_length=40, null=False, blank=False, help_text='Please , separate')
    source_code_address = models.URLField(max_length=150, null=True, blank=True)
    framework           = models.CharField(max_length=25, choices=FRAMEWORK, null=False, blank=False)
    operating_system    = models.CharField(max_length=25, choices=OS, null=False, blank=False)
    webserver           = models.CharField(max_length=25, choices=WEBSERVERS, null=False, blank=False)
    database            = models.CharField(max_length=25, choices=DATABASES, null=False, blank=False)
    method              = models.CharField(max_length=25, choices=METHOD, null=False, blank=False)
    python_version      = models.CharField(max_length=25, choices=PYTHONVERSIONS, null=False, blank=False)
    pub_date            = models.DateTimeField(auto_now_add=True)
    views               = models.PositiveSmallIntegerField(default=0)
    enable              = models.BooleanField(default=False, blank=True)

    def __str__(self):
        """
        :return:
        """
        return self.user.username

    def get_absolute_url(self):
        """
        :return:
        """
        return '/detail/' + self.slug

    def save(self, *args, **kwargs):
        """
        Slug save
        """
        super(Site, self).save(*args, **kwargs)
        if not self.slug:
            slug = self.web_site_address
            slug = slug.replace(u'http://www', '')
            slug = slug.replace(u'https://www', '')
            slug = slug.replace(u'http://', '')
            slug = slug.replace(u'https://', '')
            slug = slug.replace(u'www', '')
            self.slug = djslugify(slug + "-" + str(self.id))
            self.save()
        try:
            ping_google()
        except Exception:
            pass

    def view_count(self):
        """
        :return:
        """
        self.views += 1
        self.save()

    def tags_as_list(self):
        return self.tags.split(',')