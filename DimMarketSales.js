var str1 = market_code.getString();
var len1 = str1.length();
var bk = "";
for (i = 0; i < len1; i++){
	var word = str1.charCodeAt(i);
	word = word.toString();
	bk = bk + word;	
}
var str = bk;
var len = str.length;
var one = 0;
var two = 0;
var three = 0;
var four = 0;
var five = 0;
var six = 0;
var seven = 0;
var eight = 0;
var nine = 0;
var cero = 0;
for (i = 0; i < len; i++){
	if (str[i] == "1"){one++;}
	else if (str[i] == "2"){two++;}
	else if (str[i] == "3"){three++;}
	else if (str[i] == "4"){four++;}
	else if (str[i] == "5"){five++;}
	else if (str[i] == "6"){six++;}
	else if (str[i] == "7"){seven++;}
	else if (str[i] == "8"){eight++;}
	else if (str[i] == "9"){nine++;}
	else if (str[i] == "0"){cero++;}	
}

one = one.toString();
two = two.toString();
three = three.toString();
four = four.toString();
five = five.toString();
six = six.toString();
seven = seven.toString();
eight = eight.toString();
nine = nine.toString();
cero = cero.toString();

var market_codeBK = one + two + three + four + five + six + seven + eight + nine + cero;