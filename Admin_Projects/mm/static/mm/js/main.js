//alert("main.js");


/******************************************************
	constants
 ******************************************************/

var cname_White = "white";
var cname_Red = "red";
var cname_Yellow = "yellow";
var cname_LightBlue = "LightBlue";
var cname_Plum = "Plum";
var cname_Moccasin = "Moccasin";

var className_BT_Numbering_List = "bt_Numbering_List";

var TIME_FADE_IN = 300;
var TIME_FADE_OUT = 300;

/******************************************************
	funcs : ready
 ******************************************************/
$(document).ready(function() {
	
	//debug
	var datetime = get_Timelabel_Now();
//	var currentdate = new Date();
//	var datetime = "Last Sync: " + currentdate.getDay() + "/"+currentdate.getMonth() 
//		+ "/" + currentdate.getFullYear() + " @ " 
//		+ currentdate.getHours() + ":" 
//		+ currentdate.getMinutes() + ":" + currentdate.getSeconds();
		
	console.log("ready!" + " " + datetime);
//	console.log("ready!");
	
//    $("button").click(function(event) {
//    	
//    	//ref http://www.mysamplecode.com/2012/05/jquery-get-button-value-clicked.html
////        alert(event.target.id);
//    	var class_Name = $(this).attr('class');
////    	var tmp = $(this).attr('class');
////    	var tmp = $(this).attr('id');
////    	var tmp = $(this).prop("value");
//
////    	alert("tmp => " + tmp);
//        
//    	if (class_Name == className_BT_Numbering_List) {
//
//		} else {
//
//			console.log("Unknown class name : '" + class_Name + "'");
//
//		}//if (class_Name == )
//		
//    	
//    });
});

/******************************************************
funcs : general
******************************************************/
function show_Message(msg) {
	
	alert(msg);
	
}//function show_Message(msg) {

//ref https://stackoverflow.com/questions/21294302/converting-milliseconds-to-minutes-and-seconds-with-javascript#21294619
function millisToMinutesAndSeconds(millis) {
	
//	alert(millis);
	
	  var minutes = Math.floor(millis / 60000);
	  
	  var residue_Minutes = millis % 60000;
	  
	  var seconds = Math.floor(residue_Minutes / 1000);
//	  var seconds = (residue_Minutes / 1000).toFixed(0);
//	  var seconds = ((millis % 60000) / 1000).toFixed(0);
	  
	  var mill = millis - (minutes * 60000) - (seconds * 1000);
	  
	  //log
	  var msg_log = "millis => " + millis
					+ " "
		  			+ "residue_Minutes => " + residue_Minutes
		  			+ " "
		  			+ "mill => " + mill
	  				+ " "
	  				+ "minutes = " + minutes
	  				+ " "
	  				+ "seconds = " + seconds;
//	  console.log(msg_log);
	  
	  mill = (mill < 10 ? '00' : (mill < 100 ? '0' : "")) + mill;
	  
	  return minutes + ":" + (seconds < 10 ? '0' : '') + seconds
	  			+ "."
	  			+ mill;
//	  return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
	  
}

/*
 * https://stackoverflow.com/questions/5999209/how-to-get-the-background-color-code-of-an-element
 * answered May 14 '11 at 2:37
 */
function hexc(colorval) {
    var parts = colorval.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    delete(parts[0]);
    for (var i = 1; i <= 3; ++i) {
        parts[i] = parseInt(parts[i]).toString(16);
        if (parts[i].length == 1) parts[i] = '0' + parts[i];
    }
    color = '#' + parts.join('');
    
    return color;
}

