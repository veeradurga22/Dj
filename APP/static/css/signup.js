function Name(name,nameerror){
    var x = document.getElementById(name).value
    var letters = /^[A-Za-z]+$/;
    if(x.match(letters) && x.length>=3)
     {
        document.getElementById(name).style.border="1px solid cyan"
        document.getElementById(nameerror).style.display="none"
        return true;

     }
     else{
        
        document.getElementById(name).style.border="2px solid red";
        document.getElementById(nameerror).style.display="inline";
        return false
     }
}

function ValidateEmail() 
{
    var gmail = document.getElementById('email').value;
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(gmail))
    {
        document.getElementById('email').style.border="1px solid cyan"
        document.getElementById('emailerror').style.display="none"
        return true;
    }
    else{
        document.getElementById('email').style.border="2px solid red"
        document.getElementById('emailerror').style.display="inline"        
        return (false)
    }
        
}
function CheckPassword() 
{ 
    inputtxt = document.getElementById('password').value;
    var decimal=  /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{6,20}$/;
    if(inputtxt.match(decimal)) 
    { 
        document.getElementById('password').style.border="1px solid cyan"
        document.getElementById('passworderror').style.display="none"       
        return true;
    }
    else
    { 
        document.getElementById('password').style.border="2px solid red"
        document.getElementById('passworderror').style.display="inline"       
        return false;
    }
} 
function Phone(){
    var ph = document.getElementById("phone").value;
    if(/^[6789]\d{9}$/.test(ph)){
        document.getElementById('phone').style.border="1px solid cyan"
        document.getElementById('phoneerror').style.display="none" 
        return true
    }
    else{
        document.getElementById('phone').style.border="2px solid red"
        document.getElementById('phoneerror').style.display="inline" 
        return false
    }

}

function Pin(){
    var pin = document.getElementById("pin").value;
    if(pin.length==6){
        document.getElementById('pin').style.border="1px solid cyan"
        document.getElementById('pinerror').style.display="none" 
        return true
    }
    else{
        document.getElementById('pin').style.border="2px solid red"
        document.getElementById('pinerror').style.display="inline" 
        return false
    }
}
function Check(){
    var c = document.getElementById('registerCheck').checked;
    if(c){
        document.getElementById('registerCheck').style.border="1px solid cyan"
        document.getElementById('registerCheckerror').style.display="none" 
        return true
    }
    else{
        document.getElementById('registerCheck').style.border="2px solid cyan"
        document.getElementById('registerCheckerror').style.display="inline" 
        return false
    }
}
function Submit(){
    if(Name('firstname','firstnameerror') && Name('lastname','lastnameerror') && ValidateEmail() && CheckPassword() && Phone() && Pin() && Check()){
        return true
    }
    else{
        if(!Name("firstname",'firstnameerror')){
            Name("firstname",'firstnameerror')
        }
        if(!Name("lastname",'lastnameerror')){
            Name("lastname",'lastnameerror')
        }
        if(!ValidateEmail()){
            ValidateEmail();
        }
        if(!CheckPassword()){
            CheckPassword();
        }
        if(!Phone()){
            Phone();
        }
        if(!Pin()){
            Pin();
        }
        if(!Check()){
            Check();
        }
        return false;
    }
}