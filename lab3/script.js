document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("mybtn").addEventListener("click", myFunction);
});

function myFunction(){
    main = document.querySelector(".main12");
    let div = document.createElement("div");
    div.className = "task";
    let p = document.createElement("p");
    p.innerHTML = document.getElementById("inputTask").value.trim();
    if(p.textContent === '') return;
    let btn = document.createElement("button");
    btn.className = "delete";
    btn.textContent = "delete";
    btn.addEventListener("click", function(){
        div.remove();
    })

    let btnDone = document.createElement("button");
    btnDone.textContent = "done";
    btnDone.className = "done";
    

    main.appendChild(div);
    div.appendChild(p);
    div.appendChild(btn);
    div.appendChild(btnDone);


    btnDone.addEventListener("click", function(){
        if(btnDone.textContent == "done"){
            p.style.textDecoration = "line-through";
            btnDone.textContent = "undone";
            btnDone.style.backgroundColor = "rgb(125,64,45)";
        } else if(btnDone.textContent == "undone") {
            p.style.textDecoration = "none";
            btnDone.textContent = "done";
            btnDone.style.backgroundColor = "rgb(74, 104, 235)";
        }
        
    })

    document.getElementById("inputTask").value = "";

}