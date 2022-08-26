function show(id) {

    const ele = document.getElementById(id);

    if (ele.style.display == "none"){
        ele.style.display = "block";
    }
    else{
        ele.style.display = "none";
    }

    const bolt = document.getElementById("light-bolt");

    if (bolt.style.color == "darkred"){
        bolt.style.color = "black";    
        
    }
    else {
        bolt.style.color = "darkred";
    }
  }