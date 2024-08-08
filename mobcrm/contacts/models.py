from django.db import models

class Contact(models.Model):
    CONTACT_TYPES = (
        ('non_prospect_individual', 'Non-Prospect Individual'),
        ('church', 'Church'),
        ('prospect', 'Prospect'),
    )
    
    STATE = (
        ('al', 'AL'), ('ak', 'AK'), ('az', 'AZ'), ('ar', 'AR'), ('ca', 'CA'),('co', 'CO'),('ct', 'CT'),('de', 'DE'), ('fl', 'FL'), ('ga', 'GA'),
        ('hi', 'HI'), ('id', 'ID'), ('il', 'IL'), ('in', 'IN'), ('ia', 'IA'), ('ks', 'KS'), ('ky', 'KY'), ('la', 'LA'), ('me', 'ME'),
        ('md', 'MD'), ('ma', 'MA'), ('mi', 'MI'), ('mn', 'MN'), ('ms', 'MS'), ('mo', 'MO'), ('mt', 'MT'), ('ne', 'NE'), ('nv', 'NV'),
        ('nh', 'NH'), ('nj', 'NJ'), ('nm', 'NM'), ('ny', 'NY'), ('nc', 'NC'), ('nd', 'ND'), ('oh', 'OH'), ('ok', 'OK'), ('or', 'OR'),
        ('pa', 'PA'), ('ri', 'RI'), ('sc', 'SC'), ('sd', 'SD'), ('tn', 'TN'), ('tx', 'TX'), ('ut', 'UT'), ('vt', 'VT'), ('va', 'VA'),
        ('wa', 'WA'), ('wv', 'WV'), ('wi', 'WI'), ('wy', 'WY'),('dc', 'DC')
    )
    
    PREFERRED_CONTACT_METHODS = (
        ('email', 'Email'),('phone', 'Phone'),('text', 'Text'),('Facebook Messanger', 'Facebook Messanger'),('other', 'Other')
    )
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='contact_images/', null=True, blank=True)
    preferred_contact_method = models.CharField(max_length=100, choices=PREFERRED_CONTACT_METHODS)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    type = models.CharField(max_length=100, choices=CONTACT_TYPES)  
    church = models.CharField(max_length=100, null=True, blank=True)  
    street_address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=2, choices=STATE, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    date_created = models.DateField(null=True, blank=True)
    date_last_updated = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Prospect(Contact):
    MARITAL_STATUS = (
        ('single', 'Single'),('married', 'Married'),('divorced', 'Divorced'),('widowed', 'Widowed'),('separated', 'Separated'), ('unknown', 'Unknown'),
    )
    
    COLOR = (
        ('red', 'Red'),('yellow', 'Yellow'),('blue', 'Blue'),('green', 'Green'),('unknown', 'Unknown'),
    )
    
    INDIVIDUAL_PIPELINE = (
        ('unknown', 'Unknown'), ('rejected', 'Rejected'), ('contacted','Contacted'), ('mission vision', 'Mission Vision'),('conversations', 'Conversations'),
        ('potential recruit', 'Potential Recruit'),('recruit', 'Recruit'), ('applicant', 'Applicant'),('teammate', 'Teammate')
    )
    
    PRIORITY = (
        ('urgent', 'Urgent'),('high', 'High'), ('medium', 'Medium'), ('low', 'Low')
    )
    
    ASSIGNED_TO = (
        ('BILL JONES', 'BILL JONES'), ('JASON MODOMO', 'JASON MODOMO'), ('KEN KATAYAMA', 'KEN KATAYAMA'), ('MATTHEW RULE', 'MATTHEW RULE'),
        ('CHIP ATKINSON', 'CHIP ATKINSON'), ('RACHEL LIVELY', 'RACHEL LIVELY'), ('JIM BURCHEL', 'JIM BURCHEL'), ('JILL WALKER', 'JILL WALKER'),
        ('KARINA RAMPIN', 'KARINA RAMPIN'), ('UNASSIGNED', 'UNASSIGNED')        
    )
    
    SOURCE = (
        ('WEBFORM', 'WEBFORM'), ('INCOMING CALL', 'INCOMING CALL'), ('EMAIL', 'EMAIL'), ('SOCIAL MEDIA', 'SOCIAL MEDIA'),
        ('COLD CALL', 'COLD CALL'),('PERSPECTIVES', 'PERSPECTIVES'),('REFERAL', 'REFERAL'),('OTHER', 'OTHER'), ('UNKNOWN', 'UNKNOWN')
    )
    
    contact_ptr = models.OneToOneField(
        Contact, on_delete=models.CASCADE,
        parent_link=True,
        related_name='prospect_contact'
    )
    
    contact = models.ForeignKey(Contact, related_name='contacts', on_delete=models.CASCADE)
    virtuous = models.BooleanField(default=False)
    home_country = models.CharField(max_length=100, null=True, blank=True)
    spouse_recruit = models.BooleanField(default=False)
    marital_status = models.CharField(max_length=100, choices=MARITAL_STATUS, null=True, blank=True)
    color = models.CharField(max_length=100, choices=COLOR, null=True, blank=True)
    individual_pipeline = models.CharField(max_length=100, choices=INDIVIDUAL_PIPELINE, null=True, blank=True)
    priority = models.CharField(max_length=100, choices=PRIORITY, null=True, blank=True)
    assigned_to = models.CharField(max_length=100, choices=ASSIGNED_TO, null=True, blank=True)
    source = models.CharField(max_length=100, choices=SOURCE, null=True, blank=True)
    referred_by = models.CharField(max_length=100, null=True, blank=True)
    info_given = models.TextField(null=True, blank=True)
    desired_service = models.TextField(null=True, blank=True)
    reason_closed = models.TextField(null=True, blank=True)
    # contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date_closed = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return str(self.contact.last_name)
    
    class Meta:
        verbose_name = 'Prospect'
        verbose_name_plural = 'Prospects'

