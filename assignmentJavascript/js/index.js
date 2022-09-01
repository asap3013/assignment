let fnameNode=document.getElementById('fname');
let lnameNode=document.getElementById('lname');
let contactNode=document.getElementById('mobile');
let contactNode2=document.getElementById('officeno');
let emailNode=document.getElementById('emailid');
let passNode=document.getElementById('pass');
let cpassNode=document.getElementById('c_pass');
let aboutNode=document.getElementById("about1"); 
let errorNode1=document.getElementById('error1');
let errorNode2=document.getElementById('error2');
let errorNode3=document.getElementById('error3');
let errorNode4=document.getElementById('error4');
let errorNode5=document.getElementById('error5');
let errorNode6=document.getElementById('error6');
let errorNode7=document.getElementById('error7');
let errorNode8=document.getElementById("error8");
let errorNode9=document.getElementById("error9");
let errorNode10=document.getElementById('error10');
let errorNode11=document.getElementById('error11');
const errorBorder="2px solid red";
const successBorder="2px solid green";

function validateForm(){
    let s1=validate1();
    let s2=validate2();
    let s3=validate3();
    let s4=validate4();
    let s5=validate5();
    let s6=validate6();
    let s7=validate7();
    let s8=radioValidation();
    let s9=aboutValidation();
    let s10=checkbox();
    let s11=calculateAge();
    let s12=ageCheck();
    console.log(s1 && s2 && s3 && s4 && s5 && s6 && s7 && s8 && s9 && s10 && s11 && s12);
    return(s1 && s2 && s3 && s4 && s5 && s6 && s7 && s8 && s9 && s10 && s11 && s12);
}
window.onload = function(){
    let years = document.getElementById("year");
    let currentYear = (new Date()).getFullYear();
    for (let year = 1900; year <= currentYear; year++) {
        let option = document.createElement("option");
        option.innerHTML = year;
        option.value = year;
        years.appendChild(option);
    }
};


function validate1(){
    let fname=fnameNode.value;
    let regExp= new RegExp("^[a-zA-Z]+$"); 
    errorNode1.innerHTML="";  
    if(fname===''){
        errorNode1.innerHTML="First name is Compulsory";
        fnameNode.style.border=errorBorder;
        return false;
    }
    else if(regExp.test(fname)==false){
        errorNode1.innerHTML="Number Not Allowed in Name";
        fnameNode.style.border=errorBorder;
        return false;
    }
    else{
        fnameNode.style.border=successBorder;
        return true;
    }
}
function validate2(){
    let lname=lnameNode.value; 
    let regExp= new RegExp("^[a-zA-Z]+$"); 
    errorNode2.innerHTML="";  
    if(lname===''){
        errorNode2.innerHTML="Last name is Compulsory";
        lnameNode.style.border=errorBorder;
        return false;
    }
    else if(regExp.test(lname)==false){
        errorNode2.innerHTML="Name Only contain Alphabet";
        lnameNode.style.border=errorBorder;
        return false;
    }
    else{
        lnameNode.style.border=successBorder;
        return true;
    }
}

function validate3(){
    let mobile=contactNode.value;  
    let regExp= new RegExp("^[0-9]{10}$");  
    errorNode3.innerHTML="";  
    if(mobile===''){
        errorNode3.innerHTML="Phone Number is Compulsory";
        contactNode.style.border=errorBorder;
        return false;
    }
    else if(regExp.test(mobile)==false){
        errorNode3.innerHTML="Please enter valid Phone number";
        contactNode.style.border=errorBorder;
        return false;
    }
    else{
        contactNode.style.border=successBorder;
        return true;
    }
}

function validate4(){
    let officeno=contactNode2.value;  
    let regExp= new RegExp("^[0-9]{11}$");  
    errorNode4.innerHTML="";  
    if(officeno===''){
        errorNode4.innerHTML="Office Number is Compulsory";
        contactNode2.style.border=errorBorder;
        return false;
    }
    else if(regExp.test(officeno)==false){
        errorNode4.innerHTML="Please enter valid Office number";
        contactNode2.style.border=errorBorder;
        return false;
    }
    else{
        contactNode2.style.border=successBorder;
        return true;
    }
}
function validate5() {
    let email = emailNode.value;
    errorNode5.innerHTML = "";
    var regExp= new RegExp ("^[a-zA-Z0-9_]+@[a-zA-Z_]+.[a-zA-Z]{2,4}$");
    let ss1 = email.substring(0, email.indexOf('@'));
    let ss2 = email.substring(email.indexOf('@') + 1);

    console.log(ss1);
    console.log(ss2);
    if (email === '') {
        errorNode5.innerHTML = "Email Id is required";
        emailNode.style.border = errorBorder;
        return false;
    }
    else if (regExp.test(email)==false) {
        errorNode5.innerHTML = "Please provide proper email";
        emailNode.style.border = errorBorder;
        return false;
    }
    
    else {
        emailNode.style.border = successBorder;
        return true;
    }
}