function im_Action(_param) {
	
	/***************************
		validate : update date
	 ***************************/
	var _update;
	
	if ((_param == "11-0") ||
		(_param == "10-1")) {
//		if (_param == "11-0") {

		var tag_Date = $("input#ipt_IM_Update_Date");
		
		_update = tag_Date.val();
//		var update = tag_Date.val();
		
		if (_update == "") {

			alert("update ==> blank");

			return;
			
		} else if (_update == null) {

			alert("update ==> null");

			return;
			
		} else {
			
//			alert("_update ==> '" + _update + "'");
			
		}//if (update == "")

	}//if (_param == "11-0")
		
	/***************************
		operations
	 ***************************/
//	alert("!!param is => '" + _param + "'");
	
	//debug
	var td = $("td#td_Label_" + _param);
	
	//test
	var x = td.css('backgroundColor');
	var hex = hexc(x);
	
	/***************************
		set : color
	 ***************************/
	var color_New = "";
	
	if (hex == "#ffffff") {

		color_New = "#ffff00";

	} else {

		color_New = "#ffffff";

	}//if (hex == "#ffffff")
	
	
	td.css("background", color_New);
	
	/***************************
		return : if set to white
	 ***************************/
	if (color_New == "#ffffff") {
		
		return;
		
	}
	
	/***************************
		bg-color
	 ***************************/
	var div_Result = $('div#index_Area__Result');
	
	div_Result.css("background", cname_Plum);
	
	var tag = $('div#index_Message_Area');
	tag.html(_param);
//	$('div#index_Message_Area').html(_param);
	
	tag
		.fadeIn(200).fadeOut(200)
		.fadeIn(200).fadeOut(200)
		
		.fadeIn(200).fadeOut(200)
		.fadeIn(200).fadeOut(200)
		
		.fadeIn(200).fadeOut(200)
		.fadeIn(200).fadeOut(200)
		
		.fadeIn(200);

	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/im/im_actions";
//	var _url = "http://127.0.0.1:8000/im/actions";
	
	/***************************
		param
	 ***************************/
	var _data;
	
	//ref multiple conditions https://stackoverflow.com/questions/8710442/how-to-specify-multiple-conditions-in-an-if-statement-in-javascript answered Jan 3 '12 at 9:58
	if ((_param == "11-0") || 
			(_param == "10-1")) {
//		if (_param == "11-0") {

		_data = {action : _param, update : _update};

	} else {

		_data = {action : _param};

	}//if (_param == "11-0")
	
	$.ajax({
		
	    url: _url,
	    type: "GET",
	    //REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
	    data: _data,
	    
	    timeout: 10000
	    
	}).done(function(data, status, xhr) {

		/***************************
			exception
		 ***************************/
		var substr = "total_data";
//		var substr = "doesn't";
		
//		alert(data);
		
	//	var res = (data.indexOf(substr) !== -1);
		
		//ref substring https://stackoverflow.com/questions/1789945/how-to-check-whether-a-string-contains-a-substring-in-javascript
//		if (data.indexOf(substr) == -1) {
		if (data.includes(substr)) {	// detected
//			if (data.indexOf(substr) !== -1) {	// detected
			
			//debug
			console.log("'doesn't' ==> detected");
			
//			alert(data);
			
			var tag = $('div#index_Area__Result');
			
			$('div#index_Area__Result')
				.css("background", cname_Red);

//			tag
//			.animate({background : "red"}, 500)
//			.animate({background : "yellow"}, 500)
//			.animate({background : "white"}, 500)
			
			;

			$('div#index_Area__Result').html(data);
			
//			//ref
//			tag
//				.animate({background : "red"}, 500)
//				.animate({background : "yellow"}, 500)
//				.animate({background : "white"}, 500)
//				
//				;
			
			//ref fadein/out https://stackoverflow.com/questions/275931/how-do-you-make-an-element-flash-in-jquery answered Feb 1 '12 at 14:19
			tag
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				
				.fadeIn(200);
			
		} else if (data.includes("ERROR")) {	// detected
//		} else if (data.includes("no entries")) {	// detected
				
				//debug
				console.log("local image files => no entries");
				
				var tag = $('div#index_Area__Result');
				
				$('div#index_Area__Result')
				.css("background", cname_Red);
				
				$('div#index_Area__Result').html(data);
				
				//ref fadein/out https://stackoverflow.com/questions/275931/how-do-you-make-an-element-flash-in-jquery answered Feb 1 '12 at 14:19
				tag
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				
				.fadeIn(200);
				
		} else {
			
			var tag = $('div#index_Area__Result');
			
			$('div#index_Area__Result')
				.css("background", cname_LightBlue);
//			.css("background", cname_White);

			$('div#index_Area__Result').html(data);

			tag
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				.fadeIn(200).fadeOut(200)
				
//				.fadeIn(200).fadeOut(200)
//				.fadeIn(200).fadeOut(200)
//				
//				.fadeIn(200).fadeOut(200)
//				.fadeIn(200).fadeOut(200)
				
				.fadeIn(200);

		}

		
//		$('div#index_Area__Result').html(data);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
	});

}//function im_Action(param) {

function curr_BUSL_3__Action(_param) {
	
//	//debug
//	alert("_param => " + _param);
	
	/***************************
		bg-color : change
	 ***************************/
	var td = $("td#td_Label_" + _param);
	
	td.css("background", cname_Yellow);

	// bg-color
	// disp html
	var div_MessageArea = $("div#curr_BUSL_2__Message_Area");
	
	div_MessageArea.css("background", cname_White);
	
	var msg = "ajax starting...";
	
	div_MessageArea.html(msg);

//	//debug
//	alert("ajax starting...");
	
	/***************************
		get : param
	 ***************************/
	
	/***************************
		ajax : prep
		
	 ***************************/
	var _url = "http://127.0.0.1:8000/curr/tester_BuyUps_SellLows__V2";
//	var _url = "http://127.0.0.1:8000/curr/tester_BuyUps_SellLows";

	_data = {
			
		"param" : _param
			
	};
	
//	command=BUSL_3&busl3_action=util_get_stats__1_upsdowns_in_bb_ranges
	
	/***************************
		ajax : exec
		
	 ***************************/
	$.ajax({
		
	    url: _url,
	    type: "GET",
	    data: _data,
	    
	    timeout: 10000
	    
	}).done(function(data, status, xhr) {
		
//		//debug
//		alert("ajax ==> done");
		
		// disp html
		var div_MessageArea = $("div#curr_BUSL_2__Message_Area");
		
		div_MessageArea.html(data);
		
		// bg-color
		div_MessageArea.css("background", cname_Plum);
//		cname_Plum

		// animation
		div_MessageArea
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200);

		
	}).fail(function(xhr, status, error) {
		
		alert("ajax failed ==> " + xhr.status);
		
	});	

}//curr_BUSL_3__Action

function _mm_Index_LinkTo__0() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting...";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/mm/numbering/";
	//var _url = "http://127.0.0.1:8000/im/im_actions";
	//var _url = "http://127.0.0.1:8000/im/actions";
	
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
	//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
	//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
				.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
			.css("background", cname_Red);
	});
	
}//function _mm_Index_LinkTo__0() {

