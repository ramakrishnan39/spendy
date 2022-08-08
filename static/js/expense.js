function show_exp() {
    document.getElementById('container_exp').setAttribute("style", "display:flex");
    document.getElementById('txt_expname').focus();
}

function show_inc(){
    document.getElementById('container_inc').setAttribute("style", "display:flex");
    document.getElementById('txt_incname').focus();
    
}

function go_index(){
    window.location.href = "/";
}

function go_profile(){
    window.location.href = "/profile/";
}

function previewFile() {
    var preview = document.getElementById('profile_pic');
    var file    = document.getElementById('profile-img-chooser').files[0];
    var reader  = new FileReader();
  
    reader.onloadend = function () {
      preview.src = reader.result;
    }
  
    if (file) {
      reader.readAsDataURL(file);
    } else {
      preview.src = "";
    }
  }

function updateProfile(){
    window.location.href = "/profile/";
}

function js_register()
{
    pwd = document.getElementById('pwd_signin').value;
    pwd_confirm = document.getElementById('pwd_signin_2').value;
    if (pwd === pwd_confirm)
    {
        form_sign = document.getElementById('frm_signup');
        form_sign.setAttribute('method', 'post');
        form_sign.setAttribute('action', '../register/');
        
    }
    else
    {
        var res = document.createElement("p");
        var text = document.createTextNode("Passwords are not matched! ");
        res.appendChild(text)
    }
}

function addexpense() {
    var expense_name = prompt("Please enter the expense name ");
    var amount = prompt("Please enter the amount ")
    var ddate = document.getElementById('appdate').value;
    var sdate = ddate.toString();
    if (amount === null || typeof amount ==="") { amount = 0 }
    else { amount = Number(amount) }
    window.location.href ="/add/" + expense_name + "/" + amount + "/" + sdate;
}

function addexp()
{
    var exp_id = document.getElementById('exp_id').value;
    var expense_name = document.getElementById('txt_expname').value;
    var amount = document.getElementById('txt_expamt').value;
    var desc = document.getElementById('txt_expdesc').value;
    var ddate = document.getElementById('appdate').value;
    var sdate = ddate.toString();
    if (amount === null || typeof amount ==="") { amount = 0 }
    else { amount = Number(amount) }

    if (desc === null || desc === "") { desc = "None" }
    if (exp_id == null || exp_id == "" ) { 
        window.location.href ="/add/" + expense_name + "/" + amount +"/"+ desc + "/" + sdate; 
    }
    else { 
        exp_id = parseInt(exp_id);
        window.location.href ="/update/"+exp_id+"/"+ expense_name + "/" + amount +"/"+ desc + "/" + sdate;
    }
}


function addinc()
{
    var inc_id = document.getElementById('inc_id').value;
    var inc_name = document.getElementById('txt_incname').value;
    var amount = document.getElementById('txt_incamt').value;
    var desc = document.getElementById('txt_incdesc').value;
    var ddate = document.getElementById('appdate').value;
    var sdate = ddate.toString();
    if (amount === null || typeof amount ==="") { amount = 0 }
    else { amount = Number(amount) }

    if (desc === null || desc === "") { desc = "None" }
    if (inc_id == null || inc_id == "" ) { 
        window.location.href ="/add_inc/" + inc_name + "/" + amount +"/"+ desc + "/" + sdate; 
    }
    else { 
        inc_id = parseInt(inc_id);
        window.location.href ="/update_inc/"+inc_id+"/"+ inc_name + "/" + amount +"/"+ desc + "/" + sdate;
    }
}


function showedit_exp( exp_id, exp_name, exp_amount , exp_desc)
{
    show_exp();
    document.getElementById('txt_expname').value = exp_name;
    document.getElementById('txt_expamt').value = exp_amount;
    document.getElementById('txt_expdesc').value = exp_desc;
    document.getElementById('exp_id').value = exp_id ;
}


function showedit_inc( inc_id, inc_name, inc_amount , inc_desc)
{
    show_inc();
    document.getElementById('txt_incname').value = inc_name;
    document.getElementById('txt_incamt').value = inc_amount;
    document.getElementById('txt_incdesc').value = inc_desc;
    document.getElementById('inc_id').value = inc_id ;
}

function deleteexpense(expid) {
    expid = parseInt(expid);
    var ddate = document.getElementById('appdate').value;
    var sdate = ddate.toString();
    window.location.href = "/delete/"+expid+"/"+sdate;
}


function deleteincome(incid) {
    incid = parseInt(incid);
    var ddate = document.getElementById('appdate').value;
    var sdate = ddate.toString();
    window.location.href = "/delete_inc/"+incid+"/"+sdate;
}

function js_report()
{
    mon_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December'];
    try{
     var appdate = document.getElementById('appdate').value;
    }
    catch(TypeError){
        appdate = new Date().getDate();
    }
    var ddate = new Date(appdate);
    var mon = mon_list[ddate.getMonth()];
    var yr = ddate.getFullYear();
    window.location.href = "/report/"+mon+"/"+yr;
}

function js_report_by_mon()
{
    mon_list = ['None','January', 'February', 'March', 'April', 'May', 'June', 'July',
     'August', 'September', 'October', 'November', 'December'] ;
    var ddate = document.getElementById('mon_picker').value;
    var mon = mon_list[Number(String(ddate).substr(5,7))];
    var yr = String(ddate).substr(0,4);
    document.getElementById('mon_picker').value = ddate;
    window.location.href = "/report/"+mon+"/"+yr;
    
}

function go_find()
{
    window.location.href = "/find/";
}

function js_find()
{
    var exp = document.getElementById("txt_txn").value;
    window.location.href = "/find/"+exp;
}

function viewall()
{
    var ddate = document.getElementById('appdate').value;
    var sdate = ddate.toString();
    window.location.href = "/home/" + sdate;
}

function go_home()
{   
    var ddate = new Date();
    var sdate = ddate.toISOString().slice(0,10);
    window.location.href = "/home/" + sdate;
}

function logout()
{
    window.location.href = "/logout/";
}

