function show(id) {

    const ele = document.getElementById(id)

    if (ele.style.display == "none"){
        ele.style.display = "block"
    }
    else{
        ele.style.display = "none"
    }

  }