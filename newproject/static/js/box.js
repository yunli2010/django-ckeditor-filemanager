var open_box = false;

function showVideo(video_name){
	if(open_box == false){
		open_box = true;
		$("gClose").removeEvents("click");
		$("gSheet").removeEvents("dblclick"); 

		$("loadingmsg").innerHTML = "&nbsp; Please be patient, this video may take a while to load.";

		$("gSheet").setStyles({ 'top': -$(window).getScroll().y,'height':$(window).getScrollSize().y+$(window).getScroll().y, "display":"block" });
		var fadeFx = new Fx.Style("gSheet", 'opacity', {wait: false, duration: 300}).set(0);
		fadeFx.start(0.8);

		$("gBox").style.display = 'block';
		$("gBox").setStyles({
			'top': $(window).getScroll().y+30,
			'left': (($(window).getScrollSize().x/2)-(550/2)) + "px",
			'width': "456px",
			'height': "380px",
		});
		$("iFrame").setStyles({
			'width': "450px",
			'height': "360px",
		});

		$("iFrame").src = '/video/' + video_name + '/';

		$("gSheet").addEvent("dblclick", function(){
			closeBox();
		});
		$("giClose").addEvent("click", function(){
			closeBox();
		});
	}
}

function closeBox(){
	$("gBox").style.display = 'none';
	$("iFrame").src = '/video/null/';
	var fadeFx = new Fx.Style("gSheet", 'opacity', {wait: false, duration: 300, onComplete: function(){open_box = false} }).set(0.8);
	fadeFx.start(0);
}
function closeSheet(){
	var fadeFx = new Fx.Style("gSheet", 'opacity', {wait: false, duration: 300, onComplete: function(){open_box = false} }).set(0.8);
	fadeFx.start(0);
}
