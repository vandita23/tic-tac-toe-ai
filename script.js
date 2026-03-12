let board=["","","","","","","","",""]

let container=document.getElementById("board")

for(let i=0;i<9;i++){

let cell=document.createElement("div")

cell.className="cell"

cell.dataset.index=i

cell.onclick=playerMove

container.appendChild(cell)

}

async function playerMove(){

let i=this.dataset.index

if(board[i]!="") return

board[i]="X"

this.innerText="X"

await aiMove()

}

async function aiMove(){

let res=await fetch("http://127.0.0.1:5000/move",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({board:board})

})

let data=await res.json()

let move=data.move

if(move!=-1){

board[move]="O"

document.querySelectorAll(".cell")[move].innerText="O"

}

}