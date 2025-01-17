import pynmea2


def test_rdig():
    data = '$PRDIG,H,197.34,P,-10.2,R,-11.5,D,122.7,7*65'
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.rdi.RDIG
    assert msg.manufacturer == 'RDI'
    assert msg.sentence_type == 'RDIG'
    assert msg.head_id == 'H'
    assert msg.heading == 197.34
    assert msg.pitch_id == 'P'
    assert msg.pitch == -10.2
    assert msg.roll_id == 'R'
    assert msg.roll == -11.5
    assert msg.depth_id == 'D'
    assert msg.depth == 122.7
    assert msg.render() == data


def test_rdih():
    data = '$PRDIH,R,143.2,S,1.485,C,192.93*17'
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.rdi.RDIH
    assert msg.manufacturer == 'RDI'
    assert msg.sentence_type == 'RDIH'
    assert msg.altitude_id == 'R'
    assert msg.altitude == 143.2
    assert msg.sv_id == 'S'
    assert msg.sv == 1.485
    assert msg.sh_id == 'C'
    assert msg.sh == 192.93
    assert msg.render() == data


def test_rdii():
    data = '$PRDII,S,1.503,C,203.5*55'
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.rdi.RDII
    assert msg.manufacturer == 'RDI'
    assert msg.sentence_type == 'RDII'
    assert msg.rv_id == 'S'
    assert msg.rv == 1.503
    assert msg.rh_id == 'C'
    assert msg.rh == 203.5
