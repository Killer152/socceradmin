from django.db import models


class News(models.Model):
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    post_time = models.DateField()
    image = models.ImageField(upload_to='news_images/main_images/')

    def __str__(self):
        return f'{self.title_en}'

    class Meta:
        ordering = ['id']


class Detail_page(models.Model):
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/background_images/')
    text_en = models.TextField()
    text_ru = models.TextField()
    video=models.URLField(max_length=255,blank=True,null=True)
    detailpage = models.ForeignKey(News, on_delete=models.PROTECT, related_name='detailpage')

    def __str__(self):
        return f'{self.title_en}'

    class Meta:
        ordering = ['id']


class Players(models.Model):
    Goalkeeper = 'Goalkeeper'
    Right_Fullback = 'RightFullback'
    Left_Fullback = 'Left Fullback'
    Right_Wingback = 'Right Wingback'
    Left_Wingback = 'Left Wingback'
    Left_Winger = 'Left Winger'
    Right_Winger = 'Right Winger'
    Right_Midfield = 'Right Midfield'
    Defensive_Midfielder = 'Defensive Midfielder'
    Left_Midfield = 'Left Midfield'

    Central_Attacking_Midfielder = 'Central Attacking Midfielder'
    Centre_back = 'Centre-back'
    Center_Midfield = 'Center Midfield'
    Centre_Forward = 'Centre Forward'
    Striker = 'Striker'

    Goalkeeper_ru = 'Вратарь'
    Right_Fullback_ru = 'Правый защитник'
    Left_Fullback_ru = 'Левый защитник'
    Right_Wingback_ru = 'Правый Фланговый Защитник'
    Left_Wingback_ru = 'Левый Фланговый Защитник'
    Left_Winger_ru = 'Левый Нападающий'
    Right_Winger_ru = 'Правый Нападающий'
    Right_Midfield_ru = 'Правый полузащитник'
    Defensive_Midfielder_ru = 'Опорный Полузащитник'
    Left_Midfield_ru = 'Левый полузащитник'

    Central_Attacking_Midfielder_ru = 'Центральный Атакующий Полузащитник'
    Centre_back_ru = 'Центральный Защитник'
    Center_Midfield_ru = 'Центральный полузащитник'
    Centre_Forward_ru = 'Центральный Нападающий'
    Striker_ru = 'Форвард'

    GK = 'GK'
    RF = 'RF'
    LF = 'LF'
    LW = 'LW'
    RW = 'RW'
    DM = 'DM'
    LM = 'LM'
    CAM = 'CAM'
    CB = 'CB'
    CM = 'CM'
    CF = 'CF'
    LWB = 'LWB'
    RWB = 'RWB'
    ST = 'ST'

    GK_ru = 'ВРТ'
    RF_ru = 'ПЗ'
    LF_ru = 'ЛЗ'
    LW_ru = 'ЛФА'
    RW_ru = 'ПФА'
    RM_ru = 'ПП'
    DM_ru = 'ЦОП'
    LM_ru = 'ЛП'
    CAM_ru = 'ЦАП'
    CB_ru = 'ЦЗ'
    CM_ru = 'ЦП'
    CF_ru = 'ЦН'
    LWB_ru = 'ЛФЗ'
    RWB_ru = 'ПФЗ'
    ST_ru = 'ФРВ'

    amp_ru = ((GK_ru, GK_ru),
              (RF_ru, RF_ru),
              (LF_ru, LF_ru),
              (LW_ru, LW_ru),
              (RW_ru, RW_ru),
              (DM_ru, DM_ru),
              (LM_ru, LM_ru),
              (CAM_ru, CAM_ru),
              (CB_ru, CB_ru),
              (CM_ru, CM_ru),
              (CF_ru, CF_ru),
              (LWB_ru, LWB_ru),
              (RWB_ru, RWB_ru),
              (ST_ru, ST_ru)
              )
    amp_en = ((GK, GK),
              (RF, RF),
              (LF, LF),
              (LW, LW),
              (RW, RW),
              (DM, DM),
              (LM, LM),
              (CAM, CAM),
              (CB, CB),
              (CM, CM),
              (CF, CF),
              (LWB, LWB),
              (RWB, RWB),
              (ST, ST))

    pos_en = ((Goalkeeper, Goalkeeper),
              (Right_Fullback, Right_Fullback),
              (Left_Fullback, Left_Fullback),
              (Right_Wingback, Right_Wingback),
              (Left_Wingback, Left_Wingback),
              (Left_Winger, Left_Winger),
              (Right_Winger, Right_Winger),
              (Right_Midfield, Right_Midfield),
              (Defensive_Midfielder, Defensive_Midfielder),
              (Left_Midfield, Left_Midfield),
              (Right_Midfield, Right_Midfield),
              (Central_Attacking_Midfielder, Central_Attacking_Midfielder),
              (Centre_back, Centre_back),
              (Center_Midfield, Center_Midfield),
              (Centre_Forward, Centre_Forward),
              (Striker, Striker))

    pos_ru = ((Goalkeeper_ru, Goalkeeper_ru),
              (Right_Fullback_ru, Right_Fullback_ru),
              (Left_Fullback_ru, Left_Fullback_ru),
              (Right_Wingback_ru, Right_Wingback_ru),
              (Left_Wingback_ru, Left_Wingback_ru),
              (Left_Winger_ru, Left_Winger_ru),
              (Right_Winger_ru, Right_Winger_ru),
              (Right_Midfield_ru, Right_Midfield_ru),
              (Defensive_Midfielder_ru, Defensive_Midfielder_ru),
              (Left_Midfield_ru, Left_Midfield_ru),
              (Right_Midfield_ru, Right_Midfield_ru),
              (Central_Attacking_Midfielder_ru, Central_Attacking_Midfielder_ru),
              (Centre_back_ru, Centre_back_ru),
              (Center_Midfield_ru, Center_Midfield_ru),
              (Centre_Forward_ru, Centre_Forward_ru),
              (Striker_ru, Striker_ru))

    amplua_ru = models.CharField(choices=amp_ru, max_length=50)
    amplua_en = models.CharField(choices=amp_en, max_length=50)
    height = models.CharField(max_length=255,blank=True,null=True)
    full_name_ru = models.CharField(max_length=255)
    full_name_en = models.CharField(max_length=255)
    date_of_brith = models.DateField()
    club_ru = models.CharField(max_length=255)
    club_en = models.CharField(max_length=255)
    postion_en = models.CharField(choices=pos_en, max_length=50)
    postion_ru = models.CharField(choices=pos_ru, max_length=50)
    image = models.ImageField(upload_to='players/profile/')

    def __str__(self):
        return f'{self.full_name_en}'

    class Meta:
        ordering = ['id']
