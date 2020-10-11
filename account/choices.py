from django.utils.translation import ugettext_lazy as _

ENGLISH_LANG = 'EN'
RUSSIAN_LANG = 'RU'
TURKISH_LANG = 'TR'
AZERBAIJANI_LANG = 'AZ'
LANGUAGE_CHOICES = [
    (ENGLISH_LANG, 'English'),
    (RUSSIAN_LANG, 'Russian'),
    (TURKISH_LANG, 'Turkish'),
    (AZERBAIJANI_LANG, 'Azerbaijan'),
]


MALE_GENDER = 'M'
FEMALE_GENDER = 'F'
GENDER_CHOICES = [
    (MALE_GENDER, _('Male')),
    (FEMALE_GENDER, _('Female')),
]

A_PLUS = 'A RH+'
A_MINUS = 'A RH-'
AB_PLUS = 'AB RH+'
AB_MINUS = 'AB RH-'
B_PLUS = 'B RH+'
B_MINUS = 'B RH-'
ZERO_PLUS = '0 RH+'
ZERO_MINUS = '0 RH-'
BLOOD_GROUP_CHOICES = [
    (A_PLUS, A_PLUS),
    (A_MINUS, A_MINUS),
    (AB_PLUS, AB_PLUS),
    (AB_MINUS, AB_MINUS),
    (B_PLUS, B_PLUS),
    (B_MINUS, B_MINUS),
    (ZERO_PLUS, ZERO_PLUS),
    (ZERO_MINUS, ZERO_MINUS),
]


ACTIVITY_LOW = 'Low'
ACTIVITY_MEDIUM = 'Medium'
ACTIVITY_HIGH = 'High'
PHYSICAL_ACTIVITY_CHOICES = [
    (ACTIVITY_LOW, ACTIVITY_LOW),
    (ACTIVITY_MEDIUM, ACTIVITY_MEDIUM),
    (ACTIVITY_HIGH, ACTIVITY_HIGH),
]

SMOKER_NON = 'Non-smoker'
SMOKER_EX = 'Ex-smoker'
SMOKER_LIGHT = 'Light-smoker'
SMOKER_MODERATE = 'Moderate-smoker'
SMOKER_HEAVY = 'Heavy-smoker'
SMOKING_CHOICES = [
    (SMOKER_NON, SMOKER_NON),
    (SMOKER_EX, SMOKER_EX),
    (SMOKER_LIGHT, 'Light smoker (less than 10)'),
    (SMOKER_MODERATE, 'Moderate smoker (10 to 19)'),
    (SMOKER_HEAVY, 'Heavy smoker (20 or over)'),
]

DIABET_TYPE_NONE = 'None'
DIABET_TYPE_ONE = 'Type 1'
DIABET_TYPE_TWO = 'Type 2'
DIABETS_CHOICES = [
    (DIABET_TYPE_NONE, DIABET_TYPE_NONE),
    (DIABET_TYPE_ONE, DIABET_TYPE_ONE),
    (DIABET_TYPE_TWO, DIABET_TYPE_TWO),
]

ETHNICITY_WHITE = 'White'
ETHNICITY_INDIAN = 'Indian'
ETHNICITY_PAKISTANI = 'Pakistani'
ETHNICITY_BANGLADESHI = 'Bangladeshi'
ETHNICITY_OTHER_ASIAN = 'Asian'
ETHNICITY_BLACK_CARIBBEAN = 'Caribbean'
ETHNICITY_BLACK_AFRICAN = 'African'
ETHNICITY_CHINESE = 'Chinese'
ETHNICITY_OTHERS = 'Others'
ETHNICITY_CHOICES = [
    (ETHNICITY_WHITE, 'White or not stated'),
    (ETHNICITY_INDIAN, ETHNICITY_INDIAN),
    (ETHNICITY_PAKISTANI, ETHNICITY_PAKISTANI),
    (ETHNICITY_BANGLADESHI, ETHNICITY_BANGLADESHI),
    (ETHNICITY_OTHER_ASIAN, 'Other Asian'),
    (ETHNICITY_BLACK_CARIBBEAN, 'Black Caribbean'),
    (ETHNICITY_BLACK_AFRICAN, 'White or not stated'),
    (ETHNICITY_BLACK_AFRICAN, 'Black African'),
    (ETHNICITY_CHINESE, ETHNICITY_CHINESE),
    (ETHNICITY_OTHERS, ETHNICITY_OTHERS),
]