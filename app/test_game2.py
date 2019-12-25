import pytest
from game2 import *

def test_isvalidrole_true_with_east():
    assert isValidRole(0)

def test_isvalidrole_true_with_observer():
    assert isValidRole(-1)

def test_isvalidrole_false_with_invalid_role():
    assert not isValidRole(2)

def test_isvalidrole_false_with_invalid_type():
    assert not isValidRole('East')





def test_isvalidtile_true_with_1m():
    assert isValidTile(0)

def test_isvalidtile_true_with_5s():
    assert isValidTile(55)

def test_isvalidtile_true_with_red():
    assert isValidTile(135)

def test_isvalidtile_false_with_invalid_id():
    assert not isValidTile(136)
    assert not isValidTile(-1)

def test_isvalidtile_false_with_invalid_type():
    assert not isValidTile({'Value':123})






def test_isvalidtileview_true_with_covered():
    assert isValidTileView({
        'Covered':True}
    )

def test_isvalidtileview_true_with_open_3s():
    assert isValidTileView({
        'Covered'   :   False,
        'Tile'      :   45,
    })

def test_isvalidtileview_false_with_wrong_key():
    assert not isValidTileView({
        'Covered'   :   False,
        'tile'      :   45,
    })
    assert not isValidTileView({
        'covered'   :   False,
        'Tile'      :   45,
    })

def test_isvalidtileview_false_with_wrong_type():
    assert not isValidTile([])





def test_isvalidmountainview_true_with_full_covered():
    obj = [{'Covered':True} for _ in range(64)]
    assert isValidMountainView(obj)

def test_isvalidmountainview_true_with_empty():
    obj = [None for _ in range(64)]
    assert isValidMountainView(obj)

def test_isvalidmountainview_true_with_partial():
    obj = [None]*20+[{'Covered':False,'Tile':tid} for tid in range(44)]
    assert isValidMountainView(obj)

def test_isvalidmountainview_false_with_lacking_tile():
    obj = [None]*19+[{'Covered':False,'Tile':tid} for tid in range(44)]
    assert not isValidMountainView(obj)

def test_isvalidmountainview_false_with_invalid_tileview():
    obj = [None]*20+[tid for tid in range(44)]
    assert not isValidMountainView(obj)

def test_isvalidmountainview_false_with_wrong_type():
    obj = {}
    assert not isValidMountainView(obj)







def test_isvalidhand_true_with_1112p():
    obj = [
        {'Covered':False,'Tile':73},
        {'Covered':False,'Tile':74},
        {'Covered':False,'Tile':75},
        {'Covered':False,'Tile':76},
    ]
    assert isValidHand(obj)

def test_isvalidhand_true_with_allconcealed():
    obj = [
        {'Covered':True},
        {'Covered':True},
        {'Covered':True},
        {'Covered':True},
        {'Covered':True},
        {'Covered':True},
        {'Covered':True},
        {'Covered':True},
        {'Covered':True},
        {'Covered':True},
        {'Covered':True},
        {'Covered':True},
        {'Covered':True},
    ]
    assert isValidHand(obj)

def test_isvalidhand_true_with_empty():
    assert isValidHand([])

def test_isvalidhand_false_with_invalid_tileview():
    obj = [
        {'Covered':False,'Tile':73},
        {'Covered':False,'Tile':74},
        {'Covered':False,'Tile':333},
        {'Covered':False,'Tile':76},
    ]
    assert not isValidHand(obj)

def test_isvalidhand_false_with_wrong_type():
    assert not isValidHand(None)
    assert not isValidHand({})

def test_faceof_returns_with_red3():
    assert faceOf(135)=={'Type':'Red'}

def test_faceof_returns_with_9p2():
    assert faceOf(106)=={'Type':'Dot','Value':9}

def test_faceof_raises_with_invalid_tile_id():
    with pytest.raises(ValueError):
        faceOf(136)

    with pytest.raises(ValueError):
        faceOf(None)





# def test_isvalidtriplet_true_with_eee():
#     obj = [108,109,110]
#     assert isValidTripletInstance(obj)

# def test_isvalidtriplet_true_with_eee_reordered():
#     obj = [109,108,110]
#     assert isValidTripletInstance(obj)

# def test_isvalidtriplet_false_with_234s():
#     obj = [41,46,51]
#     assert not isValidTripletInstance(obj)
#
# def test_isvalidtriplet_false_with_22m():
#     obj = [5,6]
#     assert not isValidTripletInstance(obj)
