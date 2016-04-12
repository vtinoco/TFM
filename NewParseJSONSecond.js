obj = JSON.parse(sales_list_split);

try{ var sales_list_date = obj.date;}
catch (err) {var sales_list_date = null;}

try{ var sales_list_product_id = obj.product_id; sales_list_product_id = parseInt(sales_list_product_id);}
catch (err) {var sales_list_product_id =  null;}

try{  var sales_list_country = obj.country;}
catch (err) {var sales_list_country =  null;}

try{ var sales_list_units_product_promotions = obj.units.product.promotions; sales_list_units_product_promotions = parseInt(sales_list_units_product_promotions) || 0 ; }
catch (err) {var sales_list_units_product_promotions =  null;}

try{ var sales_list_units_product_downloads = obj.units.product.downloads; sales_list_units_product_downloads = parseInt(sales_list_units_product_downloads) || 0 ;}
catch (err) {var sales_list_units_product_downloads =  null;}

try{ var sales_list_units_product_updates = obj.units.product.updates; sales_list_units_product_updates = parseInt(sales_list_units_product_updates)|| 0 ;}
catch (err) {var sales_list_units_product_updates =  null;}

try{ var sales_list_units_product_refunds = obj.units.product.refunds; sales_list_units_product_refunds = parseInt(sales_list_units_product_refunds) || 0 ;}
catch (err) {var sales_list_units_product_refunds =  null;}

try{ var sales_list_units_product_borrowed_downloads = obj.units.product.borrowed_downloads; sales_list_units_product_borrowed_downloads = parseInt(sales_list_units_product_borrowed_downloads) || 0 ;}
catch (err) {var sales_list_units_product_borrowed_downloads =  null;}

try{ var sales_list_units_product_net_downloads = obj.units.product.net_downloads; sales_list_units_product_net_downloads = parseInt(sales_list_units_product_net_downloads) || 0 ;}
catch (err) {var sales_list_units_product_net_downloads =  null;}

try{ var sales_list_units_product_free_downloads = obj.units.product.free_downloads; sales_list_units_product_free_downloads = parseInt(sales_list_units_product_free_downloads) || 0 ;}
catch (err) {var sales_list_units_product_free_downloads =  null;}

try{ var sales_list_units_product_beta_units = obj.units.product.beta_units; sales_list_units_product_beta_units = parseInt(sales_list_units_product_beta_units) || 0 ;}
catch (err) {var sales_list_units_product_beta_units =  null;}

try{ var sales_list_units_product_trial_units = obj.units.product.trial_units; sales_list_units_product_trial_units = parseInt(sales_list_units_product_trial_units) || 0 ;}
catch (err) {var sales_list_units_product_trial_units =  null;}

try{ var sales_list_units_iap_promotions = obj.units.iap.promotions; sales_list_units_iap_promotions = parseInt(sales_list_units_iap_promotions) || 0;}
catch (err) {var sales_list_units_iap_promotions =  null;}

try{ var sales_list_units_iap_sales = obj.units.iap.sales; sales_list_units_iap_sales = parseInt(sales_list_units_iap_sales) || 0;}
catch (err) {var sales_list_units_iap_sales =  null;}

try{ var sales_list_units_iap_refunds = obj.units.iap.refunds; sales_list_units_iap_refunds = parseInt(sales_list_units_iap_refunds) || 0;}
catch (err) {var sales_list_units_iap_refunds =  null;}

try{ var sales_list_revenue_ad = obj.revenue.ad; sales_list_revenue_ad = parseFloat(sales_list_revenue_ad) || 0;}
catch (err) {var sales_list_revenue_ad =  null;}

try{ var sales_list_revenue_product_promotions = obj.revenue.product.promotions; sales_list_revenue_product_promotions = parseFloat(sales_list_revenue_product_promotions) || 0.0;}
catch (err) {var sales_list_revenue_product_promotions =  null;}

try{ var sales_list_revenue_product_downloads = obj.revenue.product.downloads; sales_list_revenue_product_downloads = parseFloat(sales_list_revenue_product_downloads) || 0.0; }
catch (err) {var sales_list_revenue_product_downloads =  null;}

try{ var sales_list_revenue_product_updates = obj.revenue.product.updates; sales_list_revenue_product_updates = parseFloat(sales_list_revenue_product_updates) || 0.0;}
catch (err) {var sales_list_revenue_product_updates =  null;}

try{ var sales_list_revenue_product_refunds = obj.revenue.product.refunds; sales_list_revenue_product_refunds = parseFloat(sales_list_revenue_product_refunds) || 0.0;}
catch (err) {var sales_list_revenue_product_refunds =  null;}

try{ var sales_list_revenue_product_trial_upgrade_revenue = obj.revenue.product.trial_upgrade_revenue; sales_list_revenue_product_trial_upgrade_revenue = parseFloat(sales_list_revenue_product_trial_upgrade_revenue) || 0.0;}
catch (err) {var sales_list_revenue_product_trial_upgrade_revenue =  null;}

try{ var sales_list_revenue_iap_sales = obj.revenue.iap.sales; sales_list_revenue_iap_sales = parseFloat(sales_list_revenue_iap_sales)|| 0.0;}
catch (err) {var sales_list_revenue_iap_sales =  null;}

try{ var sales_list_revenue_iap_refunds = obj.revenue.iap.refunds; sales_list_revenue_iap_refunds = parseFloat(sales_list_revenue_iap_refunds)|| 0.0;}
catch (err) {var sales_list_revenue_iap_refunds =  null;}

try{ var sales_list_revenue_iap_promotions = obj.revenue.iap.promotions; sales_list_revenue_iap_promotions = parseFloat(sales_list_revenue_iap_promotions) || 0.0;}
catch (err) {var sales_list_revenue_iap_promotions =  null;}