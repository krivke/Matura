/*navbar links*/
var nonetoblock = anime({
	targets:"#mobile-links li",
	opacity:1,
	duration:5000,
	autoplay:false,
	
	delay:function(el,i,t){return i*300},
	
	
});


function myFunction(){
	var mobile_links = document.getElementById("mobile-links");

	mobile_links.classList.toggle("blokaj");
	nonetoblock.play();
	nonetoblock.restart()
	

		
}



/*SMOOTH SCROLL JQUERY NAVBAR */

$(".mobile-links a,#myLinks a").on("click",function(e){
	if(this.hash !== ""){
		e.preventDefault();
	}
	const hash = this.hash;
	$("html,body").animate({
		scrollTop:$(hash).offset().top
	},500)

})



