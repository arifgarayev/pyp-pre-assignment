import os
MIME_TYPES = ('application/vnd.ms-excel',
              'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
MAX_FILE_SIZE = 5000000

DATABASE_URL = 'postgresql://root:root@localhost'

SENDGRRID_API_KEY = os.getenv('SENDGRID_API_KEY')

SENDGRRID_API_KEY = '${{SENDGRRID_API_KEY}}'

FROM_EMAIL = 'garayevarif@gmail.com'

EMAIL_SUBJECTS = {1: "Type 1 - Segment-ə görə satışlar - Hər segmentə görə tarix aralığında məhsul sayı, satiş toplamı, endirim toplamı, qazanc toplamı məlumatları",
                  2: "Type 2 - Ölkəyə görə satışlar - Hər ölkəyə görə tarix aralığında məhsul sayı, satiş toplamı, endirim toplamı, qazanc toplamı məlumatları",
                  3: "Type 3 - Məhsula görə satışlar - Hər məhsula görə tarix aralığında məhsul sayı, satiş toplamı, endirim toplamı, qazanc toplamı məlumatları",
                  4: "Type 4 - Məhsula görə endirimlər - Hər məhsula görə tarix aralığında məhsula necə faiz endirim olunduğu məlumat"}
def filename_getter(filename: str):
    return filename

d = {'file_name': None}

dt_format = "%d/$m/$Y"
