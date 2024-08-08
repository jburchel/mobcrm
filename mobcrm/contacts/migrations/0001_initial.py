# Generated by Django 5.0.7 on 2024-08-08 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='contact_images/')),
                ('preferred_contact_method', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone'), ('text', 'Text'), ('Facebook Messanger', 'Facebook Messanger'), ('other', 'Other')], max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('type', models.CharField(choices=[('non_prospect_individual', 'Non-Prospect Individual'), ('church', 'Church'), ('prospect', 'Prospect')], max_length=100)),
                ('church', models.CharField(blank=True, max_length=100, null=True)),
                ('street_address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, choices=[('al', 'AL'), ('ak', 'AK'), ('az', 'AZ'), ('ar', 'AR'), ('ca', 'CA'), ('co', 'CO'), ('ct', 'CT'), ('de', 'DE'), ('fl', 'FL'), ('ga', 'GA'), ('hi', 'HI'), ('id', 'ID'), ('il', 'IL'), ('in', 'IN'), ('ia', 'IA'), ('ks', 'KS'), ('ky', 'KY'), ('la', 'LA'), ('me', 'ME'), ('md', 'MD'), ('ma', 'MA'), ('mi', 'MI'), ('mn', 'MN'), ('ms', 'MS'), ('mo', 'MO'), ('mt', 'MT'), ('ne', 'NE'), ('nv', 'NV'), ('nh', 'NH'), ('nj', 'NJ'), ('nm', 'NM'), ('ny', 'NY'), ('nc', 'NC'), ('nd', 'ND'), ('oh', 'OH'), ('ok', 'OK'), ('or', 'OR'), ('pa', 'PA'), ('ri', 'RI'), ('sc', 'SC'), ('sd', 'SD'), ('tn', 'TN'), ('tx', 'TX'), ('ut', 'UT'), ('vt', 'VT'), ('va', 'VA'), ('wa', 'WA'), ('wv', 'WV'), ('wi', 'WI'), ('wy', 'WY'), ('dc', 'DC')], max_length=2, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('date_last_updated', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Church',
            fields=[
                ('contact_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='church_contact', serialize=False, to='contacts.contact')),
                ('virtuous', models.BooleanField(default=False)),
                ('church_name', models.CharField(max_length=100)),
                ('senior_pastor_first_name', models.CharField(max_length=100)),
                ('senior_pastor_last_name', models.CharField(max_length=100)),
                ('missions_pastor_first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('missions_pastor_last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('primary_contact_first_name', models.CharField(max_length=100)),
                ('primary_contact_last_name', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('denomination', models.CharField(blank=True, max_length=100, null=True)),
                ('congregation_size', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(choices=[('RED', 'RED'), ('YELLOW', 'YELLOW'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], default='GREEN', max_length=10)),
                ('church_pipeline', models.CharField(choices=[('UNKNOWN', 'UNKNOWN'), ('COLD UNCONTACTED', 'COLD UNCONTACTED'), ('COLD CONTACTED', 'COLD CONTACTED'), ('REPEATED FOLLOWUP', 'REPEATED FOLLOWUP'), ('WARM UNCONTACTED', 'WARM UNCONTACTED'), ('WARM CONTACTED', 'WARM CONTACTED'), ('MET', 'MET'), ('MISSION VISION', 'MISSION VISION'), ('EN42', 'EN42')], default='UNKNOWN', max_length=100)),
                ('priority', models.CharField(choices=[('URGENT', 'URGENT'), ('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], default='MEDIUM', max_length=10)),
                ('assigned_to', models.CharField(choices=[('BILL JONES', 'BILL JONES'), ('JASON MODOMO', 'JASON MODOMO'), ('KEN KATAYAMA', 'KEN KATAYAMA'), ('MATTHEW RULE', 'MATTHEW RULE'), ('CHIP ATKINSON', 'CHIP ATKINSON'), ('RACHEL LIVELY', 'RACHEL LIVELY'), ('JIM BURCHEL', 'JIM BURCHEL'), ('JILL WALKER', 'JILL WALKER'), ('KARINA RAMPIN', 'KARINA RAMPIN'), ('UNASSIGNED', 'UNASSIGNED')], default='UNASSIGNED', max_length=100)),
                ('source', models.CharField(choices=[('WEBFORM', 'WEBFORM'), ('INCOMING CALL', 'INCOMING CALL'), ('EMAIL', 'EMAIL'), ('SOCIAL MEDIA', 'SOCIAL MEDIA'), ('COLD CALL', 'COLD CALL'), ('PERSPECTIVES', 'PERSPECTIVES'), ('REFERAL', 'REFERAL'), ('OTHER', 'OTHER'), ('UNKNOWN', 'UNKNOWN')], default='UNKNOWN', max_length=100)),
                ('referred_by', models.CharField(blank=True, max_length=100, null=True)),
                ('info_given', models.TextField(blank=True, null=True)),
                ('reason_closed', models.TextField(blank=True, null=True)),
                ('date_closed', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Churches',
            },
            bases=('contacts.contact',),
        ),
        migrations.CreateModel(
            name='NonProspectInd',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contacts.contact')),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed'), ('separated', 'Separated'), ('unknown', 'Unknown')], default='unknown', max_length=10)),
                ('assigned_to', models.CharField(choices=[('BILL JONES', 'BILL JONES'), ('JASON MODOMO', 'JASON MODOMO'), ('KEN KATAYAMA', 'KEN KATAYAMA'), ('MATTHEW RULE', 'MATTHEW RULE'), ('CHIP ATKINSON', 'CHIP ATKINSON'), ('RACHEL LIVELY', 'RACHEL LIVELY'), ('JIM BURCHEL', 'JIM BURCHEL'), ('JILL WALKER', 'JILL WALKER'), ('KARINA RAMPIN', 'KARINA RAMPIN'), ('UNASSIGNED', 'UNASSIGNED')], default='UNASSIGNED', max_length=30)),
            ],
            options={
                'verbose_name': 'Non-Prospect Individual',
                'verbose_name_plural': 'Non-Prospect Individuals',
            },
            bases=('contacts.contact',),
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('contact_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='prospect_contact', serialize=False, to='contacts.contact')),
                ('virtuous', models.BooleanField(default=False)),
                ('home_country', models.CharField(blank=True, max_length=100, null=True)),
                ('spouse_recruit', models.BooleanField(default=False)),
                ('marital_status', models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed'), ('separated', 'Separated'), ('unknown', 'Unknown')], max_length=100, null=True)),
                ('color', models.CharField(blank=True, choices=[('red', 'Red'), ('yellow', 'Yellow'), ('blue', 'Blue'), ('green', 'Green'), ('unknown', 'Unknown')], max_length=100, null=True)),
                ('individual_pipeline', models.CharField(blank=True, choices=[('unknown', 'Unknown'), ('rejected', 'Rejected'), ('contacted', 'Contacted'), ('mission vision', 'Mission Vision'), ('conversations', 'Conversations'), ('potential recruit', 'Potential Recruit'), ('recruit', 'Recruit'), ('applicant', 'Applicant'), ('teammate', 'Teammate')], max_length=100, null=True)),
                ('priority', models.CharField(blank=True, choices=[('urgent', 'Urgent'), ('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], max_length=100, null=True)),
                ('assigned_to', models.CharField(blank=True, choices=[('BILL JONES', 'BILL JONES'), ('JASON MODOMO', 'JASON MODOMO'), ('KEN KATAYAMA', 'KEN KATAYAMA'), ('MATTHEW RULE', 'MATTHEW RULE'), ('CHIP ATKINSON', 'CHIP ATKINSON'), ('RACHEL LIVELY', 'RACHEL LIVELY'), ('JIM BURCHEL', 'JIM BURCHEL'), ('JILL WALKER', 'JILL WALKER'), ('KARINA RAMPIN', 'KARINA RAMPIN'), ('UNASSIGNED', 'UNASSIGNED')], max_length=100, null=True)),
                ('source', models.CharField(blank=True, choices=[('WEBFORM', 'WEBFORM'), ('INCOMING CALL', 'INCOMING CALL'), ('EMAIL', 'EMAIL'), ('SOCIAL MEDIA', 'SOCIAL MEDIA'), ('COLD CALL', 'COLD CALL'), ('PERSPECTIVES', 'PERSPECTIVES'), ('REFERAL', 'REFERAL'), ('OTHER', 'OTHER'), ('UNKNOWN', 'UNKNOWN')], max_length=100, null=True)),
                ('referred_by', models.CharField(blank=True, max_length=100, null=True)),
                ('info_given', models.TextField(blank=True, null=True)),
                ('desired_service', models.TextField(blank=True, null=True)),
                ('reason_closed', models.TextField(blank=True, null=True)),
                ('date_closed', models.DateField(blank=True, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='contacts.contact')),
            ],
            options={
                'verbose_name': 'Prospect',
                'verbose_name_plural': 'Prospects',
            },
            bases=('contacts.contact',),
        ),
    ]
