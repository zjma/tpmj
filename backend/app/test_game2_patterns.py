import pytest
from game2 import *

def test_updateMatchedPatterns_RedDragonQuad():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([132,133,134,135]),Set([80,81,82])],[],[],[]]
    gameState._updateMatchedPatterns(0,[[4,8,12],[16,20,24],[25,26]])
    assert sorted(gameState._matchedPatterns[0])==sorted(['RedDragonTriplet','OneQuad'])

### OneQuad

def test_checkOneQuad_TrueWith1Quad():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23]),Set([80,81,82])],[],[],[]]
    assert gameState._checkOneQuad(0,[[4,8,12],[16,20,24],[25,26]])

def test_checkOneQuad_FalseWith2Quads():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23]),Set([83,80,81,82])],[],[],[]]
    assert not gameState._checkOneQuad(0,[[4,8,12],[16,20,24],[25,26]])

def test_checkOneQuad_FalseWith0Quads():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22]),Set([83,81,82])],[],[],[]]
    assert not gameState._checkOneQuad(0,[[4,8,12],[16,20,24],[25,26]])


### RedDragonTriplet

def test_checkRedDragonTriplet_TrueWithConcealedTriplet():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23])],[],[],[]]
    assert gameState._checkRedDragonTriplet(0,[[132,133,135],[16,20,24],[25,26]])

def test_checkRedDragonTriplet_TrueWithBuiltTriplet():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23]),Set([132,133,135])],[],[],[]]
    assert gameState._checkRedDragonTriplet(0,[[4,8,12],[16,20,24],[25,26]])

def test_checkRedDragonTriplet_TrueWithBuiltQuad():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23]),Set([132,133,135,134])],[],[],[]]
    assert gameState._checkRedDragonTriplet(0,[[4,8,12],[16,20,24],[25,26]])

def test_checkRedDragonTriplet_FalseOtherwise():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23]),Set([80,81,82])],[],[],[]]
    assert not gameState._checkRedDragonTriplet(0,[[4,8,12],[16,20,24],[25,26]])


### GreenDragonTriplet

def test_checkGreenDragonTriplet_TrueWithConcealedTriplet():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23])],[],[],[]]
    assert gameState._checkGreenDragonTriplet(0,[[128,129,131],[16,20,24],[25,26]])

def test_checkGreenDragonTriplet_TrueWithBuiltTriplet():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23]),Set([128,129,131])],[],[],[]]
    assert gameState._checkGreenDragonTriplet(0,[[4,8,12],[16,20,24],[25,26]])

def test_checkGreenDragonTriplet_TrueWithBuiltQuad():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23]),Set([128,129,131,130])],[],[],[]]
    assert gameState._checkGreenDragonTriplet(0,[[4,8,12],[16,20,24],[25,26]])

def test_checkGreenDragonTriplet_FalseOtherwise():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23]),Set([80,81,82])],[],[],[]]
    assert not gameState._checkGreenDragonTriplet(0,[[4,8,12],[16,20,24],[25,26]])


### WhiteDragonTriplet

def test_checkWhiteDragonTriplet_TrueWithConcealedTriplet():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23])],[],[],[]]
    assert gameState._checkWhiteDragonTriplet(0,[[124,125,127],[16,20,24],[25,26]])

def test_checkWhiteDragonTriplet_TrueWithBuiltTriplet():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23]),Set([124,125,127])],[],[],[]]
    assert gameState._checkWhiteDragonTriplet(0,[[4,8,12],[16,20,24],[25,26]])

def test_checkWhiteDragonTriplet_TrueWithBuiltQuad():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23]),Set([124,125,127,126])],[],[],[]]
    assert gameState._checkWhiteDragonTriplet(0,[[4,8,12],[16,20,24],[25,26]])

def test_checkWhiteDragonTriplet_FalseOtherwise():
    gameState = GameState('p0','p1')
    gameState._builtSets = [[Set([20,21,22,23]),Set([80,81,82])],[],[],[]]
    assert not gameState._checkWhiteDragonTriplet(0,[[4,8,12],[16,20,24],[25,26]])
