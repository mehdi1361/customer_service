from django.db import models
from base.models import Base, BaseJob, BaseBankBranch, BaseMebbcoBranch, BaseFileType, BaseState

# Create your models here.
class BaseMebbcoCustomerGroup(Base):
    title = models.CharField(max_length=10, blank=True, null=True)
    rayan_id = models.BigIntegerField(blank=True, null=True)
    customer = models.ForeignKey('CustomerBrokerInfo', models.DO_NOTHING, blank=True, null=True)
    id_rayan = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_mebbco_customer_group'


class CustomerAddress(Base):
    address = models.CharField(max_length=250, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    mebbco_type = models.TextField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    country_name = models.CharField(max_length=100, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    province_name = models.CharField(max_length=100, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)
    section_id = models.IntegerField(blank=True, null=True)
    section_name = models.CharField(max_length=100, blank=True, null=True)
    city_prefix = models.TextField(blank=True, null=True)
    alley = models.TextField(blank=True, null=True)
    plaque = models.TextField(blank=True, null=True)
    tel = models.CharField(max_length=100, blank=True, null=True)
    country_prefix = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    emergency_tel = models.CharField(max_length=100, blank=True, null=True)
    emergency_tel_city_prefix = models.CharField(max_length=100, blank=True, null=True)
    emergency_tel_country_prefix = models.CharField(max_length=100, blank=True, null=True)
    fax_prefix = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'customer_address'


class CustomerBankAccount(Base):
    account_number = models.TextField(blank=True, null=True)
    rayan_bank_account_id = models.BigIntegerField(blank=True, null=True)
    ba_type_name = models.CharField(max_length=60, blank=True, null=True)
    shaba = models.CharField(max_length=60, blank=True, unique=True)
    is_default = models.BigIntegerField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_online = models.BigIntegerField(blank=True, null=True)
    branch = models.ForeignKey(BaseBankBranch, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    sheba = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'customer_bank_account'


class CustomerBranch(Base):
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey(BaseMebbcoBranch, models.DO_NOTHING, blank=True, null=True)
    mebbco_type = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'customer_branch'
        unique_together = (('customer', 'branch'),)


class CustomerBrokerBourseAccounts(Base):
    rayan_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)
    is_default = models.BooleanField(default=True)
    customer = models.ForeignKey('CustomerBrokerInfo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customer_broker_bourse_accounts'


class CustomerBrokerInfo(Base):
    telegram_username = models.CharField(max_length=100, blank=True, null=True)
    telegram_status_id = models.CharField(max_length=100, blank=True, null=True)
    registeration_number = models.CharField(max_length=100, blank=True, null=True)
    bourse_account_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=100, blank=True, null=True)
    online_username = models.CharField(max_length=100, blank=True, null=True)
    has_online_account = models.BigIntegerField(blank=True, null=True)
    modification_date = models.CharField(max_length=100, blank=True, null=True)
    is_mmtp_user = models.BigIntegerField(blank=True, null=True)
    mmtp_user_status_id = models.BigIntegerField(blank=True, null=True)
    is_site_user = models.BigIntegerField(blank=True, null=True)
    e_order_status_id = models.BigIntegerField(blank=True, null=True)
    has_sign_sample = models.BooleanField(blank=True, null=True)
    has_customer_photo = models.BooleanField(blank=True, null=True)
    has_birth_certificate = models.BooleanField(blank=True, null=True)
    has_certificate_comments = models.BooleanField(blank=True, null=True)
    has_zip_file = models.BooleanField(blank=True, null=True)
    has_official_gazette = models.BooleanField(blank=True, null=True)
    has_official_ads = models.BooleanField(blank=True, null=True)
    comex_visitor_id = models.BigIntegerField(blank=True, null=True)
    mmtp_user_id = models.BigIntegerField(blank=True, null=True)
    comex_economy_account = models.CharField(max_length=100, blank=True, null=True)
    is_portfo = models.BigIntegerField(blank=True, null=True)
    trader_credit = models.BigIntegerField(blank=True, null=True)
    comex_credit = models.BigIntegerField(blank=True, null=True)
    sf_credit = models.BigIntegerField(blank=True, null=True)
    credit = models.BigIntegerField(blank=True, null=True)
    is_stock_credit_purchase = models.BigIntegerField(blank=True, null=True)
    is_collateral_stocks_customer = models.BigIntegerField(blank=True, null=True)
    customer_identity = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    customer_service = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customer_broker_info'


class CustomerComexVisitor(Base):
    comex_id_rayan = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=60, blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    type_mebbco = models.ForeignKey(BaseMebbcoBranch, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customer_comex_visitor'


class Customer(Base):
    sejam_reference_code = models.CharField(max_length=100, blank=True, null=True)
    normal_national_code = models.CharField(unique=True, max_length=11)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_rayan_service = models.BooleanField(default=False)
    is_sejami = models.BooleanField(default=False, db_column="is_sejami")
    sejam_type = models.TextField(null=True)
    rayan_customer_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'customer_customer'


class CustomerFile(Base):
    file_data = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    #file_type_id = models.IntegerField(db_column='file_type__id', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    file_type = models.ForeignKey(BaseFileType, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customer_file'


class CustomerFinancialInfo(Base):
    asset_value = models.BigIntegerField(blank=True, null=True)
    incoming_average = models.BigIntegerField(blank=True, null=True)
    s_exchange_tranasction = models.BigIntegerField(blank=True, null=True)
    c_exchange_tranasction = models.BigIntegerField(blank=True, null=True)
    out_exchange_tranasction = models.BigIntegerField(blank=True, null=True)
    tranasction_level = models.TextField(blank=True, null=True)
    trading_knowledge_level = models.TextField(blank=True, null=True)
    company_purpose = models.TextField(blank=True, null=True)
    reference_rate_company = models.TextField(blank=True, null=True)
    rate_date = models.TextField(blank=True, null=True)
    rate = models.TextField(blank=True, null=True)
    customer = models.OneToOneField(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customer_financial_info'


class CustomerFund(Base):
    customer_id = models.BigIntegerField(blank=True, null=True)
    referred_by = models.CharField(max_length=60, blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    fund_name = models.CharField(max_length=60, blank=True, null=True)
    personality = models.CharField(max_length=60, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    issuing_city = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    national_identifier = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.CharField(max_length=100, blank=True, null=True)
    is_profit_issue = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=100, blank=True, null=True)
    customer_service = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    is_portfo = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'customer_fund'


class CustomerJobInfo(Base):
    employment_date = models.CharField(max_length=60, blank=True, null=True)
    company_name = models.CharField(max_length=60, blank=True, null=True)
    company_address = models.CharField(max_length=60, blank=True, null=True)
    company_postal_code = models.CharField(max_length=60, blank=True, null=True)
    company_email = models.CharField(max_length=60, blank=True, null=True)
    company_website = models.CharField(max_length=60, blank=True, null=True)
    company_city_prefix = models.CharField(max_length=60, blank=True, null=True)
    company_phone = models.CharField(max_length=60, blank=True, null=True)
    job_description = models.CharField(max_length=60, blank=True, null=True)
    position = models.CharField(max_length=60, blank=True, null=True)
    company_fax_prefix = models.CharField(max_length=60, blank=True, null=True)
    company_fax = models.CharField(max_length=60, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    job = models.ForeignKey(BaseJob, models.DO_NOTHING, blank=True, null=True)
    job_title = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'customer_job_info'


class CustomerLegalInfo(Base):
    id = models.OneToOneField(Customer, models.DO_NOTHING, db_column='id', primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    company_name = models.CharField(max_length=60, blank=True, null=True)
    register_number = models.CharField(max_length=60, blank=True, null=True)
    register_place = models.CharField(max_length=60, blank=True, null=True)
    register_date = models.CharField(max_length=100, blank=True, null=True)
    economic_code = models.CharField(max_length=100, blank=True, null=True)
    evidence_release_company = models.CharField(max_length=100, blank=True, null=True)
    evidence_release_date = models.CharField(max_length=100, blank=True, null=True)
    evidence_expiration_date = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'customer_legal_info'


class CustomerPhonePerson(Base):
    phone_number = models.CharField(max_length=60, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_mobile = models.BooleanField(default=False)
    mebbco_type = models.CharField(max_length=50, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customer_phone_person'


class CustomerPortfo(Base):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    domain_id = models.IntegerField(blank=True, null=True)
    intro_date = models.CharField(max_length=60, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    out_exchange_tranasction = models.CharField(max_length=60, blank=True, null=True)
    bourse_account_number = models.CharField(max_length=60, blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    c_exchange_tranasction = models.IntegerField(blank=True, null=True)
    stock_credit_purchase = models.IntegerField(blank=True, null=True)
    parent_national_code = models.CharField(max_length=250, blank=True, null=True)
    parent_is_portfo = models.BooleanField(blank=True, null=True)
    comex_visitor_id = models.IntegerField(blank=True, null=True)
    is_online = models.BooleanField(blank=True, null=True)
    customer_status_id = models.IntegerField(blank=True, null=True)
    eorder_status_id = models.IntegerField(blank=True, null=True)
    sms_transaction = models.CharField(max_length=50, blank=True, null=True)
    is_e_payment_customer = models.BooleanField(blank=True, null=True)
    dl_number = models.IntegerField(blank=True, null=True)
    type_mebbco = models.ForeignKey(BaseMebbcoBranch, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customer_portfo'


class CustomerPrivateInfo(Base):
    id = models.OneToOneField(Customer, models.DO_NOTHING, db_column='id', primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    father_name = models.CharField(max_length=60, blank=True, null=True)
    seri_sh_char = models.CharField(max_length=100, blank=True, null=True)
    seri_sh = models.CharField(max_length=100, blank=True, null=True)
    serial = models.CharField(max_length=100, blank=True, null=True)
    sh_number = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.CharField(max_length=100, blank=True, null=True)
    place_of_issue = models.CharField(max_length=100, blank=True, null=True)
    signature_file = models.TextField(blank=True, null=True)
    customer_id = models.IntegerField(unique=True, blank=True, null=True)
    sex_type_id = models.IntegerField(blank=True, null=True)
    sex_type_name = models.CharField(max_length=20, null=True)
    place_of_birth = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'customer_private_info'


class CustomerState(Base):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey(BaseState, models.DO_NOTHING, blank=True, null=True)
    confirm = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'customer_state'


class CustomerVerification(Base):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=4, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customer_verification'
