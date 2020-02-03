export function randInt(start, until) {
    var width = Math.max(0, until - start)
    return start + Math.floor(Math.random()*width)
}

export function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}
