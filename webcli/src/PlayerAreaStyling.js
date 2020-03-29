var TileGroupChars = ['🀇','🀈','🀉','🀊','🀋','🀌','🀍','🀎','🀏','🀐','🀑','🀒','🀓','🀔','🀕','🀖','🀗','🀘','🀙','🀚','🀛','🀜','🀝','🀞','🀟','🀠','🀡','🀀','🀁','🀂','🀃','🀆','🀅','🀥']
var SeatChars = ['東','南','西','北']

function getUCharByTid(tid) {
    var gid = Math.floor(tid/4)
    return TileGroupChars[gid]
}

function getTidListStr(tids) {
    return tids.map(tid => getUCharByTid(tid)).join('')
}

export function getSeatChar(seat){
    return SeatChars[seat]
}

export function getTileViewChar(tileView) {
    if (tileView) {
        if (tileView.IsValueVisible) {
            return getUCharByTid(tileView.Value)
        } else {
            return '🀫'
        }
    } else {
        return undefined;
    }
}

export function getTileViewListStr(tileViews) {
    return tileViews.map(tv => getTileViewChar(tv)).join('');
}

export function getHandStr(gameStateView, seatID) {
    var oldHandStr = getTileViewListStr(gameStateView.AreaViews[seatID].OldHand);
    var newHandStr = getTileViewListStr(gameStateView.AreaViews[seatID].NewHand);
    return oldHandStr+' '+newHandStr;
}

export function getSetRowStr(gameStateView, seatID) {
    var setStrs = gameStateView.AreaViews[seatID].BuiltSets.map(bsv => getTileViewListStr(bsv.TileViews));
    return setStrs.join(' ');
}

export function getPatternValueStr(val) {
    return `${val}番`;
}

export function getPatternUIData(pattern) {
    var result = {};
    result.DisplayValue = getPatternValueStr(pattern.Value);

    switch (pattern.Name) {
        case 'RedDragonTriplet':
            result.DisplayName = '役牌·中';
            break;
        case 'GreenDragonTriplet':
            result.DisplayName = '役牌·发';
            break;
        case 'WhiteDragonTriplet':
            result.DisplayName = '役牌·白';
            break;
        case 'OneQuad':
            result.DisplayName = '单杠';
            break;
        case 'AllTriplets':
            result.DisplayName = '对对和';
            break;
        default:
            result.DisplayName = '???';
            break;
    }

    return result;
}

export function getActionUIData(action) {
    switch (action.Type) {
        case 'Draw':
            return {
                Type: 'Pass',
                Data: action,
            }
        case 'Discard':
            switch (action.Source) {
                case 'NewHand':
                    return {
                        Type: 'Discard*',
                        Value: getUCharByTid(action.Value),
                        Data: action,
                    }
                case 'OldHand':
                    return {
                        Type: 'Discard',
                        Value: getUCharByTid(action.Value),
                        Data: action,
                    }
                default:
                    return undefined
            }
        case 'Tsumo':
            return {
                Type: 'Tsumo',
                Value: action.Value.map(tids => getTidListStr(tids)).join(' '),
                Data: action,
            }
        case 'Ron':
            return {
                Type: 'Ron',
                Value: action.Value.map(tids => getTidListStr(tids)).join(' '),
                Data: action,
            }
        case 'Chi':
            return {
                Type: 'Chi',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Data: action,
            }
        case 'Pon':
            return {
                Type: 'Pon',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Data: action,
            }
        case 'Kan0':
            return {
                Type: 'Kan',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Data: action,
            }
        case 'Kan1':
            return {
                Type: 'Kan',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Data: action,
            }
        case 'Kan2':
            return {
                Type: 'Kan+',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Data: action,
            }
        default:
            return undefined
    }
}
