var str = vertical_code.getString();
var len = str.length();
var vertical_codeBK = "";
for (i = 0; i < len; i++){
	var word = str.charCodeAt(i);
	word = word.toString();
	vertical_codeBK = vertical_codeBK + word;	
}
