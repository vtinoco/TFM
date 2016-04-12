if (num_pages != null){
	var NewURL = URL.Clone();
	NewURL = NewURL + "/" + resource.replace(" ","") + "/sales?break_down=" + break_down + "&start_date=" + start_date + "&end_date=" + end_date + "&page_index=" + num_pages;
}