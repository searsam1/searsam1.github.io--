
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

function createTocLink(e, id_){
    var li = document.createElement("li");
    var a = document.createElement("a");
    var href = document.createAttribute("href")
    href.value = `#${id_}`
    a.setAttributeNode(href)
    a.textContent = e.textContent.trim(" ")
    li.appendChild(a)

    return li;
    

}

function createTOC(){
    headers = document.getElementsByClassName("header")
    toc = document.querySelector(".toc")
    console.log(toc)

    var i = 0;
    for (header of headers){
        var att = document.createAttribute("id")
        att.value = i;
        i++;
        header.setAttributeNode(att)
        
        toc.appendChild(createTocLink(header, att.value))
            
    }
}