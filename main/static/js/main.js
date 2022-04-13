

/*Izaberi button*/
var main_btn = document.querySelector(".main-btn");

main_btn.addEventListener("mouseover",function(){
	main_btn.style.backgroundColor = "var(--light-blue)"
	main_btn.style.border = "none"
	main_btn.style.color = "white"
	
})
main_btn.addEventListener("mouseout",function(){
	main_btn.style.border = "1px solid var(--light-blue)";
	main_btn.style.color = "var(--light-blue)";
	main_btn.style.backgroundColor = "initial"
})



/*SMOOTH SCROLL JQUERY IZABERI BUTTON*/

$(".button-scroll").on("click",function(e){
	//console.log(this.hash);
	if(this.hash !== ""){
		e.preventDefault();
	}
	const hash = this.hash;
	$("html,body").animate({
		scrollTop:$(hash).offset().top
	},500)

})


//izbrise success message iz kontakt forme
var x = document.querySelector(".remove-message");
if(x){
	x.addEventListener("click",function(e){
	e.preventDefault();
	var message = document.querySelector(".contact-message");
	
	message.style.display ="none"
})
}

//scroll do error message kod kontakt forme da znaju da nisi uspjeli poslat mail
var error_message = document.getElementById("error-message");

if(error_message){
	error_message.scrollIntoView({behavior: 'smooth', block: 'start'}); 
}