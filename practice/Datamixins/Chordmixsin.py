class ChordDataMixin:
    MINOR = []
    MINOR_NINE = []
    MINOR_ELEVEN = []
    SEPT = []
    SEPT_NINE = []
    SEPT_THIRTEEN = []
    SEPT_SHARP_ELEVEN = []
    SEPT_FLAT_NINE = []
    SEPT_SHARP_NINE = []
    SEPT_FLAT_FIVE = []
    SEPT_SHARP_FIVE = []
    SEPT_FLAT_NINE_FLAT_THIRTEEN = []
    SEPT_SHARP_NINE_FLAT_THIRTEEN = []
    HALFDIMINISHED = []
    HALFDIMINISHED_NINE = []
    SUS = []
    SUS_NINE = []
    SUS_THIRTEEN = []
    MAJ = []
    MAJ_NINE = []
    MAJ_SHARP_ELEVEN = []
    MINOR_MAJ_SEVEN = []
    MINOR_MAJ_SEVEN_NINE = []
    MINOR_SIX = []
    MINOR_SIX_NINE = []
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
        10: SEPT_FLAT_FIVE,
        11: SEPT_SHARP_FIVE,
        12: SEPT_FLAT_NINE_FLAT_THIRTEEN,
        13: SEPT_SHARP_NINE_FLAT_THIRTEEN,
        14: HALFDIMINISHED,
        15: HALFDIMINISHED_NINE,
        16: SUS,
        17: SUS_NINE,
        18: SUS_THIRTEEN,
        19: MAJ,
        20: MAJ_NINE,
        21: MAJ_SHARP_ELEVEN,
        22: MINOR_MAJ_SEVEN,
        23: MINOR_MAJ_SEVEN_NINE,
        24: MINOR_SIX,
        25: MINOR_SIX_NINE,
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
        10: '7(b5)',
        11: '7(#5)',
        12: '7(b9,b13)',
        13: '7(#9,b13)',
        14: 'm7(b5)',
        15: 'm9(b5)',
        16: '7sus4',
        17: '9sus4',
        18: '13sus4',
        19: 'maj7',
        20: 'maj9',
        21: 'maj7(#11)',
        22: 'min(maj7)',
        23: 'min9(maj7)',
        24: 'min6',
        25: 'min6/9',
    }


