function show(id) {

    const ele = document.getElementById(id).getElementsByClassName("sector")[0];

    if (ele.style.display == "none"){
        ele.style.display = "block";
    }
    else{
        ele.style.display = "none";
    }

    const plusBtn = document.getElementById(id).getElementsByClassName("plus-btn")[0]

    
    if (plusBtn.style.display == "none"){
        plusBtn.style.display = "inline";
    }
    else{
        plusBtn.style.display = "none";
    }

    const minusBtn = document.getElementById(id).getElementsByClassName("minus-btn")[0]

    
    if (minusBtn.style.display == "none"){
        minusBtn.style.display = "inline";
    }
    else{
        minusBtn.style.display = "none";
    }

  }