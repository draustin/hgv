import hgv

def test_hgv():
    # Test property not present, no default.
    assert hgv.get(None,'p1') is None
    assert hgv.get('n1','p1') is None
    assert hgv.get('n1.sn1','p1') is None
    # Test property not present, default.
    assert hgv.get(None,'p1',1)==1
    assert hgv.get('n1','p1',1)==1
    assert hgv.get('n1.sn1','p1',1)==1
    # Test set at root
    hgv.set(None,'p1',0)
    assert hgv.get(None,'p1')==0
    assert hgv.get('n1','p1')==0
    assert hgv.get('n1.sn1','p1')==0
    # Test set level 1
    hgv.set('n1','p1',1)
    assert hgv.get(None,'p1')==0
    assert hgv.get('n1','p1')==1
    assert hgv.get('n1.sn1','p1')==1
    # Test set level 2
    hgv.set('n1.sn1','p1',2)
    assert hgv.get(None,'p1')==0
    assert hgv.get('n1','p1')==1
    assert hgv.get('n1.sn1','p1')==2
