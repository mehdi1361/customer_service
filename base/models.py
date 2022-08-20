from django.db import models


class Base(models.Model):
    created_date = models.DateTimeField(
        verbose_name='created date',
        auto_now_add=True, null=True
    )
    updated_date = models.DateTimeField(
        verbose_name='created date',
        auto_now=True, null=True
    )

    class Meta:
        abstract = True

class BaseBank(Base):
    title = models.CharField(max_length=100, blank=True, null=True)
    bank_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_bank'


class BaseBankBranch(Base):
    name = models.CharField(max_length=100, blank=True, null=True)
    rayan_bank_id = models.TextField(blank=True, null=True)
    bank_id = models.IntegerField(blank=True, null=True)
    city = models.ForeignKey('BaseCities', models.DO_NOTHING, blank=True, null=True)
    bank_branch_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    sejam_code = models.CharField(max_length=100, blank=True, null=True)
    dl_number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'base_bank_branch'


class BaseCities(Base):
    name = models.CharField(unique=True, max_length=10, blank=True, null=True)
    province = models.ForeignKey('BaseProvince', models.DO_NOTHING, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    rayan_city_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_cities'


class BaseCountries(Base):
    name = models.CharField(unique=True, max_length=10, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_countries'


class BaseFileType(Base):
    name = models.TextField(unique=True, blank=True, null=True)
    fa_name = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_force = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'base_file_type'


class BaseGender(Base):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'base_gender'


class BaseJob(Base):
    title = models.CharField(unique=True, max_length=10, blank=True, null=True)
    job_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'base_job'


class BaseMebbcoBranch(Base):
    title = models.CharField(max_length=100, blank=True, null=True)
    type_mebbco = models.CharField(max_length=50, blank=True, null=True)
    id_rayan = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        db_table = 'base_mebbco_branch'


class BaseMebbcoDomain(Base):
    title = models.CharField(unique=True, max_length=10, blank=True, null=True)
    id_rayan = models.IntegerField(blank=True, null=True)
    rayan_id = models.BigIntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_mebbco_domain'


class BaseProvince(Base):
    name = models.CharField(unique=True, max_length=10, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(BaseCountries, models.DO_NOTHING, blank=True, null=True)
    rayan_province_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_province'


class BaseState(Base):
    state_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    icon_class = models.CharField(max_length=100, blank=True, null=True)
    state_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_state'
