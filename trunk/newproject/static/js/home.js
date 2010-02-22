var MyJSON;
var selected_image = 1;
window.addEvent("domready", function(){
	var request = new Request.JSON({
		url: '/homeimages/',
		onComplete: function(jsonObj) { MyJSON = jsonObj; }
    }).send();
})

window.addEvent("load", function(){
	startLoop();
})

function startLoop(){
	LoopOut();
}

function LoopOut(){
	var fadeFx = new Fx.Style("fader", 'opacity', {wait: false, duration: 5000, onComplete: LoopIn}).set(1);
	fadeFx.start(0);
}

function LoopIn(){	
	var list_image, list_caption;
	var c = 0;
	MyJSON.each(function(row) {
		if(c == selected_image){
			list_image = row["fields"]["image"];
			list_caption = row["fields"]["caption"];
		}
		c++;
	});
	if(selected_image > c-2){
		selected_image = 0;
	}else{
		selected_image = selected_image + 1;
	}

	$("homeCaption").innerHTML = list_caption;
	$("fader").style.backgroundImage = "url(/static/" + list_image + ")";
	
	var fadeFx = new Fx.Style("fader", 'opacity', {wait: false, duration: 5000, onComplete: LoopOut}).set(0);
	fadeFx.start(1);
}
