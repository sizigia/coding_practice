const sameCase = (str) => (str.toUpperCase() == str || str.toLowerCase() == str) ? true : false;

sameCase("HELLO"), true
sameCase("HEllo"), false
sameCase("mArmALadE"), false
sameCase("marmalade"), true
sameCase("MARMALADE"), true
sameCase("ketchUP"), false
sameCase("pickle"), true
sameCase("MUSTARD"), true