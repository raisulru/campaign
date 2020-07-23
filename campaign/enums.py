PENDING = 'pending'
PROCESSING = 'processing'
COMPLETE = 'complete'

CAMPAIGN_STATUS = [
    (PENDING, 'Pending'),
    (PROCESSING, 'Processing'),
    (COMPLETE, 'Complete')
]


GP = 'GP'
BL = 'BL'
TT = 'TT'
RB = 'RB'

SENDER_CHOICES = [
    (GP, 'Grameen Phone'),
    (BL, 'Banglalink'),
    (TT, 'Tele Talk'),
    (RB, 'Robi')

]

SENT = 'sent'

RECIPIENT_STATUS = [
    (PENDING, 'Pending'),
    (SENT, 'Sent')
]