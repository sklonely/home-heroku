require('webduino-js');
require('webduino-blockly');
var myBoardVars = { board: 'Smart', device: '10yMEPey', transport: 'mqtt' };

var rgbled;
var led;
var myBoard;

boardReady(myBoardVars, true, function (board) {
    myBoard = board;
    board.systemReset();
    board.samplingInterval = 250;
    led = getLed(board, 13);
    led.on();
});


setTimeout(function () {
    throw 0;
}, 2500); 
