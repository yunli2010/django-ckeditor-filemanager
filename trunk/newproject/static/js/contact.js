function validateContact(return_message){
		submit_to_next_step = false;
		
		var fullname = $("id_fullname").value;
		$("id_fullname").style.color = "#000";
		$("id_fullname").style.border = "solid 2px #666666";

		var email = $("id_email").value;
		$("id_email").style.color = "#000";
		$("id_email").style.border = "solid 22pxpx #666666";

		var contact_number = $("id_contact_number").value;
		$("id_contact_number").style.color = "#000";
		$("id_contact_number").style.border = "solid 2px #666666";		

		var comment = $("id_comment").value;
		$("id_comment").style.color = "#000";
		$("id_comment").style.border = "solid 2px #666666";		

		$k = 0;
		error_fields = Array();
		ferror_fields = Array();
		if(trim(fullname) == ""){
			$("id_fullname").style.color = "#FF0000";
			$("id_fullname").style.border = "solid 2px #FF0000";
			error_fields[$k] = "Fullname";
			ferror_fields[$k] = "fullname";
			$k++;
		}
		
		if(ValidateEmail($("id_email").value) == false)
		{
			$("id_email").style.color = "#FF0000";
			$("id_email").style.border = "solid 2px #FF0000";
			error_fields[$k] = "Email Address";
			ferror_fields[$k] = "email";
			$k++;
		}
	
		if(trim(contact_number) == ""){
			$("id_contact_number").style.color = "#FF0000";
			$("id_contact_number").style.border = "solid 2px #FF0000";
			error_fields[$k] = "Contact Number";
			ferror_fields[$k] = "contact_number";
			$k++;
		}

		if(trim(comment) == ""){
			$("id_comment").style.color = "#FF0000";
			$("id_comment").style.border = "solid 2px #FF0000";
			error_fields[$k] = "Message";
			ferror_fields[$k] = "comment";
			$k++;
		}

		tc_join_word = " ";

		err_msg = "";
		flag_fields = "";
		if(error_fields.length != 0){
			join_word = " are";
			for($k=0;$k<error_fields.length;$k++){
				if(error_fields.length != 1 && $k == (error_fields.length-1)){
					err_msg += " and "	
				}else{
					join_word = " is";
				}
				flag_fields += "|" + error_fields[$k];

				err_msg += error_fields[$k];
			
				if($k != (error_fields.length-2) && $k != (error_fields.length-1)){
					err_msg += ", ";			
				}
			}
			err_msg += join_word + " not filled in correctly.";
			tc_join_word = " Also, ";		
		}

		if(error_fields.length == 0){
			submit_to_next_step = true;
		}
		

		if(return_message == true){
			if(submit_to_next_step){
				document.frmOrder.submit();
				return true;
			}else{
				alert(err_msg);
			}
		}
		return false;
}

function echeck(str) {
	var at="@"
	var dot="."
	var lat=str.indexOf(at)
	var lstr=str.length
	var ldot=str.indexOf(dot)
	if (str.indexOf(at)==-1){
	   return false
	}

	if (str.indexOf(at)==-1 || str.indexOf(at)==0 || str.indexOf(at)==lstr){
	   return false
	}

	if (str.indexOf(dot)==-1 || str.indexOf(dot)==0 || str.indexOf(dot)==lstr){
		return false
	}

	 if (str.indexOf(at,(lat+1))!=-1){
		return false;
	 }

	 if (str.substring(lat-1,lat)==dot || str.substring(lat+1,lat+2)==dot){
		return false;
	 }

	 if (str.indexOf(dot,(lat+2))==-1){
		return false;
	 }
	
	 if (str.indexOf(" ")!=-1){
		return false;
	 }

	 return true;
}

function ValidateEmail(email_address){
	if ((email_address==null)||(email_address=="")){
		return false;
	}
	if (echeck(email_address)==false){
		email_address = "";
		return false;
	}
	return true;
}

function trim(s)
{
	var l=0; var r=s.length -1;
	while(l < s.length && s[l] == ' ')
	{	l++; }
	while(r > l && s[r] == ' ')
	{	r-=1;	}
	return s.substring(l, r+1);
}
