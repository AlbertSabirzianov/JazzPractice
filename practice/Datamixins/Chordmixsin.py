class ChordDataMixin:
    MINOR = [
        'https://cloud.mail.ru/public/LW8T/RaSTadQgY',
        'https://cloud.mail.ru/public/1VgS/nAS6L6a72',
    ]
    MINOR_NINE = [
        'https://cloud.mail.ru/public/Exsx/f34tpDm15',
        'https://cloud.mail.ru/public/ViQb/aYKH5VLJu',
        'https://cloud.mail.ru/public/H4qf/fowE67hpV',
    ]
    MINOR_ELEVEN = [
        'https://cloud.mail.ru/public/mNDp/bx176bdkY',
        'https://cloud.mail.ru/public/JqHb/RynnjqSdn',
        'https://cloud.mail.ru/public/oVk6/dwDHj9vyx',
    ]
    SEPT = [
        'https://cloud.mail.ru/public/VHgX/oSDT4mUmf',
        'https://cloud.mail.ru/public/urVU/pTipb9VSM',
        'https://cloud.mail.ru/public/3tVk/WoSEEEU6v',
    ]
    SEPT_NINE = [
        'https://cloud.mail.ru/public/ATwg/6QRnTEvLp',
        'https://cloud.mail.ru/public/9WXj/gjBXrfmTS',
    ]
    SEPT_THIRTEEN = [
        'https://cloud.mail.ru/public/vKQB/R3h2t4Gjy',
        'https://cloud.mail.ru/public/BDgf/H8tqXtkKd',
        'https://cloud.mail.ru/public/oTiQ/9ooofRm8F',
    ]
    SEPT_SHARP_ELEVEN = [
        'https://cloud.mail.ru/public/EyUF/bNBMVRuAC',
        'https://cloud.mail.ru/public/MaTR/ErDy27cpk',
        'https://cloud.mail.ru/public/kcLZ/VDXYY8HQp',
    ]
    SEPT_FLAT_NINE = [
        'https://cloud.mail.ru/public/yd4f/VzWhYfr4s',
        'https://cloud.mail.ru/public/ndV7/kYQQ17oZ4',
        'https://cloud.mail.ru/public/4U4T/MVJjDxjkY',
    ]
    SEPT_SHARP_NINE = [
        'https://cloud.mail.ru/public/oSMR/4DBwiqqBz',
        'https://cloud.mail.ru/public/eSGm/vxfdJeigT',
        'https://cloud.mail.ru/public/3yyQ/493nXJQnw',
    ]
    # SEPT_FLAT_FIVE = ['7b5']
    SEPT_SHARP_FIVE = [
        'https://cloud.mail.ru/public/z8fS/daF8mGsSQ',
        'https://cloud.mail.ru/public/TEMJ/qYpnPWKV6',
        'https://cloud.mail.ru/public/6XsQ/VE9KTSXTk',
    ]
    SEPT_FLAT_NINE_FLAT_THIRTEEN = [
        'https://cloud.mail.ru/public/U4sw/x6h1ETSmT',
        'https://cloud.mail.ru/public/kXxf/PxTskLAyx',
        'https://cloud.mail.ru/public/XPj9/2rFctkJmL',
    ]
    SEPT_SHARP_NINE_FLAT_THIRTEEN = [
        'https://cloud.mail.ru/public/CXm8/rQXdHMBrj',
        'https://cloud.mail.ru/public/fEFY/TicFY9Wos',
        'https://cloud.mail.ru/public/Pj1S/7G97ADVST',
    ]
    HALFDIMINISHED = [
        'https://cloud.mail.ru/public/xWmP/gJpqKd2vX',
        'https://cloud.mail.ru/public/2cDK/wqkEFVTT4',
    ]
    HALFDIMINISHED_NINE = [
        'https://cloud.mail.ru/public/uStD/qVzFkHyCG',
        'https://cloud.mail.ru/public/x9TM/cTAczuMDB',
    ]
    SUS = [
        'https://cloud.mail.ru/public/zdSS/BrYkWjckn',
        'https://cloud.mail.ru/public/xQn4/88KU4PCs1',
    ]
    SUS_NINE = [
        'https://cloud.mail.ru/public/Mc2M/NH1SnHYNo',
        'https://cloud.mail.ru/public/LrkX/2JdNBoQXW',
    ]
    SUS_THIRTEEN = [
        'https://cloud.mail.ru/public/6vUb/QMKfWJdMu',
        'https://cloud.mail.ru/public/fozf/QXXymKMQK',
    ]
    MAJ = [
        'https://cloud.mail.ru/public/am6f/ocfzEUhDu',
        'https://cloud.mail.ru/public/F3DE/nJXjtYfD5',
    ]
    MAJ_NINE = [
        'https://cloud.mail.ru/public/M2dh/uTezfSxSd',
        'https://cloud.mail.ru/public/D9bZ/LMM2zHH81',
    ]
    MAJ_SHARP_ELEVEN = [
        'https://cloud.mail.ru/public/tizu/ge3bnUHaP',
        'https://cloud.mail.ru/public/9zDm/hgZf2ePt1',
    ]
    MINOR_MAJ_SEVEN = [
        'https://cloud.mail.ru/public/p4fE/nQhVBKyfj',
        'https://cloud.mail.ru/public/s4Dv/ntgYLNmko',
    ]
    MINOR_MAJ_SEVEN_NINE = [
        'https://cloud.mail.ru/public/hKss/XZ35UKFkL',
        'https://cloud.mail.ru/public/4NCT/AHAS1ZqTS',
    ]
    MINOR_SIX = [
        'https://cloud.mail.ru/public/9Drs/YjpWzcFBn',
        'https://cloud.mail.ru/public/E9dL/SZsNhC6Aj',
    ]
    MINOR_SIX_NINE = [
        'https://cloud.mail.ru/public/ufs2/Ci6vTZUyj',
        'https://cloud.mail.ru/public/YNno/FRhitVgEJ',
    ]
    data_number_chordlist: dict[int, list] = {
        1: MINOR,
        2: MINOR_NINE,
        3: MINOR_ELEVEN,
        4: SEPT,
        5: SEPT_NINE,
        6: SEPT_THIRTEEN,
        7: SEPT_SHARP_ELEVEN,
        8: SEPT_FLAT_NINE,
        9: SEPT_SHARP_NINE,
        # 10: SEPT_FLAT_FIVE,
        10: SEPT_SHARP_FIVE,
        11: SEPT_FLAT_NINE_FLAT_THIRTEEN,
        12: SEPT_SHARP_NINE_FLAT_THIRTEEN,
        13: HALFDIMINISHED,
        14: HALFDIMINISHED_NINE,
        15: SUS,
        16: SUS_NINE,
        17: SUS_THIRTEEN,
        18: MAJ,
        19: MAJ_NINE,
        20: MAJ_SHARP_ELEVEN,
        21: MINOR_MAJ_SEVEN,
        22: MINOR_MAJ_SEVEN_NINE,
        23: MINOR_SIX,
        24: MINOR_SIX_NINE,
    }
    data_number_str: dict[int, str] = {
        1: 'm7',
        2: 'm9',
        3: 'm11',
        4: '7',
        5: '9',
        6: '13',
        7: '7(#11)',
        8: '7(b9)',
        9: '7(#9)',
        # 10: '7(b5)',
        10: '7(#5)',
        11: '7(b9,b13)',
        12: '7(#9,b13)',
        13: 'm7(b5)',
        14: 'm9(b5)',
        15: '7sus4',
        16: '9sus4',
        17: '13sus4',
        18: 'maj7',
        19: 'maj9',
        20: 'maj7(#11)',
        21: 'min(maj7)',
        22: 'min9(maj7)',
        23: 'min6',
        24: 'min6/9',
    }