function _mm_Index_LinkTo__1() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting... param is '1'";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/mm/denumbering/";
//	var _url = "http://127.0.0.1:8000/mm/numbering/";
	//var _url = "http://127.0.0.1:8000/im/im_actions";
	//var _url = "http://127.0.0.1:8000/im/actions";
	
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
		//    data: {id: id},
		//    data: {memos: memos, image_id: image_id},
		//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
		//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
		.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
		.css("background", cname_Red);
	});
	
}//function _mm_Index_LinkTo__1() {

function _mm_Index_LinkTo__2() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting... param is '1'";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/mm/build_history/";
//	var _url = "http://127.0.0.1:8000/mm/denumbering/";
	
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
		//    data: {id: id},
		//    data: {memos: memos, image_id: image_id},
		//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
		//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
		.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
		.css("background", cname_Red);
	});
	
}//_mm_Index_LinkTo__2()

function mm_Index_LinkTo(_param) {
	
//	alert("!!param is => '" + _param + "'");
	/***************************
		dispatch
	 ***************************/
	//ref https://www.w3schools.com/jsref/jsref_parseInt.asp
	var index = parseInt(_param);
	
	if (index == 0) {	//[0, "Numbering"]
		
		_mm_Index_LinkTo__0();
		
	}
	
	else if (index == 1) {	//[1, "De-numbering"]
		
		_mm_Index_LinkTo__1();
		
	} else if (index == 2) {	//[2, "Build history"]
			
		_mm_Index_LinkTo__2();
			
	} else {
		
		alert("unknown index => " + _param);
		
	}
	
	
//	/***************************
//		message
//	 ***************************/
//	var msg = "ajax starting...";
//	
//	var elem = $('div#index_Display_Area');
//	
//	elem.html(msg);
////	$('div#index_Display_Area').html(msg);
//	
//	elem.css("background", cname_Yellow);
////	elem.css("background", "yellow");
//	
//	/***************************
//		ajax
//		
//		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
//	 ***************************/
//	var _url = "http://127.0.0.1:8000/mm/numbering/";
////	var _url = "http://127.0.0.1:8000/im/im_actions";
////	var _url = "http://127.0.0.1:8000/im/actions";
//	
////	var _data = {action : _param};
//	
//	$.ajax({
//		
//		url: _url,
//		type: "GET",
//		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
////	    data: {id: id},
////	    data: {memos: memos, image_id: image_id},
////		data: _data,
//		
//		timeout: 10000
//		
//	}).done(function(data, status, xhr) {
//		
////		alert(data);
//		
//		$('div#index_Display_Area').html(data);
//		
//		$('div#index_Display_Area')
//				.css("background", cname_White);
//		
//	}).fail(function(xhr, status, error) {
//		
//		alert(xhr.status);
//		
//		var msg = "ajax returned error";
//		
//		$('div#index_Display_Area').html(msg);
//		
//		$('div#index_Display_Area')
//			.css("background", cname_Red);
//	});
	
}//function mm_Index_LinkTo(_param) {

function exec_Numbering(_param) {
	
//	alert("_param => '" + _param + "'");
	
	/***************************
		get : vars
	 ***************************/
	/***************************
		dpath
	 ***************************/
	var elem = $('input#ipt_Numbering_MainDir');
	
	//ref val https://stackoverflow.com/questions/4088467/get-the-value-in-an-input-text-box answered Apr 9 '13 at 13:28
	var _dpath = elem.val();
	
//	alert("dpath => " + dpath + "'");
	
	/***************************
		fname
	 ***************************/
	var _fname = _param;
	
//	alert("file fullpath => '" + _dpath + "\\" + _fname + "'");
	
	/***************************
		data
	 ***************************/
//	var _data = {action : _param};
	var _data = {dpath : _dpath, fname : _fname};
	
	var _url = "http://127.0.0.1:8000/mm/exec_Numbering/";

	/***************************
		background
	 ***************************/
	var elem = $('div#numbering_content_Message_Area');
	
	elem.css("background", cname_Yellow);
//	elem.css("background", "yellow");
	
	/***************************
		ajaxing
	 ***************************/
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
		data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		alert(data);
		
		$('div#numbering_content_Message_Area').html(data);
		
		$('div#numbering_content_Message_Area')
				.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);

		$('div#numbering_content_Message_Area')
				.css("background", cname_Red);

	});

}//exec_Numbering

function exec_BuildHistory(_param) {
	
//	alert("_param => '" + _param + "'");
	
	/***************************
		get : vars
	 ***************************/
	/***************************
		dpath
	 ***************************/
	var elem = $('input#ipt_Numbering_MainDir');
	
	//ref val https://stackoverflow.com/questions/4088467/get-the-value-in-an-input-text-box answered Apr 9 '13 at 13:28
	var _dpath = elem.val();
	
//	alert("dpath => " + dpath + "'");
	
	/***************************
		fname
	 ***************************/
	var _fname = _param;
	
//	alert("file fullpath => '" + _dpath + "\\" + _fname + "'");
//	
//	return;
	
	/***************************
		data
	 ***************************/
//	var _data = {action : _param};
	var _data = {dpath : _dpath, fname : _fname};
	
	var _url = "http://127.0.0.1:8000/mm/exec_BuildHistory/";
	
	/***************************
		background
	 ***************************/
	var elem = $('div#numbering_content_Message_Area');
	
	elem.css("background", cname_Yellow);
//	elem.css("background", "yellow");
	
	/***************************
		ajaxing
	 ***************************/
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
		data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		alert(data);
		
		$('div#numbering_content_Message_Area').html(data);
		
		$('div#numbering_content_Message_Area')
		.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#numbering_content_Message_Area')
		.css("background", cname_Red);
		
	});
	
}//exec_BuildHistory

