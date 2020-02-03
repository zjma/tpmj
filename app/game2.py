import random
from copy import deepcopy

def isValidRole(obj):
    return type(obj)==int and obj in (-1,0,1)

def isValidTile(obj):
    return type(obj)==int and obj>=0 and obj<136

def isValidTileView(obj):
    return type(obj)==dict and \
            type(obj.get('Covered', None))==bool and \
            (obj['Covered'] or isValidTile(obj.get('Tile',None)))

def isValidMountainView(obj):
    return type(obj)==list and \
            len(obj)==64 and \
            all((item==None or isValidTileView(item)) for item in obj)

def isValidHand(obj):
    return type(obj)==list and \
            all(isValidTileView(item) for item in obj)

def faceOf(tile):
    if not isValidTile(tile): raise ValueError(f'tile={tile}')
    if tile < 0 or tile > 136: assert False
    if tile < 36: return {'Type':'Character','Value':tile//4+1}
    if tile < 72: return {'Type':'Bamboo','Value':(tile-36)//4+1}
    if tile < 108: return {'Type':'Dot','Value':(tile-72)//4+1}
    if tile < 112: return {'Type':'East'}
    if tile < 116: return {'Type':'South'}
    if tile < 120: return {'Type':'West'}
    if tile < 124: return {'Type':'North'}
    if tile < 128: return {'Type':'White'}
    if tile < 132: return {'Type':'Green'}
    return {'Type':'Red'}

def isValidTripletInstance(obj):
    if type(obj)!='list': return False
    if len(obj)!=3: return False
    if not all(isValidTileView(tile) for tile in obj): return False
    faces = [faceOf(tile) for tile in obj]
    if faces[0]==faces[1] and faces[0]==faces[2]: return True
    return False

def isValidSequenceInstance(obj):
    if type(obj)!='list': return False
    if len(obj)!=3: return False
    if not all(isValidTileView(tile) for tile in obj): return False
    faces = [faceOf(tile) for tile in obj]
    if not all(face['Type'] in ('Character','Bamboo','Dot') for face in faces):
        return False
    sorted_faces = sorted(faces, key=lambda face:face['Value'])
    if sorted_faces[0]['Value']+1!=sorted_faces[1]['Value']: return False
    if sorted_faces[1]['Value']+1!=sorted_faces[2]['Value']: return False
    return True

def isValidBuiltSet(obj):
    if type(obj)!=dict: return False
    typ = obj.get('Type',None)
    val = obj.get('Value',None)
    if not isValidSetType(typ): return False
    if typ=='Triplet' and not isValidTripletInstance(val): return False
    if typ=='Sequence' and not isValidSequenceInstance(val): return False
    if typ=='Quad' and not isValidQuadInstance(val): return False
    return True

def isValidBuiltSetList(obj):
    return type(obj)==list and \
            all(isValidBuiltSet(item) for item in obj)
def isValidPlayerStateView(obj):
    return type(obj)==dict and \
            isValidHand(obj.get('OldHand', None)) and \
            isValidHand(obj.get('NewHand', None)) and \
            isValidBuiltSetList(obj.get('BuiltSets', None)) and \
            isValidDiscarded(obj.get('Discarded', None))

def isValidGameStateView(obj):
    return type(obj)==dict and \
            isValidRole(obj.get('Role',None)) and \
            isValidMountainView(obj.get('MountainView', None)) and \
            type(obj.get('PlayerStates',None))==list and \
            all(isValidPlayerStateView(v) for v in obj['PlayerStates']) and \
            isValidStateHint(obj.get('StateHint', None))


def remainingDrawCount(mountain):
    return len([x for x in mountain if x!=None])

def _draw(mountain):
    if remainingDrawCount(mountain)==0:
        raise Exception('Drawing from an empty mountain')
    sel = min([(idx,val) for idx,val in enumerate(mountain) if val!=None])
    new_mountain = deepcopy(mountain)
    new_mountain[sel[0]] = None
    draw = sel[1]
    return new_mountain,draw

def getGameStateView(gameState, role):
    if role == -1:
        return gameState

    if role in (0,1):
        return {
            'Role'          :   role,
            'MountainCount' :   remainingDrawCount(gameState['Mountain']),
            'MyState'       :   gameState['PlayerStates'][role],
            'StateHint'     :   gameState['StateHint'],
        }

    assert False

def getActionOptions(gameStateView):
    if gameStateView['StateHint']['Finished']: return []
    if gameStateView['Role']==0:
        if gameStateView['StateHint']['Type']=='P0ToHandleDraw':
            return [{'Type':'DiscardDraw'}]
        return []
    if gameStateView['Role']==1:
        if gameStateView['StateHint']['Type']=='P1ToHandleDraw':
            return [{'Type':'DiscardDraw'}]
        return []
    return []

def tryPerformAction(state, role, action):
    if state['StateHint']['Finished']: return False,state
    if state['StateHint']['Type']=='P0ToHandleDraw':
        if role!=0: return False,state
        if action['Type']=='DiscardDraw':
            newState = deepcopy(state)
            newState['PlayerStates'][0]['Draw'] = None
            if remainingDrawCount(newState['Mountain'])==0:
                newState['StateHint']={'Finished':True}
            else:
                newState['Mountain'],newState['PlayerStates'][1]['Draw'] = _draw(state['Mountain'])
                newState['StateHint']['Type']='P1ToHandleDraw'
            return True,newState
        return False,state
    if state['StateHint']['Type']=='P1ToHandleDraw':
        if role!=1: return False,state
        if action['Type']=='DiscardDraw':
            newState = deepcopy(state)
            newState['PlayerStates'][1]['Draw'] = None
            if remainingDrawCount(newState['Mountain'])==0:
                newState['StateHint']={'Finished':True}
            else:
                newState['Mountain'],newState['PlayerStates'][0]['Draw'] = _draw(state['Mountain'])
                newState['StateHint']['Type']='P0ToHandleDraw'
            return True,newState
        return False,state
    assert False

def newMountain():
    ret = list(range(36,72)) + list(range(108,136))
    random.shuffle(ret)
    return ret

def newGameState():
    mountain = newMountain()
    hands = [[],[]]
    for i in range(13):
        for player_idx in range(2):
            mountain,draw = _draw(mountain)
            hands[player_idx].append(draw)

    mountain,p0_draw = _draw(mountain)

    return {
        'Mountain': mountain,
        'Rivers': [
            [],
            [],
        ],
        'PlayerStates':[
            {
                'Hand':hands[0],
                'Draw':p0_draw,
            },
            {
                'Hand':hands[1],
                'Draw':None,
            },
        ],
        'StateHint':{
            'Finished'  :   False,
            'Type'      :   'P0ToHandleDraw',
        },
    }