function validate6(){
    let password=passNode.value;
    let regExp= new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,12})");
    errorNode6.innerHTML="";
    console.log(regExp.test(password));
    if(password===''){
        errorNode6.innerHTML="password is Compulsory";
        passNode.style.border=errorBorder;
        return false;
    }
    else if (regExp.test(password)==false){
        errorNode6.innerHTML="min size=8,1capital letter,1small letter,1No,1symbol";
        passNode.style.border=errorBorder;
        return false;
    }
    else{
        passNode.style.border=successBorder;
        return true;
    }
}
function validate7(){
    let password=passNode.value;
    let c_password=cpassNode.value
    errorNode7.innerHTML="";
    if(c_password===''){
        errorNode7.innerHTML="confirm password is Compulsory";
        cpassNode.style.border=errorBorder;
        return false;
    }
    else if (c_password!=password){
        errorNode7.innerHTML="password should match";
        cpassNode.style.border=errorBorder;
        return false;
    }
    else{
        cpassNode.style.border=successBorder;
        return true;
    }
}
function radioValidation(){
    if (document.getElementById("male").checked === false  &&  document.getElementById("female").checked === false ){
        errorNode8.innerHTML= "Please choose your Gender";
        return false;
    }
    else{
        errorNode8.innerHTML=''
        return true;
    }
}
function aboutValidation(){ 
    let about1=aboutNode.value;
    errorNode9.innerHTML=""; 
    if(about1==="" || about1===null){
        errorNode9.innerHTML="Enter some review";
        aboutNode.style.border=errorBorder;
        return false;
    }
    else{
        aboutNode.style.border=successBorder;
        return true;
    }
}


function checkbox(){
    let ch1=document.getElementById('checkbox_1').checked;
    let ch2=document.getElementById('checkbox_2').checked;
    let ch3=document.getElementById('checkbox_3').checked;

    if(ch1===false && ch2===false && ch3===false){
        errorNode10.innerHTML="Please select at least one check box";
        return false;
    }   
}
function check(){
    let errorNode10 = document.getElementById('error11');
    if(document.getElementById('checkbox_1').checked===true || document.getElementById('checkbox_2').checked===true || document.getElementById('checkbox_3').checked===true){
        errorNode10.innerHTML='';
    }

};
function ageCheck(){
    console.log("hello2")
    var  day= document.getElementById("day").value;
    var  month= document.getElementById("month").value;
    var   year= document.getElementById("year").value;
    console.log(day);
    console.log(month);
    console.log(year);


    
    if (day === "day"){
        console.log("h1")
        document.getElementById("error11").style.display= "block";
        errorNode11.innerHTML= "please select proper date format";
    
    }else if (month === "month"){
        console.log("h2")
        document.getElementById("error11").style.display= "block";
        errorNode11.innerHTML= "please select proper date format";
    
    }else if(year === "year" ){
        console.log("h3")
        document.getElementById("error11").style.display= "block";
        errorNode11.innerHTML= "please select proper date format";
    
    }else{
        console.log("h4")
        document.getElementById("error11").style.display= "none";
        errorNode11.innerHTML= "";
    }
};
function calculateAge(){
    console.log("hello")

    let  day= document.getElementById("day").value;
    let  month= document.getElementById("month").value;
    let  year= document.getElementById("year").value;
    if(month == "4"){
        document.getElementById("day29").style.display="block";
        document.getElementById("day30").style.display="block";
        
        document.getElementById("day31").style.display = "none";
    };
    if(month == "6" ){
        document.getElementById("day29").style.display="block";
        document.getElementById("day30").style.display="block";
        
        document.getElementById("day31").style.display = "none";
    };
    if(month == "9" ){
        document.getElementById("day29").style.display="block";
        document.getElementById("day30").style.display="block";

        document.getElementById("day31").style.display = "none";
    };
    if(month == "11"){
        document.getElementById("day29").style.display="block";
        document.getElementById("day30").style.display="block";
        document.getElementById("day31").style.display = "none";
    };
    
  if(month == "2" && (year % 4 == 0)){
    document.getElementById("day29").style.display="block";
            document.getElementById("day30").style.display = "none";
            document.getElementById("day31").style.display = "none";
    }else if(month == "2" && (!(year % 4)== 0)){
            document.getElementById("day29").style.display = "none";
            document.getElementById("day30").style.display = "none";
            document.getElementById("day31").style.display = "none";
    }
    else if(month=="1" || month=="3"|| month=="5"|| month=="7"|| month=="8" ){
        document.getElementById("day29").style.display="block";
        document.getElementById("day30").style.display="block";
        document.getElementById("day31").style.display="block";
    };
    if( day != "day" && month != "month" && year != "year" ){
        var stringDate = month + "/" + day + "/" + year 
        var timestamp = Date.parse(stringDate);
        var dateObject = new Date(timestamp);
        var currentYear = new Date().getFullYear();
        var birthYear = dateObject.getFullYear();
        var age = currentYear - birthYear;
        var today = new Date();
    var birthDate = new Date(stringDate);
        var m = today.getMonth() - birthDate.getMonth();
        if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) 
    {
        age=age-1;
        m=12+m
    }
    var age=String(age)+String("."+m);
    age= age + " years"
        document.getElementById("txt-age").value = age;
    }
};
