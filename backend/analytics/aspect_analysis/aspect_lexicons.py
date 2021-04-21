fingerprint_types = ['onscreen', 'rear', 'powerbutton']
display_types = ['normal', 'curved', 'flip']
charger_types = ['wireless', 'wired']
headphone_jack = ['available', 'none']
size = ['normal', 'large']

FEATURE_TYPES = {
    "display": display_types,
    "fingerprint": fingerprint_types,
    "headphone-jack": headphone_jack,
    "size": size,
}
FEATURE_CATEGORY = ["camera", "display", "battery",
                    "face recognition", "fingerprint", "speakers", "headphone-jack", "headphone", "wireless-charger", "charger", "size"]

category_synonyms = [["camera"],
                     ["display", "screen"],
                     ["battery"],
                     ["face recognition", "face id",
                      "recognition", "face-recognition"],
                     ["fingerprint", "reader"],
                     ["speakers", "speaker", "sound"],
                     ["headphone jack", "headphone-jack"],
                     ["headphone", "earphone"],
                     ["charger", "charge", "charging"],
                     ["wireless charger", "wireless-charge",
                         "wireless charging", "wireless-charging"],
                     ["size"]
                     ]
phones = {
    fingerprint_types[0]: [
        'oneplus-6t',
        'oneplus-7t',
        'oneplus-7-pro',
        'oneplus-8-pro',
        'oneplus-8t',
        'samsung-galaxy-a50',
        'samsung-galaxy-note-10-lite',
        'samsung-electronics-galaxy-note-20',
        'samsung-galaxy-a31',
        'samsung-galaxy-a51',
        'samsung-galaxy-a71',
        'huawei-p30pro'
    ],
    fingerprint_types[1]: [
        'oneplus-6',
        'oneplus-nord-n100',
        'oneplus-6t',
        'samsung-galaxy-a21s',
        'samsung-galaxy-a70',
        'google-pixel-4a',
        'huawei-p30-lite'
    ],
    fingerprint_types[2]: [
        'realme-6',
        'realme-6-pro',
        'samsung-galaxy-j3-prime'
    ],
    display_types[0]: [
        'samsung-galaxy-note-8',
        "samsung-galaxy-s10",
        "samsung-galaxy-s9",
        'apple-iphone-11',
        'samsung-galaxy-a21s',
        'apple-iphone-7-plus',
        'apple-iphone-7',
        'apple-iphone-8-plus',
        'apple-iphone-8',
        'apple-iphone-se',
        'apple-iphone-x',
        'apple-iphone-xr',
        'apple-iphone-xs-max',
        'apple-iphone-xs',
        'samsung-galaxy-note-10-lite',
        'samsung-galaxy-a01-core',
        'samsung-galaxy-a01',
        'samsung-galaxy-a10e',
        'samsung-galaxy-a10s',
        'samsung-galaxy-a11',
    ],
    display_types[1]: [
        "samsung-galaxy-s10+",
        "samsung-galaxy-s9+",
        'oneplus-7-pro',
        'oneplus-8-pro',
        'oneplus-8t',
        'samsung-galaxy-a50',
        'samsung-electronics-galaxy-note-20',
        'samsung-galaxy-a31',
        'samsung-galaxy-a51',
        'samsung-galaxy-a70',
        'samsung-galaxy-a71',
        'google-pixel-4',
        'google-pixel-4a',
        'huawei-p30-lite',
        'huawei-p30pro'
    ],
    display_types[2]: [
        'samsung-galaxy-z-flip'
    ],
    charger_types[0]: [

    ],
    charger_types[1]: [

    ],

    headphone_jack[0]: [
        'Huawei-honor-9',
        'huawei-honor-8s',
        'samsung-galaxy-a50',
        'samsung-galaxy-note-10-lite',
        'samsung-galaxy-a01-core',
        'samsung-galaxy-a01',
        'samsung-galaxy-a10e',
        'samsung-galaxy-a10s',
        'samsung-galaxy-a11',
        'apple-iphone-20s',
        'samsung-galaxy-note-',
        'samsung-galaxy-a21s',
        'samsung-galaxy-a31',
        'samsung-galaxy-a51',
        'samsung-galaxy-a70',
        'samsung-galaxy-a71',
        'motorola-moto-z-play',
        'google-pixel-4a',
        'huawei-p30-lite',

    ],
    headphone_jack[1]: [
        'oneplus-7t',
        'oneplus-7-pro',
        'oneplus-8t',
        'oneplus-8-pro',
        'apple-iphone-11',
        'apple-iphone-7-plus',
        'apple-iphone-7',
        'apple-iphone-8-plus',
        'apple-iphone-8',
        'apple-iphone-x',
        'apple-iphone-xr',
        'apple-iphone-xs-max',
        'apple-iphone-xs',
        'samsung-electronics-galaxy-note-20',
        'google-pixel-4',
        'huawei-p30pro',

    ],
    size[0]: [
        'apple-iphone-8',
        'samsung-galaxy-a50',
        'apple-iphone-11',
        'apple-iphone-7',
        'apple-iphone-se',
        'apple-iphone-x',
        'apple-iphone-xr',
        'apple-iphone-xs',
        'samsung-galaxy-a01-core',
        'samsung-galaxy-a01',
        'samsung-galaxy-a10e',
        'Samsung-galaxy-a10s',
        'samsung-galaxy-a11',
        'Apple-iphone-20s',
        'Motorola-moto-z-play',
        'Google-pixel-4',
        'google-pixel-4a',

    ],
    size[1]: ['samsung-galaxy-note-8',
              'apple-iphone-8-plus',
              'apple-iphone-7-plus',
              'apple-iphone-xs-max',
              'samsung-galaxy-note-10-lite',
              'samsung-electronics-galaxy-note-20',
              'Samsung-galaxy-a21s',
              'Samsung-galaxy-a31',
              'Samsung-galaxy-a51',
              'Samsung-galaxy-a70',
              'Samsung-galaxy-a71',
              'Huawei-p30-lite',
              'huawei-p30pro', ]
}