class Church(Contact):
    COLOR = (
        ('RED', 'RED'),('YELLOW', 'YELLOW'), ('BLUE', 'BLUE'),('GREEN', 'GREEN')
    )
    
    CHURCH_PIPELINE_CHOICES = (
        ('UNKNOWN', 'UNKNOWN'), ('COLD UNCONTACTED', 'COLD UNCONTACTED'), ('COLD CONTACTED', 'COLD CONTACTED'),
        ('REPEATED FOLLOWUP', 'REPEATED FOLLOWUP'), ('WARM UNCONTACTED', 'WARM UNCONTACTED'), ('WARM CONTACTED', 'WARM CONTACTED'),
        ('MET', 'MET'), ('MISSION VISION', 'MISSION VISION'), ('EN42', 'EN42')
    )
    
    PRIORITY = (
        ('URGENT', 'URGENT'), ('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')
    )
    
    ASSIGNED_TO_CHOICES = (
        ('BILL JONES', 'BILL JONES'), ('JASON MODOMO', 'JASON MODOMO'), ('KEN KATAYAMA', 'KEN KATAYAMA'), ('MATTHEW RULE', 'MATTHEW RULE'),
        ('CHIP ATKINSON', 'CHIP ATKINSON'), ('RACHEL LIVELY', 'RACHEL LIVELY'), ('JIM BURCHEL', 'JIM BURCHEL'), ('JILL WALKER', 'JILL WALKER'),
        ('KARINA RAMPIN', 'KARINA RAMPIN'), ('UNASSIGNED', 'UNASSIGNED')        
    )
    
    SOURCE = (
        ('WEBFORM', 'WEBFORM'), ('INCOMING CALL', 'INCOMING CALL'), ('EMAIL', 'EMAIL'), ('SOCIAL MEDIA', 'SOCIAL MEDIA'),
        ('COLD CALL', 'COLD CALL'),('PERSPECTIVES', 'PERSPECTIVES'),('REFERAL', 'REFERAL'),('OTHER', 'OTHER'), ('UNKNOWN', 'UNKNOWN')
    )
    
    contact_ptr = models.OneToOneField(
        Contact, on_delete=models.CASCADE,
        parent_link=True,
        related_name='church_contact'
    )
    
    virtuous = models.BooleanField(default=False)
    church_name = models.CharField(max_length=100)
    senior_pastor_first_name = models.CharField(max_length=100)
    senior_pastor_last_name = models.CharField(max_length=100)
    missions_pastor_first_name = models.CharField(max_length=100, null=True, blank=True)
    missions_pastor_last_name = models.CharField(max_length=100, null=True, blank=True)
    primary_contact_first_name = models.CharField(max_length=100)
    primary_contact_last_name = models.CharField(max_length=100)
    website = models.URLField(null=True, blank=True)
    denomination = models.CharField(max_length=100, null=True, blank=True)
    congregation_size = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=10, choices=COLOR, default='GREEN')
    church_pipeline = models.CharField(max_length=100, choices=CHURCH_PIPELINE_CHOICES, default='UNKNOWN')
    priority = models.CharField(max_length=10, choices=PRIORITY, default='MEDIUM')
    assigned_to = models.CharField(max_length=100, choices=ASSIGNED_TO_CHOICES, default='UNASSIGNED')
    source = models.CharField(max_length=100, choices=SOURCE, default='UNKNOWN')
    referred_by = models.CharField(max_length=100, null=True, blank=True)    
    info_given = models.TextField(null=True, blank=True)
    reason_closed = models.TextField(null=True, blank=True)    
    date_closed = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return self.church_name
    
    class Meta:
        verbose_name_plural = "Churches"

class NonProspectInd(Contact):
    MARITAL_STATUS = (
        ('single', 'Single'),('married', 'Married'),('divorced', 'Divorced'),('widowed', 'Widowed'),('separated', 'Separated'), ('unknown', 'Unknown'),
    )
    
    ASSIGNED_TO_CHOICES = (
        ('BILL JONES', 'BILL JONES'), ('JASON MODOMO', 'JASON MODOMO'), ('KEN KATAYAMA', 'KEN KATAYAMA'), ('MATTHEW RULE', 'MATTHEW RULE'),
        ('CHIP ATKINSON', 'CHIP ATKINSON'), ('RACHEL LIVELY', 'RACHEL LIVELY'), ('JIM BURCHEL', 'JIM BURCHEL'), ('JILL WALKER', 'JILL WALKER'),
        ('KARINA RAMPIN', 'KARINA RAMPIN'), ('UNASSIGNED', 'UNASSIGNED')        
    )
    
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS, default='unknown')
    assigned_to = models.CharField(max_length=30, choices=ASSIGNED_TO_CHOICES, default='UNASSIGNED')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Non-Prospect Individual"
        verbose_name_plural = "Non-Prospect Individuals"
    


