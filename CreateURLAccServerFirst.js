var first_date = new Date(first_sales_date.getString());
var last_date = new Date(last_sales_date.getString());
var current_date =  new Date(current_sales_date.getString());
var real_current_date = new Date(current_date.setDate(current_date.getDate() + 1));

if(real_current_date > last_date ){
 	var start_date = null;
	var end_date = null;
}
else{
	if (first_date > current_date){
		var start_date = first_sales_date.getString();
		var end_date = last_sales_date.getString();
	}
	else{
		var start_date = date2str(real_current_date, "yyyy/MM/dd");
		var end_date = last_sales_date.getString();
	}
}