function exec_DeNumbering(_param) {
	
	
	/***************************
		get : vars
	 ***************************/
	/***************************
		dpath
	 ***************************/
	var elem = $('input#ipt_DeNumbering_MainDir');
//	var elem = $('input#ipt_Numbering_MainDir');
	
	//ref val https://stackoverflow.com/questions/4088467/get-the-value-in-an-input-text-box answered Apr 9 '13 at 13:28
	var _dpath = elem.val();
	
//	alert("dpath => " + dpath + "'");
	
	/***************************
		fname
	 ***************************/
	var _fname = _param;
	
//	alert("file fullpath => '" + _dpath + "\\" + _fname + "'");
	
//	//debug
//	return;
	
	/***************************
		data
	 ***************************/
//	var _data = {action : _param};
	var _data = {dpath : _dpath, fname : _fname};
	
	var _url = "http://127.0.0.1:8000/mm/exec_DeNumbering/";
//	var _url = "http://127.0.0.1:8000/mm/exec_Numbering/";
	
	/***************************
		background
	 ***************************/
	var elem = $('div#numbering_content_Message_Area');
	
	elem.css("background", cname_Yellow);
//	elem.css("background", "yellow");
	
	/***************************
		ajaxing
	 ***************************/
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
		data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		alert(data);
		
		$('div#numbering_content_Message_Area').html(data);
		
		/***************************
			exception
		 ***************************/
		var substr = "EXCEPTION";
		
//		var res = (data.indexOf(substr) !== -1);
		
		if (data.indexOf(substr) !== -1) {
			
			alert("EXCEPTION");
			
			$('div#numbering_content_Message_Area')
				.css("background", cname_Red);
			
		} else {
			
			$('div#numbering_content_Message_Area')
				.css("background", cname_White);
		}
		
		
//		$('div#numbering_content_Message_Area')
//			.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#numbering_content_Message_Area')
		.css("background", cname_Red);
		
	});
	
}//exec_Numbering

	
function exec_GenPeakData(_param) {
	/***************************
		vars
	 ***************************/
	var t_Start = +new Date();

	
//	alert("_param => '" + _param + "'");
//	
//	//debug
//	return;
	
//	/***************************
//		get : vars
//	 ***************************/
//	/***************************
//		dpath
//	 ***************************/
//	var elem = $('input#ipt_Numbering_MainDir');
//	
//	//ref val https://stackoverflow.com/questions/4088467/get-the-value-in-an-input-text-box answered Apr 9 '13 at 13:28
//	var _dpath = elem.val();
//	
////	alert("dpath => " + dpath + "'");
//	
//	/***************************
//		fname
//	 ***************************/
//	var _fname = _param;
//	
////	alert("file fullpath => '" + _dpath + "\\" + _fname + "'");
//	
	/***************************
		params
	 ***************************/
//	var _data = {action : _param};
	var _data = {fname : _param};
	
	var _url = "http://127.0.0.1:8000/curr/exec_Gen_PeakData/";
//	var _url = "http://127.0.0.1:8000/mm/exec_Numbering/";

	/***************************
		background
	 ***************************/
	var elem = $('div#div_Curr_Basics_Gen_PeakData_Message_Area');
	
	elem.css("background", cname_Yellow);
//	elem.css("background", "yellow");
	
	var txt_Message = "ajax starting for --> '" + _param + "'"
				+ " (" + get_Timelabel_Now_2() + ")";
	
	// log
	console.log(txt_Message);
	
	/***************************
		ajaxing
	 ***************************/
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
		data: _data,
		
		timeout: 20000		// 20 seconds
//		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		alert(data);
		
		$('div#div_Curr_Basics_Gen_PeakData_Result_Area').html(data);
		
		$('div#div_Curr_Basics_Gen_PeakData_Result_Area')
				.css("background", cname_Plum);
		
		/***************************
			time
		 ***************************/
		//ref elapsed https://stackoverflow.com/questions/3528425/how-to-display-moving-elapsed-time-in-jquery answered Apr 29 '17 at 1:04
		var elapsed = +new Date() - t_Start;
		
		var txt_Elapsed = millisToMinutesAndSeconds(elapsed);
		
		/***************************
			message
		 ***************************/
		var msg = "ajax done for --> 'exec_GenPeakData'"
				+ " "
				+ "(" + get_Timelabel_Now_2() + ")"
				+ "(command = 'gen_peak_data')"
				+ "(file = '" + _param + "')"
				+ " (took = " + txt_Elapsed + ")"
				;

		//log
		console.log(msg);
		
		// message
		$('div#div_Curr_Basics_Gen_PeakData_Message_Area').css("background", cname_LightBlue);
		
//		var txt_Message = "ajax done" + _param + " "
//						+ " (" + get_Timelabel_Now_2() + ")";
		
		
		$('div#div_Curr_Basics_Gen_PeakData_Message_Area').html(msg);
//		$('div#div_Curr_Basics_Gen_PeakData_Message_Area').html("Ajax => done");
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status + " (error = '" + error + "')");
//		alert(xhr.status);
		
		/***************************
			time
		 ***************************/
		//ref elapsed https://stackoverflow.com/questions/3528425/how-to-display-moving-elapsed-time-in-jquery answered Apr 29 '17 at 1:04
		var elapsed = +new Date() - t_Start;
		
		var txt_Elapsed = millisToMinutesAndSeconds(elapsed);

		var msg = "ajax returned error : " + error + "(elapsed = " + txt_Elapsed + ")";
		
		//log
		console.log(msg);
		
		$('div#div_Curr_Basics_Gen_PeakData_Message_Area').html(msg);

		$('div#div_Curr_Basics_Gen_PeakData_Message_Area')
				.css("background", cname_Red);

	});

}//exec_GenPeakData


