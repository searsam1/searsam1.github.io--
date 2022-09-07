
function displayElement(ele, displayTypeA,displayTypeB="none") {
    if (ele.style.display == displayTypeB){
        ele.style.display = displayTypeA;
    }
    else{
        ele.style.display = displayTypeB;
    }
}

function changeColor(ele, color1, color2) {
    if (ele.style.color == color2){
        ele.style.color = color1;
    }
    else{
        ele.style.color = color2;
    }
}

function show(id) {
    const sector = document
                    .getElementById(id)
                    .getElementsByClassName("sector")[0];
    displayElement(sector, "block")

  }


function clickMe(){
    alert("I was clicked")
}

