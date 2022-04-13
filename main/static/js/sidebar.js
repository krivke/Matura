
var add_icons = Array.from(document.getElementsByClassName("plus-icon"))
console.log("h")
add_icons.forEach(icon=>{
    icon.addEventListener("click",function(){
        var icon_id = icon.dataset["id"];
        var form = document.getElementById(icon_id);
        if(form.style.display != "flex"){
            form.style.display = "flex";
        }else{
            
            form.style.display = "none";
        }
    })
})