function exec_Tester_BUSL(_param) {
	/***************************
		vars
	 ***************************/
	var t_Start = +new Date();
	
	
//	alert("_param => '" + _param + "'");
	
//	//debug
//	return;
	
	/***************************
		get : vars
	 ***************************/
	/***************************
		dpath
	 ***************************/
	var elem = $('input#ipt_Curr_Tester_BUSL_DpathImages');
	
	//ref val https://stackoverflow.com/questions/4088467/get-the-value-in-an-input-text-box answered Apr 9 '13 at 13:28
	var _dpath = elem.val();
	
//	alert("dpath => " + _dpath + "'");
	
	/***************************
		fname
	 ***************************/
	var _fname = _param;
//	
//	//debug
//	return;
	
////	alert("file fullpath => '" + _dpath + "\\" + _fname + "'");
	/***************************
		params
	 ***************************/
//	var _data = {action : _param};
	var _data = {fname : _param, dpath_image : _dpath};
	
	var _url = "http://127.0.0.1:8000/curr/exec_Tester_BuyUps_SellLows/";
//	var _url = "http://127.0.0.1:8000/mm/exec_Numbering/";
	
	/***************************
		background
	 ***************************/
	var elem = $('div#div_Curr_Basics_Gen_PeakData_Message_Area');
	
	elem.css("background", cname_Yellow);
//	elem.css("background", "yellow");
	
	var txt_Message = "ajax starting for --> '" + _param + "'"
	+ " (" + get_Timelabel_Now_2() + ")";
	
	// log
	console.log(txt_Message);
	
	/***************************
		ajaxing
	 ***************************/
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
//	    data: {id: id},
//	    data: {memos: memos, image_id: image_id},
		data: _data,
		
		timeout: 20000		// 20 seconds
//		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		alert(data);
		// html elements
		var div_Result = $('div#div_Curr_Basics_Gen_PeakData_Result_Area');
		var div_Message = $('div#div_Curr_Basics_Gen_PeakData_Message_Area');
		
		div_Result.html(data);
		
		div_Result.css("background", cname_Plum);
		
		/***************************
			time
		 ***************************/
		//ref elapsed https://stackoverflow.com/questions/3528425/how-to-display-moving-elapsed-time-in-jquery answered Apr 29 '17 at 1:04
		var elapsed = +new Date() - t_Start;
		
		var txt_Elapsed = millisToMinutesAndSeconds(elapsed);
		
		/***************************
			message
		 ***************************/
		var msg = "ajax done for --> 'exec_GenPeakData'"
			+ " "
			+ "(" + get_Timelabel_Now_2() + ")"
			+ "(command = 'gen_peak_data')"
			+ "(file = '" + _param + "')"
			+ " (took = " + txt_Elapsed + ")"
			;
		
		//log
		console.log(msg);
		
		// message
		div_Message.css("background", cname_LightBlue);
//		$('div#div_Curr_Basics_Gen_PeakData_Message_Area').css("background", cname_LightBlue);
		
//		var txt_Message = "ajax done" + _param + " "
//						+ " (" + get_Timelabel_Now_2() + ")";
		
		
		div_Message.html(msg);
//		$('div#div_Curr_Basics_Gen_PeakData_Message_Area').html(msg);
//		$('div#div_Curr_Basics_Gen_PeakData_Message_Area').html("Ajax => done");
		
		// animation
		div_Message
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200);

	}).fail(function(xhr, status, error) {
		
		alert(xhr.status + " (error = '" + error + "')");
//		alert(xhr.status);
		
		/***************************
			time
		 ***************************/
		//ref elapsed https://stackoverflow.com/questions/3528425/how-to-display-moving-elapsed-time-in-jquery answered Apr 29 '17 at 1:04
		var elapsed = +new Date() - t_Start;
		
		var txt_Elapsed = millisToMinutesAndSeconds(elapsed);
		
		var msg = "ajax returned error : " + error + "(elapsed = " + txt_Elapsed + ")";
		
		//log
		console.log(msg);
		
		// tag
		var div_Message = $('div#div_Curr_Basics_Gen_PeakData_Message_Area');
		
		div_Message.html(msg);
//		$('div#div_Curr_Basics_Gen_PeakData_Message_Area').html(msg);
		
		div_Message.css("background", cname_Red);
		
		// animation
		div_Message
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200);
		
	});
	
}//exec_Tester_BUSL


function get_Timelabel_Now() {
	
	//ref https://stackoverflow.com/questions/10211145/getting-current-date-and-time-in-javascript
	//ref https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date
	var currentdate = new Date();
	var datetime = "Last Sync: " + currentdate.getDate() + "/"+currentdate.getMonth() + 1 
//	var datetime = "Last Sync: " + currentdate.getDay() + "/"+currentdate.getMonth() 
		+ "/" + currentdate.getFullYear() + " @ " 
		+ currentdate.getHours() + ":" 
		+ currentdate.getMinutes() + ":" + currentdate.getSeconds();

	return datetime;
	
}

