export function randInt(start, until) {
    var width = Math.max(0, until - start)
    return start + Math.floor(Math.random()*width)
}
