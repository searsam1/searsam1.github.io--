function show(id,id_2) {
    const elem = document.getElementById(id_2);

    if (elem.style.transform == "rotate(90deg)"){
        document.getElementById(id_2).style.transform = "rotate(0deg)"
    }
    else{
        document.getElementById(id_2).style.transform = "rotate(90deg)"
    }
    const ele2 = document.getElementById(id)

    if (ele2.style.display == "none"){
        ele2.style.display = "block"
    }
    else{
        ele2.style.display = "none"
    }

    

        
  }