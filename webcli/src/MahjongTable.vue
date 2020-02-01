<template>
    <div>
        <div :style="myAriaStyle">
            <div class=river-row-0>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-1>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-2>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-3>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class='mountain-row-top'>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
            </div>
            <div class='mountain-row-bottom'>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
            </div>
              <div class='gap-tile-row'>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div id='hand'>
                  <span class='nonexisting-tile'>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div class='gap-tile-row'>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div class='built-sets-row'>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
              </div>

        </div>
        <div :style="oppositeAreaStyle">
            <div class=river-row-0>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-1>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-2>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-3>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class='mountain-row-top'>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
            </div>
            <div class='mountain-row-bottom'>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
            </div>
              <div class='gap-tile-row'>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div id='hand'>
                  <span class='nonexisting-tile'>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div class='gap-tile-row'>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div class='built-sets-row'>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
              </div>

        </div>
        <div :style="leftAreaStyle">
            <div class=river-row-0>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-1>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-2>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-3>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class='mountain-row-top'>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
            </div>
            <div class='mountain-row-bottom'>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
            </div>
              <div class='gap-tile-row'>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div id='hand'>
                  <span class='nonexisting-tile'>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div class='gap-tile-row'>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div class='built-sets-row'>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
              </div>

        </div>
        <div :style="rightAreaStyle">
            <div class=river-row-0>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-1>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-2>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'></span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class=river-row-3>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
                <span class='nonexisting-tile'>🀇</span>
            </div>
            <div class='mountain-row-top'>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
            </div>
            <div class='mountain-row-bottom'>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
                <span>🀫</span>
            </div>
              <div class='gap-tile-row'>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div id='hand'>
                  <span class='nonexisting-tile'>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div class='gap-tile-row'>
                  <span class='nonexisting-tile'>🀇</span>
              </div>
              <div class='built-sets-row'>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span class='nonexisting-tile'>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
                  <span>🀇</span>
              </div>

        </div>
    </div>
</template>

<script>
export default {
    name : 'MahjongTable',
    data: function(){
        return {
            myAriaStyle:{
                'font-size': '0',
                width: '314px',
                'max-width': '314px',
                height: '240px',
                'max-height': '240px',
                'text-align': 'center',
                position: 'absolute',
                top: '352px',
                left: '144px'
            },
            oppositeAreaStyle:{
                'font-size': '0',
                'width': '314px',
                'max-width': '314px',
                height: '240px',
                'max-height': '240px',
                'text-align': 'center',
                position: 'absolute',
                top: '0px',
                left: '144px',
                transform: 'rotate(-180deg)',
                '-webkit-transform': 'rotate(-180deg)',
                '-moz-transform': 'rotate(-180deg)',
                '-ms-transform': 'rotate(-180deg)',
                '-o-transform': 'rotate(-180deg)',
                filter: 'progid:DXImageTransform.Microsoft.BasicImage(rotation=2)'
            },
            leftAreaStyle:{
                'font-size': '0',
                width: '314px',
                'max-width': '314px',
                height: '240px',
                'max-height': '240px',
                'text-align': 'center',
                position: 'absolute',
                top: '176px',
                left: '-32px',
                transform: 'rotate(90deg)',
                '-webkit-transform': 'rotate(90deg)',
                '-moz-transform': 'rotate(90deg)',
                '-ms-transform': 'rotate(90deg)',
                '-o-transform': 'rotate(90deg)',
                filter: 'progid:DXImageTransform.Microsoft.BasicImage(rotation=1)'
            },
            rightAreaStyle:{
                'font-size': '0',
                width: '314px',
                'max-width': '314px',
                height: '240px',
                'max-height': '240px',
                'text-align': 'center',
                position: 'absolute',
                top: '176px',
                left: '320px',
                transform: 'rotate(-90deg)',
                '-webkit-transform': 'rotate(-90deg)',
                '-moz-transform': 'rotate(-90deg)',
                '-ms-transform': 'rotate(-90deg)',
                '-o-transform': 'rotate(-90deg)',
                filter: 'progid:DXImageTransform.Microsoft.BasicImage(rotation=1)'
            }
        }
    }
}
</script>

<style module>
.myArea {
    position: absolute;
    top: 352px;
    left: 144px;
}
.oppositeArea {
    position: absolute;
    top: 0px;
    left: 144px;
    transform: rotate(-180deg);
    -webkit-transform: rotate(-180deg);
    -moz-transform: rotate(-180deg);
    -ms-transform: rotate(-180deg);
    -o-transform: rotate(-180deg);
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
}
.leftArea {
    position: absolute;
    top: 176px;
    left: -32px;
    transform: rotate(90deg);
    -webkit-transform: rotate(90deg);
    -moz-transform: rotate(90deg);
    -ms-transform: rotate(90deg);
    -o-transform: rotate(90deg);
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
}
.rightArea {
    position: absolute;
    top: 176px;
    left: 320px;
    transform: rotate(-90deg);
    -webkit-transform: rotate(-90deg);
    -moz-transform: rotate(-90deg);
    -ms-transform: rotate(-90deg);
    -o-transform: rotate(-90deg);
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
}
.player {
    font-size: 0;
    width: 314px;
    max-width: 314px;
    height: 240px;
    max-height: 240px;
    text-align: center;
}
span {
    display: inline-block;
    font-size: 16px;
    width: 16px;
    max-width: 16px;
}
.rotate {
    display: inline-block;
    /* transform: rotate(-90deg); */
    /* -webkit-transform: rotate(-90deg);
    -moz-transform: rotate(-90deg);
    -ms-transform: rotate(-90deg);
    -o-transform: rotate(-90deg);
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3); */
}

.nonexisting-tile {
    visibility: hidden;
}
</style>