function get_Timelabel_Now_2() {
	
	//ref https://stackoverflow.com/questions/10211145/getting-current-date-and-time-in-javascript
	//ref https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date
	
	var cd = new Date();
//	var currentdate = new Date();
	
//	var month = cd.getMonth() + 1;
	var month = (cd.getMonth() + 1).toString();
	
	if (month.toString().length < 2) {
		
		month = "0" + month;
		
	}
	
	var year = cd.getFullYear().toString();
	var day = cd.getDate().toString();

	if (day.length < 2) {
		
		day = "0" + day;
		
	}

//	alert("month => " + month);
	
//	var datetime = cd.getFullYear() + (cd.getMonth() + 1) + cd.getDay()
//	var datetime = "" + cd.getFullYear() + (month) + cd.getDay()
//	var datetime = "" + cd.getFullYear().toString() + (month).toString() + cd.getDay().toString()
	var datetime = year + month + day
	 			+ "_"
	 			+ cd.getHours() + cd.getMinutes() + cd.getSeconds();
		
//	var datetime = "Last Sync: " + currentdate.getDate() + "/"+currentdate.getMonth() + 1 
////	var datetime = "Last Sync: " + currentdate.getDay() + "/"+currentdate.getMonth() 
//	+ "/" + currentdate.getFullYear() + " @ " 
//	+ currentdate.getHours() + ":" 
//	+ currentdate.getMinutes() + ":" + currentdate.getSeconds();
	
	return datetime;
	
}//function get_Timelabel_Now_2() {

function mm_Index_GO() {
	
	/***************************
		get selected
	 ***************************/
	//ref selection https://learn.jquery.com/using-jquery-core/faq/how-do-i-get-the-text-value-of-a-selected-option/
	//ref get value, not text https://stackoverflow.com/questions/13089944/jquery-get-selected-option-value-not-the-text-but-the-attribute-value Selvakumar Arumugam
	var selection = $( "#select_MM_Actions option:selected" );
//	var selection = $( "#select_MM_Actions option:selected" ).text();
	
	var text = selection.text();
	
	var value = selection.val();
	
//	alert("text => '" + text + "'" + " / " + "val = " + value);

	/***************************
		dispatch
	 ***************************/
	mm_Index_LinkTo(value);
	
}//mm_Index_GO()

/***************************
	<option value="0" class="opt_MM_Actions">Updown patterns</option>
 ***************************/
function _curr_Index_LinkTo__0() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting...";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		clear : message
	 ***************************/
	//ref clear div https://stackoverflow.com/questions/1701973/how-to-clear-all-divs-contents-inside-a-parent-div answered Nov 9 '09 at 16:05
	$('div#index_Message_Area').html('');
	
	$('div#index_Area__Result').html('');
	
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/curr/updown_patterns/";
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
	//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
	//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
				.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
			.css("background", cname_Red);
	});
	
}//function _curr_Index_LinkTo__0() {

function _curr_Index_LinkTo__1() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting...";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		clear : message
	 ***************************/
	$('div#index_Message_Area').html('');
	
	$('div#index_Area__Result').html('');

	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/curr/correlations/";
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
	//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
	//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
				.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
			.css("background", cname_Red);
	});
	
}//function _curr_Index_LinkTo__1() {

function _curr_Index_LinkTo__2() {
	
	/***************************
		message
	 ***************************/
	var msg = "ajax starting... param is '1'";
	
	var elem = $('div#index_Display_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		clear : message
	 ***************************/
	$('div#index_Message_Area').html('');
	
	$('div#index_Area__Result').html('');

	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/mm/build_history/";
//	var _url = "http://127.0.0.1:8000/mm/denumbering/";
	
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
		//    data: {id: id},
		//    data: {memos: memos, image_id: image_id},
		//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
		//	alert(data);
		
		$('div#index_Display_Area').html(data);
		
		$('div#index_Display_Area')
		.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";
		
		$('div#index_Display_Area').html(msg);
		
		$('div#index_Display_Area')
		.css("background", cname_Red);
	});
	
}//_curr_Index_LinkTo__2()

function curr_Index_LinkTo(_param) {
	
//	alert("!!param is => '" + _param + "'");
	/***************************
		dispatch
	 ***************************/
	//ref https://www.w3schools.com/jsref/jsref_parseInt.asp
	var index = parseInt(_param);
	
	if (index == 0) {	//[0, "Numbering"]
		
		_curr_Index_LinkTo__0();
		
	}
	
	else if (index == 1) {	//[1, "De-numbering"]
		
		_curr_Index_LinkTo__1();
		
	} else if (index == 2) {	//[2, "Build history"]
			
		_curr_Index_LinkTo__2();
			
	} else {
		
		alert("unknown index => " + _param);
		
	}
	
	
//	/***************************
//		message
//	 ***************************/
//	var msg = "ajax starting...";
//	
//	var elem = $('div#index_Display_Area');
//	
//	elem.html(msg);
////	$('div#index_Display_Area').html(msg);
//	
//	elem.css("background", cname_Yellow);
////	elem.css("background", "yellow");
//	
//	/***************************
//		ajax
//		
//		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
//	 ***************************/
//	var _url = "http://127.0.0.1:8000/mm/numbering/";
////	var _url = "http://127.0.0.1:8000/im/im_actions";
////	var _url = "http://127.0.0.1:8000/im/actions";
//	
////	var _data = {action : _param};
//	
//	$.ajax({
//		
//		url: _url,
//		type: "GET",
//		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
////	    data: {id: id},
////	    data: {memos: memos, image_id: image_id},
////		data: _data,
//		
//		timeout: 10000
//		
//	}).done(function(data, status, xhr) {
//		
////		alert(data);
//		
//		$('div#index_Display_Area').html(data);
//		
//		$('div#index_Display_Area')
//				.css("background", cname_White);
//		
//	}).fail(function(xhr, status, error) {
//		
//		alert(xhr.status);
//		
//		var msg = "ajax returned error";
//		
//		$('div#index_Display_Area').html(msg);
//		
//		$('div#index_Display_Area')
//			.css("background", cname_Red);
//	});
	
}//function mm_Index_LinkTo(_param) {

