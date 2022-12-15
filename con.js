// let a=6;
// a=String(a)                      //string 
// console.log(a, typeof a)

// let a='123';
// console.log(a, typeof a)


// let a=8;
// console.log(a,typeof a)

// let a=8;
// a=a+" "                         
// console.log(a, typeof a)   // string 

// let a=8;
// a=a-2
// console.log(a, typeof a)   // number

// let a=8;
// a= !a
// console.log(a,typeof a)

// console.log(Boolean(0))  //false
// console.log(Boolean(12)) //true
// console.log(Boolean(null))           //false
// console.log(Boolean(undefined))      //false


// let a='10';
// a=+a+2                          //number
// console.log(a, typeof a)

// let a='10';
// a=a+2                          //string concenation
// console.log(a, typeof a)


// let a=Number("123tanu");
// console.log(a)             //NaN

// a='9'+2+23-'5'   //9218
// console.log(a);

// b='23'*2+'2'+12-2   //46210
// console.log(b)










// a=Number(undefined)
// console.log(a)     //NaN

// a=Number(null)
// console.log(a)   //0

// a=null
// b=true
// c=false
// // console.log(a+b+c) //1
// // console.log(a-b+c) //-1
// console.log(a+b)
// console.log(a-b)

// a=null
// b=undefined
// console.log(a+b)   //NaN
// console.log(a/b)    //NaN


// a=null
// b=true
// console.log(a/b)   //0
// console.log(a*b)    //0
// console.log(a*b*10)   //0


// a='12'
// b=10
// c='5'
// console.log(a+b-c)  //1205
// console.log(a+b+c)    //12105
// console.log((a+b)/c)  //242
// console.log(a*b*c)     //600
// console.log(b+a+c)     //10125



// Implicit Conversion to String//


// numeric string used with + gives string type
// let result;

// result = '3' + 2; 
// console.log(result) // "32"

// result = '3' + true; 
// console.log(result); // "3true"

// result = '3' + undefined; 
// console.log(result); // "3undefined"

// result = '3' + null; 
// console.log(result); // "3null" 


// Implicit Conversion to Number

// numeric string used with - , / , * results number type

// let result;
// result = '4' - '2'; 
// console.log(result); // 2

// result = '4' - 2;
// console.log(result); // 2

// result = '4' * 2;
// console.log(result); // 8

// result = '4' / 2;
// console.log(result); // 2




// Non-numeric String Results to NaN


// non-numeric string used with - , / , * results to NaN

// let result;

// result = 'hello' - 'world';
// console.log(result); // NaN

// result = '4' - 'hello';
// console.log(result); // NaN

//  Implicit Boolean Conversion to Number


// if boolean is used, true is 1, false is 0

// let result;

// result = '4' - true;
// console.log(result); // 3

// result = 4 + true;
// console.log(result); // 5

// result = 4 + false;
// console.log(result); // 4



// null Conversion to Number

// null is 0 when used with number
// let result;

// result = 4 + null;
// console.log(result);  // 4

// result = 4 - null;
// console.log(result);  // 4


// undefined used with number, boolean or null



// let result;

// result = 4 + undefined;
// console.log(result);  // NaN

// result = 4 - undefined;
// console.log(result);  // NaN

// result = true + undefined;
// console.log(result);  // NaN

// result = null + undefined;
// console.log(result);  // NaN

// Convert to Number Explicitly

// let result;

// // string to number
// result = Number('324');
// console.log(result); // 324

// result = Number('324e-1')  
// console.log(result); // 32.4

// // boolean to number
// result = Number(true);
// console.log(result); // 1

// result = Number(false);
// console.log(result); // 0




// let result;
// result = Number(null);
// console.log(result);  // 0

// let result = Number(' ')
// console.log(result);  // 0


// let result;
// result = Number('hello');
// console.log(result); // NaN

// result = Number(undefined);
// console.log(result); // NaN

// result = Number(NaN);
// console.log(result); // NaN


// let result;
// result = parseInt('20.01');
// console.log(result); // 20

// result = parseFloat('20.01');
// console.log(result); // 20.01

// result = +'20.01';                    
// console.log(result); // 20.01

// result = Math.floor('20.01');
// console.log(result); // 20

// let a=String(123)
// console.log(typeof a)

//number to string
// let result;
// result = String(324);
// console.log(result);  // "324"

// result = String(2 + 4);
// console.log(result); // "6"

// //other data types to string
// result = String(null);
// console.log(result); // "null"

// result = String(undefined);
// console.log(result); // "undefined"

// result = String(NaN);
// console.log(result); // "NaN"

// result = String(true);
// console.log(result); // "true"

// result = String(false);
// console.log(result); // "false"

// // using toString()
// result = (324).toString();
// console.log(result); // "324"

// result = true.toString();
// console.log(result); // "true"







//  //////false example


// let result;
// result = Boolean('');
// console.log(result); // false

// result = Boolean(0);
// console.log(result); // false

// result = Boolean(undefined);
// console.log(result); // false

// result = Boolean(null);
// console.log(result); // false

// result = Boolean(NaN);
// console.log(result); // false


//  // // // // All other values give true. For example,

// result = Boolean(324);
// console.log(result); // true

// result = Boolean('hello');
// console.log(result); // true

// result = Boolean(' ');
// console.log(result); // true