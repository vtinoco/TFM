obj = JSON.parse(result);

try{ var code = obj.code;}
catch (err) {var code = null;}

try{ var currency = obj.currency;}
catch (err) {var currency =  null;}

try{  var vertical = obj.vertical;}
catch (err) {var vertical =  null;}

try{ var market = obj.market;}
catch (err) {var market =  null;}

try{ var page_num = obj.page_num;}
catch (err) {var page_num =  null;}

try{ var page_index = obj.page_index;}
catch (err) {var page_index =  null;}

try{ var next_page = obj.next_page;}
catch (err) {var next_page =  null;}

try{ var prev_page = obj.prev_page;}
catch (err) {var prev_page =  null;}

try{ 
	var len = obj.sales_list.length;
	var sales_list_output = "";
	for (var i = 0; i < len; i++){		
	if (i == 0){
			try{ sales_list_output = JSON.stringify(obj.sales_list[i]) ;}
			catch (err) {sales_list_output = "[]";}
	}
	else {
			try{ sales_list_output = sales_list_output + ";" + JSON.stringify(obj.sales_list[i]) ;}
			catch (err) {sales_list_output = sales_list_output + ";" + "[]";}
	} 
		
	}	
}
catch (err) {var sales_list_data =  null;}