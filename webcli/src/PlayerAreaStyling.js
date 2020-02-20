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
