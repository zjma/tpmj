import random
import itertools

from copy import deepcopy
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def Check3X(tgids):
    if len(tgids)==0: return True
    if len(tgids)%3!=0: return False
    tgid = min(tgids)
    tgid0Count = len([None for x in tgids if x==tgid])
    if tgid in range(7) or tgid in range(9,16) or tgid in range(18,25):
        tgid1Count = len([None for x in tgids if x==tgid+1])
        tgid2Count = len([None for x in tgids if x==tgid+2])
        if tgid1Count>=1 and tgid2Count>=1:
            tmpTgids = list(tgids)
            tmpTgids.remove(tgid)
            tmpTgids.remove(tgid+1)
            tmpTgids.remove(tgid+2)
            if Check3X(tmpTgids): return True
    if tgid0Count>=3:
        tmpTgids = list(tgids)
        tmpTgids.remove(tgid)
        tmpTgids.remove(tgid)
        tmpTgids.remove(tgid)
        if Check3X(tmpTgids): return True
    return False

def Check3Xn2(tgids):
    if len(tgids)%3!=2: return False
    tg2c = [0 for _ in range(34)]
    for tgid in tgids: tg2c[tgid]+=1
    for tgid in range(34):
        if tg2c[tgid]>=2:
            tmpTgids = list(tgids)
            tmpTgids.remove(tgid)
            tmpTgids.remove(tgid)
            if Check3X(tmpTgids): return True
    return False

