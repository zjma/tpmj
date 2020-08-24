import Sound1 from './assets/sound/sound1.wav';
import Sound5 from './assets/sound/sound5.wav';
import Sound6 from './assets/sound/sound6.wav';
import Sound8 from './assets/sound/sound8.wav';
import Sound9 from './assets/sound/sound9.wav';
import Sound18 from './assets/sound/sound18.wav';
import Sound21 from './assets/sound/sound21.wav';
import Sound27 from './assets/sound/sound27.wav';
import Sound45 from './assets/sound/sound45.wav';
import Sound54 from './assets/sound/sound54.wav';
import Sound65 from './assets/sound/sound65.wav';
import Sound111 from './assets/sound/sound111.wav';
import Sound528 from './assets/sound/sound528.wav';

var Sounds = {
    'DrewTile':Sound111,
    'Pon':Sound18,
    'Chi':Sound65,
    'Kan':Sound45,
    'FastReSet':Sound21,
    'Tsumo':Sound54,
    'Ron':Sound9,
    'End':Sound27,
    'DiscardedNew':Sound5,
    'DiscardedOld':Sound6,
    'GameStarted':Sound1,
    'NormalAction':Sound8,
    'Attention':Sound528,
};

export function play(soundName){
    if (soundName in Sounds) {
        var element = document.getElementById('SoundPlayer');
        element.setAttribute('src', Sounds[soundName]);
        element.play();
    } else {
        window.console.warn(`Unregistered sound: ${soundName}`);
    }
}
