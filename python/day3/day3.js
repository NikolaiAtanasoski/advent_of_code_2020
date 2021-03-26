const path = require('path');
const fs = require('fs');

async function load_input(){
    var current_dir = path.dirname(__filename);
    return new Promise((resolve,reject) => {
        fs.readFile(path.join(current_dir, "day3_input.txt"),'utf-8', function (err, data) {
            if (err) {
                return reject(err);
            }
            resolve(data);
        })
    });
}


function countTrees(woods, steps_right, steps_down){
    let treeCounter = 0;
    let position = -steps_right
    let lineLength = woods[0].length
    for(current_row = 0; current_row < woods.length; current_row+=steps_down){
        position = (position + steps_right) % lineLength;
        if(woods[current_row].charAt(position) === "#"){
            treeCounter++;
        }
    }
    return treeCounter;
}

function countMultiple(woods,steps){
    answer = 1;
    steps.forEach(element => {
        stepsRight = element[0];
        stepsDown = element[1];
        answer *= countTrees(woods,stepsRight,stepsDown);
    });
    return answer;
}


async function main(){
    let woods = await load_input();
    woods = woods.split(/\r?\n/);

    let treeCount = countTrees(woods,3,1);
    console.log("tree count puzzle 1: " + treeCount);

    let steps = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    let treeCount2 = countMultiple(woods,steps);
    console.log("Answer puzzle 2: " + treeCount2)
    
}


// MAIN
main()