function curr_Index_GO() {
	
//	alert("curr index");
	
	var selection = $( "#select_Curr_Actions option:selected" );
//	var selection = $( "#select_MM_Actions option:selected" ).text();
	
	var text = selection.text();
	
	var value = selection.val();

//	//debug
//	alert("text => '" + text + "'" + " / " + "val = " + value);
	
	/***************************
		clear : areas
	 ***************************/
	var area_Display = $('div#index_Display_Area');
	
//	alert(area_Display);
	
//	area_Display.html() = "";
	area_Display.html('');

	// index_Message_Area
	$('div#index_Message_Area').html('');
	
	$('div#index_Area__Result').html('');
	
	
	
	/***************************
		dispatch
	 ***************************/
	curr_Index_LinkTo(value);

}

function curr_Updown_GO() {

//	alert("updown GO");

	/***************************
		message
	 ***************************/
	var msg = "ajax starting...";
	
	var elem = $('div#index_Message_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		param : body volume : up
	 ***************************/
	var tag_Vol_Up = $('input#ipt_Curr_UpdownPatterns_Range_Up');
	
	var val_Vol_Up = tag_Vol_Up.val();
	
	/***************************
		build : data
	 ***************************/
	var _data = {body_volume_up : val_Vol_Up};
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/curr/exec_updown_patterns/";
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
		data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		var tag = $('div#index_Area__Result');
//		
//		tag.html(data);
//		
//		tag
//				.css("background", cname_White);
		
		/***************************
			exception
		 ***************************/
		var substr = "ERROR";
		
		//ref substring https://stackoverflow.com/questions/1789945/how-to-check-whether-a-string-contains-a-substring-in-javascript
		if (data.includes(substr)) {	// detected
			
			//debug
			console.log("'" + substr + "'" + " ==> detected");
			
			var tag = $('div#index_Area__Result');
			
			$('div#index_Area__Result')
				.css("background", cname_Red);

			$('div#index_Area__Result')
				.css("color", cname_White);
			
			$('div#index_Area__Result').html(data);
			
			//ref fadein/out https://stackoverflow.com/questions/275931/how-do-you-make-an-element-flash-in-jquery answered Feb 1 '12 at 14:19
			tag
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
//				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
//				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				
				.fadeIn(TIME_FADE_IN);
			
		} else {
			
			var tag = $('div#index_Area__Result');
			
			$('div#index_Area__Result')
				.css("background", cname_LightBlue);
	
			$('div#index_Area__Result').html(data);
	
			tag
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				
				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
//				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
//				.fadeIn(TIME_FADE_IN).fadeOut(TIME_FADE_OUT)
				
//				.fadeIn(TIME_FADE_IN200).fadeOut(200)
//				.fadeIn(200).fadeOut(200)
//				
//				.fadeIn(200).fadeOut(200)
//				.fadeIn(200).fadeOut(200)
				
				.fadeIn(TIME_FADE_IN);
	
		}
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
		var msg = "ajax returned error";

		var tag = $('div#index_Area__Result');

		tag.html(msg);
		
		tag.css("background", cname_Red);
	});
}

function curr_Correl_GO() {

	/***************************
		message
	 ***************************/
	var msg = "ajax starting... (curr_Correl_GO)";
	
	var elem = $('div#index_Message_Area');
	
	elem.html(msg);
	//$('div#index_Display_Area').html(msg);
	
	elem.css("background", cname_Yellow);
	//elem.css("background", "yellow");
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/curr/exec_correlations/";
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
	//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
	//	alert(data);
		
		var tag = $('div#index_Area__Result');
		
		tag.html(data);
		
		tag
				.css("background", cname_White);
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status + " / " + error);
//		alert(xhr.status);
		
		var msg = "ajax returned error";
	
		var tag = $('div#index_Area__Result');
	
		tag.html(msg);
		
		tag.css("background", cname_Red);
	});

}

function curr_Show_Basics_Table_Commands() {
	
//	alert("show");
	
	//ref toggle https://api.jquery.com/toggle/
	$('#div_Basics_ListOf_Actions').toggle();
	
}//function curr_Show_Basics_Table_Commands() {

