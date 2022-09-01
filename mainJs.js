
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
    const plusBtn = document
                    .getElementById(id)
                    .getElementsByClassName("plus-btn")[0];
    const h3 = document
                .getElementById(id)
                .getElementsByTagName("h3")[0];                    
    const minusBtn = document
                        .getElementById(id).
                        getElementsByClassName("minus-btn")[0];
    displayElement(sector, "block")
    displayElement(plusBtn, "none", "inline")
    displayElement(minusBtn, "inline")
    console.log(h3);
    changeColor(h3, "black", "darkblue");

  }