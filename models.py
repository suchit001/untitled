from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

class Principal_investigator(models.Model):
    PI_id = models.UUIDField(primary_key=True,editable=False)
    p_name = models.CharField(max_length=100)
    P_Dept = models.CharField(max_length=100)
    p_contact = models.CharField(max_length=20)
    p_email = models.EmailField(max_length=100,unique=True,null=True,blank=True)
    p_designation =models.CharField(max_length=100)

class Co_Investigator(models.Model):
    Co_inv_id = models.UUIDField(max_length=12,primary_key=True,editable=False)
    Co_name = models.CharField(max_length=100)
    Co_designation = models.CharField(max_length=100)
    Co_contact_no = models.CharField(max_length=20)
    Co_email = models.EmailField(max_length=100,unique=True,null=True,blank=True)


class collaborations(models.Model):
    collab_id=models.UUIDField(primary_key=True,editable=False)
    Institue = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Collab_type = models.TextField()
    Ec_approval = models.BooleanField(max_length=2)
    Authorship = models.TextField()


class Std_details(models.Model):
    std_id = models.UUIDField(primary_key=True,editable=False)
    st_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    st_contact_no = models.CharField(max_length=100)
    st_email = models.EmailField(max_length=100,unique=True,null=True,blank=True)
    study_purpose =(
        ('D','DNB'),('M','MSc'),('P','PhD'),('O','Others')
    )
    st_study_purpose = models.CharField(max_length=100,choices=study_purpose)
    st_collab_id = models.ForeignKey(collaborations, on_delete=models.CASCADE)

class study_design(models.Model):
    study_design_id = models.UUIDField(primary_key=True,editable=False)
    case_report = (
        ('O','Cohort,Prospective'),('ER','Open-(non blinded)'),('EN','Non-Randomized')
    )
    cs_report = models.CharField(max_length=100,choices=case_report)
    case_series = (
        ('O','Cohort,Retrospective'),('ER','Single-blind'),('EN','Study of diagnostic efficacy')
    )

    cs_series = models.CharField(max_length=100,choices=case_series)
    survey = (
        ('OC','Case control'),('OS','Cross-sectional'),('ERD','Double blind'),('ERT','Triple blind')
    )
    srvey = models.CharField(max_length=100,choices=survey)
    others = models.TextField()

class Time_Frame(models.Model):
    time_frame_id = models.UUIDField(primary_key=True,editable=False)
    study_coll_period = models.DurationField()
    retro_period = models.DurationField()
    patient_part = models.DurationField()
    data_analysis = models.DurationField
    Thesis_submis = models.DurationField()

class  pat_sel_id(models.Model):
    pat_sel_id = models.UUIDField(primary_key=True,editable=False)
    define_pop = models.TextField()
    In_criteria = models.TextField()
    Ex_criteria = models.TextField()

class work_up(models.Model):
    work_up_id = models.UUIDField(primary_key=True,editable=False)
    clinical = models.TextField()
    Investigations = models.TextField()

class Out_funding(models.Model):
    fund_id = models.UUIDField(primary_key=True,editable=False)
    fund_name= models.TextField()
    address= models.TextField()
    email = models.EmailField(max_length=100,null=False,blank=False)
    type = models.TextField()


class study_step(models.Model):
    study_step = models.UUIDField(primary_key=True,editable=True)
    patient_sel_id = models.ForeignKey(pat_sel_id,on_delete=models.CASCADE)
    inf_consent = (
        ('W','Written'),('T','Telephonic'),('V','Waiver'),('O','Other')
    )
    informed_consent = models.CharField(max_length= 100,choices=inf_consent)
    int_code = (
        ('D','Drug Studies For approved indication'),
        ('O','Off-label use of drugs approved for other indication'),
        ('S','Surgery'),
        ('T','Special Test'),
        ('Q','Questionaire'),
        ('A','Any other')
    )
    Intevention_code =models.CharField(max_length=100,choices=int_code)
    Q_valid = (
        ('Y','YES'),('N','NO')
    )
    Questionaire_valid=models.CharField(max_length=100,choices=Q_valid)
    R_lang = (
        ('Y','YES'),('N','NO')
    )
    Regional_lang = models.CharField(max_length=100,choices=R_lang)
    work_up_id = models.ForeignKey(work_up,on_delete=models.CASCADE)
    med_id = models.URLField()
    surgical_id = models.URLField()
    lab_id = models.URLField()
    outcome_measure_id = models.TextField()
    methodology = models.TextField()
    proforma = models.TextField()
    translation = models.TextField()
    budget_id = models.CharField(max_length=100)
    outside_fund = models.ForeignKey(Out_funding,on_delete=models.CASCADE)

class prog_report(models.Model):
    progress_id = models.UUIDField(primary_key=True,editable=False)

class comp_report(models.Model):
    completion_id = models.UUIDField(primary_key=True,editable=False)


class project_detials(models.Model):
    project_id = models.UUIDField(primary_key=True,editable=False)
    project_code_no =models.CharField(editable=False,max_length=100)
    PI_id = models.ForeignKey(Principal_investigator,on_delete=models.CASCADE)
    Co_id = models.ForeignKey(Co_Investigator,on_delete=models.CASCADE)
    period_of_data =  models.DurationField()
    enroll_period = models.DurationField()
    budget_estimate = models.IntegerField()
    stud_id = models.ForeignKey(Std_details,on_delete=models.CASCADE)
    project_title = models.CharField(max_length=256)
    appr_date_erb = models.DateField()
    st_design_id = models.ForeignKey(study_design,on_delete=models.CASCADE)
    sample_size = models.IntegerField()
    fund = (
        ('H','HH'),('O','Out')
    )
    choose_fund = models.CharField(max_length=100,choices=fund)
    Funding_body = models.ForeignKey(Out_funding,on_delete=models.CASCADE)
    Time_frame_id = models.ForeignKey(Time_Frame,on_delete=models.CASCADE)
    study_steps_id = models.ForeignKey(study_step,on_delete=models.CASCADE)
    progress_report_id = models.ForeignKey(prog_report,on_delete=models.CASCADE)
    completion_report_id = models.ForeignKey(comp_report,on_delete=models.CASCADE)

class sec_details(models.Model):
    sec_id = models.UUIDField(primary_key=True,editable=False)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)


class Director_details(models.Model):
    dir_id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)


class login(models.Model):
    secretariat_id = models.ForeignKey(sec_details,on_delete=models.CASCADE)
    Director_id = models.ForeignKey(Director_details,on_delete=models.CASCADE)
    Consultant_id = models.ForeignKey(Principal_investigator,on_delete=models.CASCADE)
    Researcher_id = models.ForeignKey(Std_details,on_delete=models.CASCADE)






    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