def CheckTriplet(tids, **kwargs):
    '''Check if the given tiles form a triplet.
    If ReturnTGID=True is given, return TileGroupID or None instead of boolean.
    '''
    if type(tids)!=list: return False
    if len(tids)!=3: return False
    if len(set(tids))!=3: return False
    tgids = [tid // 4 for tid in tids]

    if kwargs.get('ReturnTGID', False):
        if tgids[0]==tgids[1] and tgids[0]==tgids[2]:
            return tgids[0]
        else:
            return None

    return tgids[0]==tgids[1] and tgids[0]==tgids[2]

def CheckSequence(tids, **kwargs):
    '''Check if the given tiles form a sequence.
    If ReturnTGID=True is given, return TileGroupID or None instead of boolean.
    '''
    if type(tids)!=list: return False
    if len(tids)!=3: return False
    tids = sorted(tids)
    tgids = [tid // 4 for tid in tids]
    if kwargs.get('ReturnTGID', False):
        if tgids[0]+1==tgids[1] and tgids[1]+1==tgids[2] and (tgids[0] in range(0,7) or tgids[0] in range(9,16) or tgids[0] in range(18,25)):
            return sorted(tgids)[0]
        else:
            return None
    return tgids[0]+1==tgids[1] and tgids[1]+1==tgids[2] and (tgids[0] in range(0,7) or tgids[0] in range(9,16) or tgids[0] in range(18,25))

def CheckQuad(tids, **kwargs):
    '''Check if the given tiles form a quad.
    If ReturnTGID=True is given, return TileGroupID or None instead of boolean.
    '''
    if type(tids)!=list: return False
    if len(tids)!=4: return False
    if len(set(tids))!=4: return False
    tgids = [tid // 4 for tid in tids]

    if kwargs.get('ReturnTGID', False):
        if tgids[0]==tgids[1] and tgids[0]==tgids[2] and tgids[0]==tgids[3]:
            return tgids[0]
        else:
            return None

    return tgids[0]==tgids[1] and tgids[0]==tgids[2] and tgids[0]==tgids[3]

def CheckPair(tids, **kwargs):
    '''Check if the given tiles form a pair.
    If ReturnTGID=True is given, return TileGroupID or None instead of boolean.
    '''
    if type(tids)!=list: return False
    if len(tids)!=2: return False
    if len(set(tids))!=2: return False
    tgids = [tid // 4 for tid in tids]

    if kwargs.get('ReturnTGID', False):
        if tgids[0]==tgids[1]:
            return tgids[0]
        else:
            return None

    return tgids[0]==tgids[1]

def getWinRequestTileSet(req):
    result = set()
    for grp in req:
        for tid in grp:
            result.add(tid)
    return result

class Mountain:
    def __init__(self):
        tiles = list(range(36,72)) + list(range(108,136))
        random.shuffle(tiles)
        self._tiles = [
            [None]*6+tiles[:32],
            [None for _ in range(38)],
            [None]*6+tiles[32:],
            [None for _ in range(38)],
        ]
        i0 = random.randint(0,3)
        j0 = random.randint(0,37)
        self._forwardCursor = (i0,j0)
        self._backwordCursor = self._prevCursor(i0,j0)
    @property
    def tiles(self):
        return self._tiles
    def _ensureForwardCursorValid(self):
        attemptCount=0
        while attemptCount<999:
            i,j = self._forwardCursor
            if self._tiles[i][j]!=None: break
            self._forwardCursor = self._nextCursor(i,j)
            attemptCount+=1
        return attemptCount<999
    def _ensureBackwardCursorValid(self):
        attemptCount=0
        while attemptCount<999:
            i,j = self._backwordCursor
            if self._tiles[i][j]!=None: break
            self._backwordCursor = self._prevCursor(i,j)
            attemptCount+=1
        return attemptCount<999
    def draw(self):
        if len(self)==0: return None
        if not self._ensureForwardCursorValid(): return None
        i,j = self._forwardCursor
        result = self._tiles[i][j]
        self._tiles[i][j] = None
        return result
    def drawFromBack(self):
        if len(self)==0: return None
        if not self._ensureBackwardCursorValid(): return None
        i,j = self._backwordCursor
        result = self._tiles[i][j]
        self._tiles[i][j] = None
        return result
    def __len__(self):
        return len([x for x in (self._tiles[0]+self._tiles[2]) if x!=None])
    def getTilesBySeatID(self, seatID):
        return self._tiles[seatID]
    def _nextCursor(self, i, j):
        if j==37: return (i-1)%4,0
        return i,j+1
    def _prevCursor(self, i, j):
        if j==0: return (i+1)%4,37
        return i,j-1
class Set:
    def __init__(self, tiles):
        self._tiles = sorted(tiles)
    def toSetView(self):
        return {
            'TileViews' : [{'IsValueVisible':True,'Value':tid} for tid in sorted(self._tiles)],
        }
    def addTile(self, tid):
        self._tiles.append(tid)
        self._tiles.sort()
    def isTriplet(self): return CheckTriplet(self._tiles)
    def isSequence(self): return CheckSequence(self._tiles)
    def isQuad(self): return CheckQuad(self._tiles)
    def getTiles(self): return self._tiles
    @property
    def tiles(self): return self._tiles
class GameState:
    def __init__(self, player0, player1):
        self._PatternValues = {
            'OneQuad':1,
            'RedDragonTriplet':1,
            'GreenDragonTriplet':1,
            'WhiteDragonTriplet':1,
            'AllTriplets':2,
        }

        self._playerNames = [player0, player1]
        self._river = [
            [],
            [],
            [],
            [],
        ]
        self._mountain = Mountain()
        self._oldHand = [[],[],[],[]]
        self._newHand = [[],[],[],[]]
        self._matchedPatterns = [[],[],[],[]]

        for i in range(13):
            self._oldHand[0].append(self._mountain.draw())
            self._oldHand[2].append(self._mountain.draw())
        self._oldHand[0].sort()
        self._oldHand[2].sort()
        self._newHand[0].append(self._mountain.draw())
        self._builtSets = [[],[],[],[]]
        self._state = {
            'Main'  : 'PlayerXHandleDraw',
            'X'     : 0,
        }
    def getStateView(self, role):
        return {
            'AreaViews' : [
                self._getAreaViewBySeatID(0,role),
                self._getAreaViewBySeatID(1,role),
                self._getAreaViewBySeatID(2,role),
                self._getAreaViewBySeatID(3,role),
            ],
            'State' : self._state,
            'PlayerNames' : self._playerNames,
            'PatternValues':self._PatternValues,
            'MatchedPatterns':self._matchedPatterns,
        }

    def _getMountainViewBySeatID(self, seatID, role):
        if role==-1 or self._state['Main'] in ('PlayerXWon','Finished'):
            return [({'IsValueVisible':True,'Value':tid} if tid!=None else None) for tid in self._mountain.getTilesBySeatID(seatID)]
        return [({'IsValueVisible':False} if tid!=None else None) for tid in self._mountain.getTilesBySeatID(seatID)]

    def _getOldHandView(self, seatID, role):
        if role==-1 or seatID==self._getSeatIDByRole(role) or self._state['Main'] in ('PlayerXWon','Finished'):
            return [{'IsValueVisible':True,'Value':tid} for tid in self._oldHand[seatID]]
        return [{'IsValueVisible':False} for tid in self._oldHand[seatID]]

    def _getNewHandView(self, seatID, role):
        if role==-1 or seatID==self._getSeatIDByRole(role) or self._state['Main'] in ('PlayerXWon','Finished'):
            return [{'IsValueVisible':True,'Value':tid} for tid in self._newHand[seatID]]
        return [{'IsValueVisible':False} for tid in self._newHand[seatID]]

    def _getAreaViewBySeatID(self, seatID, role):
        '''
        Get what it looks like at seatID area from role's view.
        '''
        return {
            'River'     : [{'IsValueVisible':True,'Value':tid} for tid in self._river[seatID]],
            'Mountain'  : self._getMountainViewBySeatID(seatID, role),
            'OldHand'   : self._getOldHandView(seatID, role),
            'NewHand'   : self._getNewHandView(seatID, role),
            'BuiltSets' : [s.toSetView() for s in self._builtSets[seatID]],
        }
    def performAction(self, role, action):
        '''
        @return True if the action was accepted, or False otherwise.
        '''
        logger.info(f'OldState={self._state}')
        mainState = self._state.get('Main',None)
        try:
            if action==None: return False
            if mainState == 'PlayerXHandleDraw':
                if role==self._state.get('X',None):
                    seatID = self._getSeatIDByRole(role)
                    actionType = action.get('Type',None)
                    if actionType=='Discard':
                        src = action.get('Source', None)
                        tid = action.get('Value', None)
                        if src=='OldHand' and tid in self._oldHand[seatID] or src=='NewHand' and tid in self._newHand[seatID]:
                            fromOldHand = src=='OldHand'
                            self._discardFromHandToRiver(seatID,fromOldHand,tid)
                            self._organizeHand(seatID)
                            self._state = {'Main':'PlayerXToRespondToDiscard','X':1-role}
                            return True
                    if actionType=='Tsumo':
                        val = action.get('Value', [])
                        logger.debug(f'RequestedDecomposition={val}')
                        # Check if provided tiles matches what the player have in hand.
                        expectedTileSet = set(self._oldHand[seatID]+self._newHand[seatID])
                        actualTileSet = set(itertools.chain.from_iterable(val))
                        logger.debug(f'expectedTileSet={expectedTileSet}')
                        logger.debug(f'actualTileSet={actualTileSet}')
                        if actualTileSet != expectedTileSet: return False
                        # Check if the decomposition has 1 pair.
                        pairs = [0 for grp in val if CheckPair(grp)]
                        logger.debug(f'pairs={pairs}')
                        if len(pairs) != 1: return False
                        # Check if the decomposition has n-1 set.
                        sets = [0 for grp in val if CheckTriplet(grp) or CheckSequence(grp)]
                        logger.debug(f'sets={sets}')
                        if len(sets) != len(val)-1: return False
                        self._state = {'Main':'PlayerXWon','X':role}
                        self._updateMatchedPatterns(seatID, val)
                        return True
                    if actionType=='Kan0':
                        tids = action.get('Value',None)
                        logger.debug(f'tids={tids}')
                        if not CheckQuad(tids): return False
                        tidSet = set(tids)
                        handSet = set(self._oldHand[seatID]+self._newHand[seatID])
                        logger.debug(f'tidSet={tidSet}')
                        logger.debug(f'handSet={handSet}')
                        if tidSet&handSet!=tidSet: return False
                        logger.debug(f'MountainRemaining={len(self._mountain)}')
                        if len(self._mountain)<=0: return False
                        logger.debug('All check passed.')
                        self._buildSet(seatID, sorted(tids))
                        self._organizeHand(seatID)
                        self._drawTile(seatID)
                        self._state = {'Main':'PlayerXHandleDraw', 'X':role, 'IsKanDraw':True}
                        return True
                    if actionType=='Kan2':
                        tids = action.get('Value',None)
                        logger.debug(f'tids={tids}')
                        if not CheckQuad(tids): return False
                        logger.debug(f'MountainRemaining={len(self._mountain)}')
                        if len(self._mountain)<=0: return False
                        handSet = set(self._oldHand[seatID]+self._newHand[seatID])
                        logger.debug(f'handSet={handSet}')
                        tidSet = set(tids)
                        tidToAddToSet = None
                        sid = None
                        for idx,built in enumerate(self._builtSets[seatID]):
                            logger.debug(f'builtTiles={built.getTiles()}')
                            if not built.isTriplet(): continue
                            builtTileSet = set(built.getTiles())
                            if len(tidSet&handSet)==1 and len(tidSet&builtTileSet)==3:
                                tidToAddToSet = (tidSet&handSet).pop()
                                sid = idx
                                break
                        logger.debug(f'tidToAddToSet={tidToAddToSet}')
                        logger.debug(f'sid={sid}')
                        if sid==None: return False
                        logger.debug('All checks passed.')
                        self._removeTile(tidToAddToSet)
                        self._builtSets[seatID][sid].addTile(tidToAddToSet)
                        self._organizeHand(seatID)
                        self._drawTile(seatID)
                        self._state = {'Main':'PlayerXHandleDraw', 'X':role, 'IsKanDraw':True}
                        return True
            elif mainState == 'PlayerXToRespondToDiscard':
                if role==self._state.get('X',None):
                    seatID = self._getSeatIDByRole(role)
                    oppoRole = 1-role
                    oppoSeatID = self._getSeatIDByRole(oppoRole)
                    actionType = action.get('Type',None)
                    if actionType=='Draw':
                        if len(self._mountain)>=1:
                            self._drawTile(seatID)
                            self._state = {'Main':'PlayerXHandleDraw','X':role}
                        else:
                            self._state = {'Main':'Finished'}
                        return True
                    elif actionType=='Pon':
                        tids = action.get('Value', [])
                        if not CheckTriplet(tids): return False
                        tidSet = set(tids)
                        lastDiscardedSet = set(self._river[oppoSeatID][-1:])
                        oldHandSet = set(self._oldHand[seatID])
                        logger.debug(f'tidSet={tidSet}')
                        logger.debug(f'lastDiscardedSet={lastDiscardedSet}')
                        logger.debug(f'oldHandSet={oldHandSet}')
                        if len(tidSet&lastDiscardedSet)!=1: return False
                        if len(tidSet&oldHandSet)!=2: return False
                        #All checks pass.
                        self._buildSet(seatID, sorted(tids))
                        self._state = {'Main':'PlayerXHandleDraw', 'X':role}
                        return True
                    elif actionType=='Chi':
                        tids = action.get('Value', [])
                        if not CheckSequence(tids): return False
                        tidSet = set(tids)
                        lastDiscardedSet = set(self._river[oppoSeatID][-1:])
                        oldHandSet = set(self._oldHand[seatID])
                        logger.debug(f'tidSet={tidSet}')
                        logger.debug(f'lastDiscardedSet={lastDiscardedSet}')
                        logger.debug(f'oldHandSet={oldHandSet}')
                        if len(tidSet&lastDiscardedSet)!=1: return False
                        if len(tidSet&oldHandSet)!=2: return False
                        #All checks pass.
                        self._buildSet(seatID, sorted(tids))
                        self._state = {'Main':'PlayerXHandleDraw', 'X':role}
                        return True
                    elif actionType=='Ron':
                        val = action.get('Value', [])
                        logger.debug(f'RequestedDecomposition={val}')
                        # Check if provided tiles matches what the player have in hand.
                        expectedTileSet = set(self._oldHand[seatID]+self._river[oppoSeatID][-1:])
                        actualTileSet = set(itertools.chain.from_iterable(val))
                        logger.debug(f'expectedTileSet={expectedTileSet}')
                        logger.debug(f'actualTileSet={actualTileSet}')
                        if actualTileSet != expectedTileSet: return False
                        # Check if the decomposition has 1 pair.
                        pairs = [0 for grp in val if CheckPair(grp)]
                        logger.debug(f'pairs={pairs}')
                        if len(pairs) != 1: return False
                        # Check if the decomposition has n-1 set.
                        sets = [0 for grp in val if CheckTriplet(grp) or CheckSequence(grp)]
                        logger.debug(f'sets={sets}')
                        if len(sets) != len(val)-1: return False

                        self._state = {'Main':'PlayerXWon','X':role}
                        self._updateMatchedPatterns(seatID,val)
                        return True
                    elif actionType=='Kan1':
                        tids = action.get('Value', [])
                        if not CheckQuad(tids): return False
                        tidSet = set(tids)
                        lastDiscardedSet = set(self._river[oppoSeatID][-1:])
                        oldHandSet = set(self._oldHand[seatID])
                        logger.debug(f'tidSet={tidSet}')
                        logger.debug(f'lastDiscardedSet={lastDiscardedSet}')
                        logger.debug(f'oldHandSet={oldHandSet}')
                        if len(tidSet&lastDiscardedSet)!=1: return False
                        if len(tidSet&oldHandSet)!=3: return False
                        logger.debug(f'MountainRemaining={len(self._mountain)}')
                        if len(self._mountain)<=0: return False
                        #All checks pass.
                        self._buildSet(seatID, sorted(tids))
                        self._drawTile(seatID)
                        self._state = {'Main':'PlayerXHandleDraw', 'X':role, 'IsKanDraw':True}
                        return True
            return False
        finally:
            logger.info(f'NewState={self._state}')
    def _buildSet(self, builderSeatID, tiles):
        for tile in tiles:
            self._removeTile(tile)
        self._builtSets[builderSeatID].append(Set(tiles))
    def _removeTile(self, tid):
        '''
        Remove a given tile from whatever hand/river it is in currently.
        '''
        for seatID in range(4):
            self._removeIfExist(self._oldHand[seatID],tid)
            self._removeIfExist(self._newHand[seatID],tid)
            self._removeIfExist(self._river[seatID],tid)
    def _removeIfExist(self, lst, val):
        if val in lst: lst.remove(val)
    def _discardFromHandToRiver(self, seatID, fromOldHand, tid):
        assert seatID in [0,1,2,3]
        if fromOldHand:
            assert tid in self._oldHand[seatID]
            self._oldHand[seatID].remove(tid)
        else:
            assert tid in self._newHand[seatID]
            self._newHand[seatID].remove(tid)
        self._river[seatID].append(tid)

    def _organizeHand(self, seatID):
        assert seatID in [0,1,2,3]
        self._oldHand[seatID] = sorted(self._oldHand[seatID]+self._newHand[seatID])
        self._newHand[seatID] = []
    def _drawTile(self, seatID):
        assert seatID in [0,1,2,3]
        tid = self._mountain.draw()
        assert tid!=None
        self._newHand[seatID].append(tid)
    def _getSeatIDByRole(self, role):
        if role==0: return 0
        if role==1: return 2
        return None
    def finished(self):
        return self._state['Main'] in ('PlayerXWon','Finished')

    def _updateMatchedPatterns(self, seatID, handGroups):
        '''(Re-)calculate bonus patterns for winner.
        @params seatID      The winner's seatID.
        @params handGroups  How the tiles in hand is grouped into sets and pairs.
        @returns            List of patterns hit by the winner.
        '''
        self._matchedPatterns[seatID] = []

        for pattern,value in self._PatternValues.items():
            patternChecker = f"_check{pattern}"
            logger.debug(f'[_updateMatchedPatterns] invoking {patternChecker}.')
            if getattr(self, patternChecker)(seatID, handGroups):
                self._matchedPatterns[seatID].append(pattern)

    def _checkOneQuad(self, seatID, handGroups):
        return len([set for set in self._builtSets[seatID] if set.isQuad()])==1

    def _checkRedDragonTriplet(self, seatID, handGroups):
        tileGroups = handGroups + [set.getTiles() for set in self._builtSets[seatID]]
        for tileGroup in tileGroups:
            if CheckTriplet(tileGroup, ReturnTGID=True)==33 or CheckQuad(tileGroup, ReturnTGID=True)==33:
                return True
        return False

    def _checkGreenDragonTriplet(self, seatID, handGroups):
        tileGroups = handGroups + [set.getTiles() for set in self._builtSets[seatID]]
        for tileGroup in tileGroups:
            if CheckTriplet(tileGroup, ReturnTGID=True)==32 or CheckQuad(tileGroup, ReturnTGID=True)==32:
                return True
        return False

    def _checkWhiteDragonTriplet(self, seatID, handGroups):
        tileGroups = handGroups + [set.getTiles() for set in self._builtSets[seatID]]
        for tileGroup in tileGroups:
            if CheckTriplet(tileGroup, ReturnTGID=True)==31 or CheckQuad(tileGroup, ReturnTGID=True)==31:
                return True
        return False

    def _checkAllTriplets(self, seatID, handGroups):
        tileGroups = handGroups + [set.getTiles() for set in self._builtSets[seatID]]
        return len([0 for tileGroup in tileGroups if CheckTriplet(tileGroup)])==4

    def edit(self, request):
        logger.debug(f"Handling Edit request: {request}")
        cmd = request.get('Command', None)
        if cmd=='Swap':
            logger.debug(f"Handling Swap command.")
            locs = request.get('Locations', [])
            if type(locs)!=list or len(locs)!=2:
                logger.debug(f"Invalid locations.")
                return False
            area0 = locs[0].get('Area', None)
            seatID0 = locs[0].get('SeatID', None)
            idx0 = locs[0].get('Index', None)
            area1 = locs[1].get('Area', None)
            seatID1 = locs[1].get('SeatID', None)
            idx1 = locs[1].get('Index', None)
            tid0 = self.getTidByLocation(Area=area0, SeatID=seatID0, Index=idx0)
            tid1 = self.getTidByLocation(Area=area1, SeatID=seatID1, Index=idx1)
            logger.debug(f"tid0={tid0}")
            logger.debug(f"tid1={tid1}")
            if tid0==None or tid1==None:
                return False
            assert self.setTidByLocation(Area=area0, SeatID=seatID0, Index=idx0, NewValue=tid1)
            assert self.setTidByLocation(Area=area1, SeatID=seatID1, Index=idx1, NewValue=tid0)
            return True
        else:
            return False

    def getTidByLocation(self, **kwargs):
        area = kwargs.get('Area', None)
        seatID = kwargs.get('SeatID', None)
        index = kwargs.get('Index', None)
        logger.debug(f'[getTidByLocation]: area={area},seatID={seatID},index={index}')
        if seatID not in (0,1,2,3):
            logger.debug('Invalid seatID.')
            return None
        if area=='Mountain':
            tiles = self._mountain.tiles[seatID]
        elif area=='River':
            tiles = self._river[seatID]
        elif area=='OldHand':
            tiles = self._oldHand[seatID]
        elif area=='NewHand':
            tiles = self._newHand[seatID]
        elif area=='BuiltSet0' and len(self._builtSets)>=1:
            tiles = self._builtSets[seatID][0].getTiles()
        elif area=='BuiltSet1' and len(self._builtSets)>=2:
            tiles = self._builtSets[seatID][1].getTiles()
        elif area=='BuiltSet2' and len(self._builtSets)>=3:
            tiles = self._builtSets[seatID][2].getTiles()
        elif area=='BuiltSet3' and len(self._builtSets)>=4:
            tiles = self._builtSets[seatID][3].getTiles()
        else:
            tiles = []
        return tiles[index] if index>=0 and index<len(tiles) else None

    def setTidByLocation(self, **kwargs):
        area = kwargs.get('Area', None)
        seatID = kwargs.get('SeatID', None)
        index = kwargs.get('Index', None)
        newval = kwargs.get('NewValue', None)
        if newval not in range(136): return False
        if seatID not in (0,1,2,3): return False
        if area=='Mountain':
            tiles = self._mountain.tiles[seatID]
        elif area=='River':
            tiles = self._river[seatID]
        elif area=='OldHand':
            tiles = self._oldHand[seatID]
        elif area=='NewHand':
            tiles = self._newHand[seatID]
        elif area=='BuiltSet0' and len(self._builtSets)>=1:
            tiles = self._builtSets[seatID][0].tiles
        elif area=='BuiltSet1' and len(self._builtSets)>=2:
            tiles = self._builtSets[seatID][1].tiles
        elif area=='BuiltSet2' and len(self._builtSets)>=3:
            tiles = self._builtSets[seatID][2].tiles
        elif area=='BuiltSet3' and len(self._builtSets)>=4:
            tiles = self._builtSets[seatID][3].tiles
        else:
            return False

        if index>=0 and index<len(tiles):
            tiles[index] = newval
            return True
        return False
