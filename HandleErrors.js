obj = JSON.parse(result);

try{ var code = obj.code; code = parseInt(code);}
catch (err) {var code = null;}

try{ var sales_list_data = JSON.stringify(obj.sales_list);}
catch (err) {var sales_list_data =  null;}

try{ var page_num = obj.page_num; page_num = parseInt(page_num);}
catch (err) {var page_num =  null;}