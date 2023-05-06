let minusButton = document.querySelectorAll(".minus");
let plusButton = document.querySelectorAll(".plus");

function minusCounter(){
    let obj = this.closest("div");
    let tagP = obj.querySelector(".amount");
    if (tagP.innerHTML > 1){
        tagP.innerHTML = Number(tagP.innerHTML) - 1
    }
    else{
        tagP.innerHTML = 1
    }
    obj.querySelector(".value").setAttribute("value",tagP.innerHTML); 
}

function plusCounter() {
    let obj = this.closest("div");
    let tagP = obj.querySelector(".amount");
    tagP.innerHTML = Number(tagP.innerHTML) + 1;
    obj.querySelector(".value").setAttribute("value",tagP.innerHTML);
}

for(let i of minusButton){
    i.addEventListener("click", minusCounter)
}


for(let i of plusButton){
    console.log(i)
    i.addEventListener("click", plusCounter)    
}