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
    window.console.log('PlayerAreaStyling.getActionUIData()');
    window.console.log(action);
    switch (action.Type) {
        case 'Draw':
            return {
                Type: '不要',
                Data: action,
            }
        case 'Discard':
            switch (action.Source) {
                case 'NewHand':
                    return {
                        Type: '摸切',
                        Value: getUCharByTid(action.Value),
                        Preview: action.Preview,
                        Data: action,
                    }
                case 'OldHand':
                    return {
                        Type: '手切',
                        Value: getUCharByTid(action.Value),
                        Preview: action.Preview,
                        Data: action,
                    }
                default:
                    return undefined
            }
        case 'Tsumo':
            return {
                Type: '自摸',
                Value: action.Value.map(tids => getTidListStr(tids)).join(' '),
                Preview: action.Preview,
                Data: action,
            }
        case 'Ron':
            return {
                Type: '铳和',
                Value: action.Value.map(tids => getTidListStr(tids)).join(' '),
                Preview: action.Preview,
                Data: action,
            }
        case 'Chi':
            return {
                Type: '吃',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Preview: action.Preview,
                Data: action,
            }
        case 'Pon':
            return {
                Type: '碰',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Preview: action.Preview,
                Data: action,
            }
        case 'Kan0':
            return {
                Type: '暗杠',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Preview: action.Preview,
                Data: action,
            }
        case 'Kan1':
            return {
                Type: '大明杠',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Preview: action.Preview,
                Data: action,
            }
        case 'Kan2':
            return {
                Type: '加杠',
                Value: action.Value.map(tid => getUCharByTid(tid)).join(''),
                Preview: action.Preview,
                Data: action,
            }
        default:
            return undefined
    }
}

export const DrawResultTitleText = "流局";
export const TsumoResultTitleText = "自摸";
export const RonResultTitleText = "铳和";
export const DialogNextButtonText = "好的";
export const GameNameText = "索子麻雀练习";
export const MountainRemainingLabelText = "牌山";
export const ObserveButtonText = "观战";
export const PlayButtonText = "匹配";
export const MatchedText = "匹配完成.";
export const MatchingText = "正在寻找对手...";
export const GameEndShowResult = "显示成绩";
export const GameEndContinue = "返回大厅";

export const PatternDocs = {
    'RedDragonTriplet': {
        Name:'役牌·白',
        Desc:'手中有🀆的刻/杠。',
    }
};