function _curr_Basics_Index_GO__Gen_Peak_Data() {
	
	/***************************
		vars
	 ***************************/
	var t_Start = +new Date();
	
	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/curr/gen_peak_data/";
	//var _data = {action : _param};
	
	$.ajax({
		
		url: _url,
		type: "GET",
		//REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
	//	data: _data,
		
		timeout: 10000
		
	}).done(function(data, status, xhr) {
		
//		//test
		//ref http://www.hp-stylelink.com/news/2013/11/20131126.php#list03
//		var huga = 0;
//		var hoge = setInterval(function() {
//		    console.log(huga);
//		    huga++;
//		    //終了条件
////		    if (huga == 10) {
//		    	if (huga == 4) {
//		    clearInterval(hoge);
//		    console.log("終わり");
//		    }
//		}, 500);
		
		
	//	alert(data);
		/***************************
			result
		 ***************************/
		var tag_Result = $('div#div_Curr_Basics_Result_Area');
		
		tag_Result.html(data);
		
		tag_Result.css("background", cname_White);
		
		/***************************
			time
		 ***************************/
		//ref elapsed https://stackoverflow.com/questions/3528425/how-to-display-moving-elapsed-time-in-jquery answered Apr 29 '17 at 1:04
		var elapsed = +new Date() - t_Start;
		
		var txt_Elapsed = millisToMinutesAndSeconds(elapsed);
		
		/***************************
			message
		 ***************************/
		var msg = "ajax done for --> 'gen_peak_data'"
				+ " "
				+ "(" + get_Timelabel_Now_2() + ")"
				+ "(command = 'gen_peak_data')"
				+ " (took = " + txt_Elapsed + ")"
				;
		
		var tag = $('div#div_Curr_Basics_Message_Area');
		
		tag.html(msg);
		
		tag.css("background", cname_LightBlue);
		
		
	}).fail(function(xhr, status, error) {
		
		/***************************
			message
		 ***************************/
//		alert(xhr.status + " / " + error);
	//	alert(xhr.status);
		
		var msg = "ajax returned error (" + xhr.status + " / " + error + ")"
				+ "(" + get_Timelabel_Now_2() + ")"
				+ "(command = 'gen_peak_data')";
//		var msg = "ajax returned error";
	
		var tag = $('div#div_Curr_Basics_Message_Area');
	
		tag.html(msg);
		
		tag.css("background", cname_Red);
	});
	
}//function _curr_Basics_Index_GO__Gen_Peak_Data() {


function curr_Basics_Index_GO(param) {
	
//	//debug
//	alert("param => '" + param + "'");
//	
//	return;
	
	/***************************
		clear : areas
	 ***************************/
	var area_Display = $('div#index_Display_Area');
	
//	alert(area_Display);
	
//	area_Display.html() = "";
	area_Display.html('');

	// index_Message_Area
	var txt_Message = "ajax starting for --> '" + param + "'"
					+ " (" + get_Timelabel_Now_2() + ")";
	
	$('div#div_Curr_Basics_Message_Area').html(txt_Message);
	
	$('div#index_Area__Result').html('');
	
	/***************************
		dispatch
	 ***************************/
	if (param == "gen_peak_data") {

		console.log(param);
		
		var div = $('div#div_Curr_Basics_Message_Area');

		div.css("background", cname_Yellow);
		
		/***************************
			start ajax
		 ***************************/
		_curr_Basics_Index_GO__Gen_Peak_Data();
		
	} else {

		// index_Message_Area
		var txt_Message = "Unknown commdand --> '" + param + "'"
						+ " (" + get_Timelabel_Now_2() + ")";
		
		$('div#div_Curr_Basics_Message_Area').html(txt_Message);
		
		$('div#div_Curr_Basics_Message_Area').css("background", cname_Red);

	}//if (param == )
	

}

function _curr_Tester_Tmpl_BUSL(_param) {
	
	alert("ajax starting for... => '" + _param + "'");

	/***************************
		ajax
		
		ref : C:\WORKS_2\WS\Eclipse_Luna\Cake_IFM11\app\webroot\js\main.js
	 ***************************/
	var _url = "http://127.0.0.1:8000/curr/tester_BuyUps_SellLows";
	//var _url = "http://127.0.0.1:8000/im/actions";
	
	/***************************
		param
	 ***************************/
//	var _data;
	
	$.ajax({
		
	    url: _url,
	    type: "GET",
	    //REF http://stackoverflow.com/questions/1916309/pass-multiple-parameters-to-jquery-ajax-call answered Dec 16 '09 at 17:37
	//    data: {id: id},
	//    data: {memos: memos, image_id: image_id},
//	    data: _data,
	    
	    timeout: 10000
	    
	}).done(function(data, status, xhr) {
		
		/***************************
			result
		 ***************************/
//		alert("ajax => done");
		
		console.log("ajax => done");
		
		var tag = $('div#div_Curr_Tester_Index_Area__Result');
//		var tag = $('div#index_Area__Result');
		
		tag.html(data);
		
	//	$('div#index_Area__Result').html(data);

		/***************************
			message
		 ***************************/
		var tag_Message = $('div#div_Curr_Tester_Index_Area_Message');
//		var tag_Message = $('div#index_Area_Message');
		
		var msg = "ajax => done";
		
		tag_Message.html(msg);
//		tag_Message.html(tag_Message);
		
		tag_Message.css("background", cname_Plum);
		
		tag_Message
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200).fadeOut(200)
			.fadeIn(200).fadeOut(200)
			
			.fadeIn(200);

		
		
	}).fail(function(xhr, status, error) {
		
		alert(xhr.status);
		
	});

	
}

function curr_Tester_Tmpl_Commands(_param) {
	
	/***************************
		validate : update date
	 ***************************/
	var _update;
	
	if ((_param == "buy_Ups_Sell_Lows")
		) {

//		alert("command => '" + _param + "'");
		
		_curr_Tester_Tmpl_BUSL(_param);

	} else {//if ((_param == "buy_Ups_Sell_Lows") ||
		
		alert("unknown command !! => '" + _param + "'");
		
	}//if ((_param == "buy_Ups_Sell_Lows") ||
		

}//function curr_Tester_Tmpl_BUSL(param) {

